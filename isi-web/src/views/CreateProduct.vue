<script lang="ts" setup>
/** Yajing Liu: 
 * It is the frontend about creating products. 
 * The major function of this page of code is to show a view for users to create a new product and send requests to backend. 
 * The difficulty is in the handling of the photos */
import axios from "axios";
import {computed, reactive, ref} from "vue";
import config from "../config"
import {useRouter} from 'vue-router'
import {useStore} from 'vuex'
import FormData from 'form-data'

const router = useRouter()
const store = useStore()

const name = ref("")
const brand = ref("")
const price = ref("")
const thumbnail = ref("")
const information = ref("")
const pic = ref("")
const file = new File([],'')
const thumbnailImage = ref(file)
const img = reactive([] as Array<File>)
const imgList = ref([])

const initImage = () => {
  if(img.length > 0){
    while(img.length > 0){
      img.pop()
      imgList.value.pop()
    }
  }
}

const onFileChange = (event) => {
  initImage()
  const files = event.target.files || event.dataTransfer.files;
  if (files.length > 4){
    alert("We can only handle at most 4 different detailed photographs.")
    for (let i = 0; i < 4; i++){
    img.push(files[i])
  }
  }else{
    for (let i = 0; i < files.length; i++){
      img.push(files[i])
    }
  }
  for(let i = 0; i < img.length; i++){
      let reader = new FileReader()
      reader.readAsDataURL(img[i])
      reader.onload = function (){
        let dataURL = reader.result as string
        // @ts-ignore
        imgList.value.push(dataURL)
      }
    }
}
const thumbnailChange = (event) => {
  const files = event.target.files || event.dataTransfer.files;
  thumbnailImage.value = files[0]
  let reader = new FileReader()
  reader.readAsDataURL(thumbnailImage.value)
  reader.onload = function (){
  let dataURL = reader.result as string
  let output = document.getElementById('ThumbnailImage') as HTMLImageElement
  output.src = dataURL
  }
}

const createProduct = () => {
  if (name.value === "" || brand.value === "" || price.value === "" || information.value === "" || thumbnailImage.value.name === "" || img.length == 0) {
    alert("Please fill in all the fields.")
  } else {
    if (store.state.userStatus === 'vendor') {
      thumbnail.value = thumbnailImage.value.name
      //thumbnail.value = img[0].name
      //pic.value = img.value.name
      let picString = ''
      picString = thumbnail.value + ";"
      for (let i = 0; i < img.length - 1; i++) {
        picString = picString + img[i].name + ';'
      }
      picString = picString + img[img.length - 1].name
      pic.value = picString
      const formData = new FormData();
      formData.append("images", thumbnailImage.value)
      for (let i = 0; i < img.length; i++) {
        formData.append('images', img[i])
      }
      const queryImage = "http://" + config.apiServer + ":" + config.port + "/api/image/upload"
      axios.post(queryImage, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(() => {
        const query = "http://" + config.apiServer + ":" + config.port + "/api/product/create"
        axios.post(query, {
          pName: name.value,
          brand: brand.value,
          price: price.value,
          pDesc: information.value,
          thumbnail: thumbnail.value,
          pic: pic.value,
        }).then((res) => {
          if (res.data.status === 'success') {
            router.push('/product/' + res.data.pid)
          } else {
            alert(res.data.status)
          }
        })
      })
    } else {
      alert("You do not have the authority to add a new product.")
    }
  }
  
}

</script>
<template>
  <div class="min-h-full flex items-center justify-center py-6 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-4">
      <router-link to="/manage">
        <div class="text-cyan-800">
          <div class="inline text-xl">&lsaquo;&nbsp;</div>
          <div class="inline text-md">Go Back</div>
        </div>
      </router-link>
      <h2 class="text-left font-medium text-gray-900">
        <div class="text-2xl">Create New Product</div>
      </h2>
      <div class="creation_form">
        <div class="border rounded-lg shadow-lg bg-white px-4">
          <div class="mt-4 mb-4">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Name</label
            >
            <input
                v-model="name"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder=""
                required
                type="text"
            />
          </div>
          <div class="mt-4 mb-4">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Brand</label
            >
            <input
                v-model="brand"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder=""
                required
                type="text"
            />
          </div>
          <div class="mt-4 mb-4">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Price</label
            >
            <input
                v-model="price"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder=""
                required
                type="number"
            />
          </div>
          <div class="mt-4 mb-4">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Thumbnail Image</label
            >
            <img class="shadow-xl rounded-xl border" id="ThumbnailImage">
            <input
                accept="image/*"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder=""
                required
                type="file"
                @change="thumbnailChange"
            />
          </div>
          <div class="mt-4 mb-4">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Detailed Photographs (1-4 Photographs)</label
            >
            <div v-for="pic in imgList">
              <img :src="pic" class="shadow-xl rounded-xl border">
            </div>
            <input
                accept="image/*"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder=""
                required
                type="file"
                @change="onFileChange"
                multiple
            />
          </div>
          <div class="mt-4 mb-4">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Detail Information</label
            >
            <textarea
                v-model="information"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder=""
                required
                type="text"
            />
          </div>
        </div>
      </div>
      <button
          class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          type="submit"
          @click="createProduct"
      >
        Add
      </button>
    </div>
  </div>
</template>