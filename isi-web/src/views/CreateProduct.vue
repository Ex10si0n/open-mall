<script lang="ts" setup>
import axios from "axios";
import {ref} from "vue";
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


function onFileChange(event){
    const files = event.target.files || event.dataTransfer.files;
    const img = files[0]
    thumbnail.value = img.name
    const formData = new FormData();
    formData.append("image", img)
    const query = "http://" + config.apiServer + ":" + config.port + "/api/image/upload"
    axios.post(query, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })

    //var reader = new FileReader()
    //reader.onload = () => {
    //    alert(reader.result)
    //}
    //if (img){
    //    reader.readAsArrayBuffer(img);
    //}
}

const createProduct = () => {
    if (store.state.userStatus === 'vendor'){
        const query = "http://" + config.apiServer + ":" + config.port + "/api/product/create"
        axios.post(query, {
            pName: name.value,
            brand: brand.value,
            price: price.value,
            pDesc: information.value,
            thumbnail: thumbnail.value,
            pic: pic.value,
        }).then((res) => {
            if(res.data.status === 'success'){
                alert(res.data.status)
                router.push('/product/' + res.data.pid)
            }else{
                alert(res.data.status)
            }
        })
    }else{
        alert("You do not have the authority to add a new product.")
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
                            type="text"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder=""
                            required
                            v-model="name"
                        />
                    </div>
                    <div class="mt-4 mb-4">
                        <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                        >Brand</label
                        >
                        <input
                            type="text"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder=""
                            required
                            v-model="brand"
                        />
                    </div>
                    <div class="mt-4 mb-4">
                        <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                        >Price</label
                        >
                        <input
                            type="number"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder=""
                            required
                            v-model="price"
                        />
                    </div>
                    <div class="mt-4 mb-4">
                        <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                        >Thumbnail Image</label
                        >
                        <input
                            type="file"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder=""
                            required
                            @change="onFileChange"
                            accept="image/*"
                        />
                    </div>
                    <div class="mt-4 mb-4">
                        <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                        >Detail Information</label
                        >
                        <textarea
                            type="text"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder=""
                            required
                            v-model="information"
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