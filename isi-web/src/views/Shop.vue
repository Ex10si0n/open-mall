<script setup lang="ts">
// import { reactive, ref, watch, computed } from 'vue'
import {reactive} from "vue";
import {useStore} from "vuex";
import axios from "axios";
import config from "../config";

const store = useStore();

type ProductState = {
  pid: string;
  pname: string;
  brand: string;
  price: number;
  pdesc: string;
  thumbnail: string;
  pic: string;
};

const products = reactive([] as Array<ProductState>);

axios
    .get("http://" + config.apiServer + ":" + config.port + "/api/products")
    .then((res) => {
      // console.log(res.data.product_list);
      const productList = res.data.product_list;
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
      });
    })
    .catch((error) => console.log(error));

const chgViewingProduct = (pid: string) => {
  store.commit("chgViewingProduct", pid);
};

chgViewingProduct("");
</script>

<template>
  <div
      class="flex items-center justify-center min-h-full px-4 py-6 bg-red sm:px-6 lg:px-8"
  >
    <div class="w-full max-w-md space-y-8">
      <div class="sticky top-0 z-50 w-full max-w-md bg-slate-100 space-y-8">
        <h2 class="text-2xl font-medium text-left text-gray-900">
          <span class="font-bold">Open</span> Mall
          <div class="text-sm text-gray-500">Online Shopping Mall Project for ISI</div>
        </h2>
        <div class="w-full max-w-md space-y-8">
          <div class="relative flex flex-wrap items-stretch w-full mb-4 input-group">
            <input
                type="search"
                class="form-control relative flex-auto min-w-0 block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-slate-200 bg-clip-padding border-2 border-solid border-gray-100 rounded-lg transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none"
                placeholder="Search"
                aria-label="Search"
                aria-describedby="button-addon2"
            />
          </div>
        </div>
      </div>
      <div class="grid grid-cols-2 gap-3">
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
