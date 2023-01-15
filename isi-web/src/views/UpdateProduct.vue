<script lang="ts" setup>
/** Yajing Liu: 
 * It is the frontend about editing products. 
 * The major function of this page of code is to show a view for users to edit products and send requests to backend. 
 * The difficulty is in the handling of the photos */
import axios from "axios";
import {reactive, ref} from "vue";
import config from "../config"
import {useRoute, useRouter} from 'vue-router'
import {useStore} from 'vuex'

const router = useRouter()
const route = useRoute()
const store = useStore()

const pid = route.params.pid
const name = ref("")
const brand = ref("")
const price = ref("")
const thumbnailURL = ref("")
const information = ref("")
const file = new File([],'')
const thumbnailImage = ref(file)
const picList = ref([])
const imgList = ref([])
const img = reactive ([] as Array<File>)
const picString = ref("")
const thumbnailName = ref("")

const thumbnailChange = (event) => {
  const files = event.target.files || event.dataTransfer.files;
  thumbnailImage.value = files[0]
  let reader = new FileReader()
  reader.readAsDataURL(thumbnailImage.value)
  reader.onload = function (){
    let dataURL = reader.result as string
    thumbnailURL.value = dataURL
  }
  thumbnailName.value = thumbnailImage.value.name
  let temp = picString.value.split(";")
  temp[0] = thumbnailName.value
  picString.value = temp.join(";")
}

const addPic = (event) => {
  const files = event.target.files || event.dataTransfer.files;
  let allowNo = 4 - picList.value.length - imgList.value.length
  if (files.length > allowNo){
    alert("We can only handle at most 4 different detailed photographs.")
    for (let i = 0; i < allowNo; i++){
      img.push(files[i])
    }
  }else{
    for (let i = 0; i < files.length; i++){
      img.push(files[i])
    }
  }
  for (let i = 0; i < img.length; i++){
    if(picString.value === ""){
      picString.value = img[i].name
    }else{
      picString.value = picString.value + ";" + img[i].name
    }
    let reader = new FileReader()
    reader.readAsDataURL(img[i])
    reader.onload = function (){
    let dataURL = reader.result as string
      // @ts-ignore
      imgList.value.push(dataURL)
  }
  }
}

const getProduct = async () => {
  const query = "http://" + config.apiServer + ":" + config.port + "/api/product/" + pid
  axios.get(query).then((res) => {
    console.log(res.data)
    name.value = res.data.product.pname
    brand.value = res.data.product.brand
    price.value = res.data.product.price
    information.value = res.data.product.pdesc
    thumbnailURL.value =
      "http://" +
      config.apiServer +
      ":" +
      config.port +
      "/api/img/" +
      res.data.product.thumbnail;
    thumbnailName.value = res.data.product.thumbnail
    picString.value = res.data.product.pic
    let pics = []
    let temp = res.data.product.pic.split(";")
    for (let i = 1; i < temp.length; i++){
      // @ts-ignore
      pics.push("http://" + config.apiServer + ":" + config.port + "/api/img/" + temp[i])
    }
    picList.value = pics
  })
}

getProduct()

const updateProduct = () => {  
  if (name.value === "" || brand.value === "" || price.value === "" || information.value === "" || thumbnailName.value === "" || (picList.value.length === 0 && imgList.value.length === 0)) {
    alert("Please fill in all the fields.")
   } else {
    if (store.state.userStatus === 'vendor') {
      if(img.length > 0 || thumbnailImage.value.size > 0){
        const formData = new FormData();
        if(thumbnailImage.value.name !== ""){
          formData.append("images", thumbnailImage.value)
        }
        for (let i = 0; i < img.length; i++){
          formData.append('images', img[i])
        }
        const queryImage = "http://" + config.apiServer + ":" + config.port + "/api/image/upload"
        axios.post (queryImage, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(() => {
          const query = "http://" + config.apiServer + ":" + config.port + "/api/product/" + pid + "/update"

          axios.post(query, {
            pid: pid,
            pName: name.value,
            brand: brand.value,
            price: price.value,
            pDesc: information.value,
            thumbnail: thumbnailName.value,
            pic: picString.value,
          }).then((res) => {
            if (res.data.status === 'success') {
              router.push('/product/' + res.data.pid)
            } else {
              alert(res.data.status)
            }
          })
        })
      }
      else {
        const query = "http://" + config.apiServer + ":" + config.port + "/api/product/" + pid + "/update"

        axios.post(query, {
          pid: pid,
          pName: name.value,
          brand: brand.value,
          price: price.value,
          pDesc: information.value,
          thumbnail: thumbnailName.value,
          pic: picString.value,
        }).then((res) => {
          if (res.data.status === 'success') {
            router.push('/product/' + res.data.pid)
          } else {
            alert(res.data.status)
          }
        })

      }
    } else {
      alert("You do not have the authority to add a new product.")
  }
  } 
}

const deletePic = (url) => {
  const picName = url.split('/')[url.split('/').length - 1]
  picList.value = picList.value.filter((pic: string) => {
    return pic.split('/')[pic.split('/').length - 1] !== picName
  })
  let pics = picString.value.split(';')
  pics = pics.filter((p: string) => {
    return p !== picName
  })
  picString.value = pics.join(";")
  const query = "http://" + config.apiServer + ":" + config.port + "/api/image/delete"
  axios.post(query, {
    picName: picName
    })
}

const deleteAddedPic = (url) => {
  imgList.value = imgList.value.filter((imgURL) => {
      imgURL !== url
    })
    let temp = picString.value.split(";")
    for(let i = 0; i < img.length; i++){
      let reader = new FileReader()
      reader.readAsDataURL(img[i])
      reader.onload = function (){
      let dataURL = reader.result as string
      if (dataURL === url){
        alert("I am here.")
        for(let j = i; j < (img.length - 1); j ++){
          img[j] = img[j+1]
          temp[j] = temp[j+1]
        }
        img.pop()
        temp.pop()
      }
      picString.value = temp.join(";")
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
        <div class="text-2xl">Update Product</div>
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
            <img :src="thumbnailURL" class="shadow-xl rounded-xl border" id="ThumbnailImage">
            <button class="text-sm text-black-500 text-left py-3">
                Replace the thumbnail image by uploading a new image here :
            </button>
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
            <div v-for="pic in picList">
              <img :src="pic" class="shadow-xl rounded-xl border">
              <button @click="deletePic(pic)" class="text-sm text-red-500 text-center pb-3">
                Delete
              </button>
            </div>
            <div v-for="pic in imgList">
              <img :src="pic" class="shadow-xl rounded-xl border">
              <button @click="deleteAddedPic(pic)" class="text-sm text-red-500 text-center pb-3">
                Delete
              </button>
            </div>
            <input
                accept="image/*"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder=""
                required
                type="file"
                @change="addPic"
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
          @click="updateProduct"
      >
        Update
      </button>
    </div>
  </div>
</template>
