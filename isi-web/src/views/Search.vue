<script setup lang="ts">
import axios from "axios";
import {reactive, ref} from "vue";
import config from "../config"
import {useRouter} from 'vue-router'
import {useStore} from 'vuex'

const router = useRouter()
const store = useStore()
// const count = ref(0)

const content = ref("")
type ProductState = {
  pid: string;
  pname: string;
  brand: string;
  price: number;
  pdesc: string;
  thumbnail: string;
  pic: string;
};

const result = ref("");

const products = reactive([] as Array<ProductState>);
const search = () => {
  var searchResult1 = true
  var searchResult2 = true
  axios
      .get("http://" + config.apiServer + ":" + config.port + "/api/search/name/" + content.value)
      .then((res) => {
        if (res.data.status === 'success') {
          const productList = res.data.products;
          productList.forEach((product: ProductState) => {
            product.pic =
                "http://" + config.apiServer + ":" + config.port + "/api/img/" + product.pic;
            product.thumbnail =
                "http://" +
                config.apiServer +
                ":" +
                config.port +
                "/api/img/" +
                product.thumbnail;
            products.push(product as ProductState);
          })
        } else if (res.data.status === 'none'){
          searchResult1 = false
          if(store.state.userStatus != 'vendor'){
            result.value = "None"
          }
        }
        if (store.state.userStatus === 'vendor') {
          axios
          .get("http://" + config.apiServer + ":" + config.port + "/api/search/id/" + content.value)
          .then((res) => {
            if (res.data.status === 'success') {
              searchResult2 = true;
              const product = res.data.product;
              product.pic =
                "http://" + config.apiServer + ":" + config.port + "/api/img/" + product.pic;
              product.thumbnail =
                "http://" +
                config.apiServer +
                ":" +
                config.port +
                "/api/img/" +
                product.thumbnail;
              products.push(product as ProductState);
            } else if (res.data.status === 'none'){
                searchResult2 = false;
              if (!searchResult1 && !searchResult2) {
                result.value = "None"
              }
            }
          })
        }
      })
}
</script>
<template>
  <div class="flex items-center justify-center min-h-full px-4 py-6 bg-red sm:px-6 lg:px-8">
    <div class="w-full max-w-md space-y-4">
      <div class="sticky top-0 z-50 w-full max-w-md bg-slate-100">
        <router-link to="/">
          <div class="text-cyan-800">
            <div class="inline text-xl">&lsaquo;&nbsp;</div>
            <div class="inline text-md">Go Back</div>
          </div>
        </router-link>
        <h2 class="text-3xl font-medium text-left text-gray-900">
          <span class="font-bold">Search for {{ content }}</span>
        </h2>
        <div class="relative flex flex-wrap my-4 items-stretch w-full input-group">
          <input
              type="search"
              class="form-control relative flex-auto min-w-0 block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-slate-200 bg-clip-padding border-2 border-solid border-gray-100 rounded-lg transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none"
              placeholder="Search"
              aria-label="Search"
              aria-describedby="button-addon2"
              v-model="content"
              @keyup.enter="search"
              autofocus
          />
        </div>
        <div class="grid grid-cols-2 gap-3">
          <select class="col-span-1 bg-white rounded-lg w-full p-2  mb-3 shadow-2xl">
            <option value="all">All Brands</option>
            <option v-for="brand in products_brands" :value="brand">{{ brand }}</option>
          </select>
          <select class="col-span-1 bg-white rounded-lg w-full p-2  mb-3 shadow-2xl">
            <option value="all">Sort default</option>
            <option>Price (Low to High)</option>
            <option>Price (High to Low)</option>
            <option>Mostly Viewed</option>
            <option>Featured</option>
          </select>
        </div>
      </div>
      <div><p>{{ result }}</p></div>
      <div class="grid grid-cols-1 gap-3">
        <div
            v-for="product in products"
            class="max-w-md bg-white border rounded-lg grid-cols-1 shadow-sm"
            @click="
            $router.push('/product/' + product.pid);
            chgViewingProduct(product.pid);
          "
        >
          <img class="py-0 rounded-t-lg" :src="product.thumbnail"/>
          <div class="px-5 py-2 pb-5">
            <h3 class="font-semibold tracking-tight text-gray-900 text-md">
              {{ product.pname }}
            </h3>
            <h3 class="text-sm font-semibold tracking-tight text-gray-500">
              {{ product.pdesc.split(" ").slice(0, 8).join(" ") }}
            </h3>
            <div class="flex items-center mt-2.5 mb-5">
              <span
                  class="bg-blue-100 text-blue-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded"
              >{{ product.brand }}</span
              >
            </div>
            <div class="flex items-center justify-between">
              <span class="font-bold text-gray-700 text-md">HK${{ product.price }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>