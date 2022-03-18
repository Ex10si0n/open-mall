<script lang="ts" setup>
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
const thumbnail = ref("")
const information = ref("")
const file = new File([],'')
const thumbnailImage = ref(file)
const picList = ref([])

const thumbnailChange = (event) => {
  const files = event.target.files || event.dataTransfer.files;
  thumbnailImage.value = files[0]
  console.log(thumbnailImage)
}

const getProduct = async () => {
  const query = "http://" + config.apiServer + ":" + config.port + "/api/product/" + pid
  axios.get(query).then((res) => {
    console.log(res.data)
    name.value = res.data.product.pname
    brand.value = res.data.product.brand
    price.value = res.data.product.price
    information.value = res.data.product.pdesc
    thumbnail.value =
      "http://" +
      config.apiServer +
      ":" +
      config.port +
      "/api/img/" +
      res.data.product.thumbnail;
    let pics = []
    res.data.product.pic.split(";").forEach((pic: string) => {
      pics.push("http://" + config.apiServer + ":" + config.port + "/api/img/" + pic)
    });
    console.log(pics)
    picList.value = pics
  })
}

getProduct()

const updateProduct = () => {
  if (store.state.userStatus === 'vendor') {
    const query = "http://" + config.apiServer + ":" + config.port + "/api/product/" + pid + "/update"
    axios.post(query, {
      pid: pid,
      pName: name.value,
      brand: brand.value,
      price: price.value,
      pDesc: information.value,
      thumbnail: thumbnail.value,
      pic: picList.value,
    }).then((res) => {
      if (res.data.status === 'success') {
        alert(res.data.status)
        router.push('/product/' + res.data.pid)
      } else {
        alert(res.data.status)
      }
    })
  } else {
    alert("You do not have the authority to add a new product.")
  }
}

const deletePic = (url) => {
  const picName = url.split('/')[url.split('/').length - 1]
  console.log(picName)
  const otherPics = picList.value.filter((pic: string) => {
    return pic.split('/')[pic.split('/').length - 1] !== picName
  })
  let res = ''
  otherPics.forEach((pic: string) => {
    res += pic.split('/')[pic.split('/').length - 1] + ';'
  })
  console.log("other:", res.substring(0, res.length - 1))
  // To Jane: upload `res` to the db
}

const addPic = () => {
  // get new pic name

  // upload new pic to server db/img

  let res = ''
  picList.value.forEach((pic: string) => {
    res += pic.split('/')[pic.split('/').length - 1] + ';'
  })
  console.log("updatedPic:", res)
  // append new pic name to res

  // update server db

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
            <img :src="thumbnail" class="shadow-xl rounded-xl border">
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
          @click="createProduct"
      >
        Add
      </button>
    </div>
  </div>
</template>
