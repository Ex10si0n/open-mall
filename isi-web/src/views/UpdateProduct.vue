<script lang="ts" setup>
import axios from "axios";
import {ref} from "vue";
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
const pic = ref("")

const updateProduct = () => {
    if (store.state.userStatus === 'vendor'){
        const query = "http://" + config.apiServer + ":" + config.port + "/api/product/" + pid + "/update"
        axios.post(query, {
            pid: pid,
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
    <div class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-md w-full space-y-8">
            <h2 class="text-left font-medium text-gray-900">
                <div class="text-2xl mt-4">Update Product</div>
            </h2>
            <div class="creation_form">
                <div class="border rounded-lg rounded-b-none shadow-lg bg-white px-4">
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
            @click="updateProduct"
        >
          Update
        </button>
        </div>
    </div>
</template>