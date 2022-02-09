<script setup lang="ts">
import { computed, reactive, ref } from "vue";
import { useStore } from "vuex";
import { useRouter, useRoute, onBeforeRouteLeave, onBeforeRouteUpdate } from "vue-router";
import Carousel from "../components/Carousel.vue";
import config from "../config";
import axios from "axios";

const store = useStore();

const address = computed(() => {
  return store.state.primaryAddress;
});

const route = useRoute();

type ProductState = {
  pid: string;
  pname: string;
  brand: string;
  price: number;
  pdesc: string;
  thumbnail: string;
  pic: Array<string>;
  // pic: string;
};

const product = reactive({} as ProductState);

axios
  .get(
    "http://" + config.apiServer + ":" + config.port + "/api/product/" + route.params.pid
  )
  .then((res) => {
    console.log(
      "http://" +
        config.apiServer +
        ":" +
        config.port +
        "/api/product/" +
        route.params.pid
    );
    const json = res.data.product;
    product.pid = json.pid;
    product.pname = json.pname;
    product.brand = json.brand;
    product.price = json.price;
    product.pdesc = json.pdesc;
    // product.pic =
    //   "http://" + config.apiServer + ":" + config.port + "/api/img/" + json.pic;
    product.pic = [];
    json.pic.split(";").forEach((pic: string) => {
      console.log(pic);
      product.pic.push(
        "http://" + config.apiServer + ":" + config.port + "/api/img/" + pic
      );
    });

    console.log(product);
  })
  .catch((error) => console.log(error));
</script>

<template>
  <div class="min-h-full flex items-center justify-center py-6 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div class="bg-white max-w-sm rounded-lg overflow-hidden border shadow-sm">
        <div>
          <!-- <img v-for="pic in product.pic" :src="pic" alt="Product" /> -->
          <!-- <img :src="product.pic" alt="" /> -->
          <Carousel :pic="product.pic" />
        </div>
        <div class="px-6 py-4">
          <h2 class="text-left text-2xl font-medium text-gray-900">
            {{ product.pname }}, <span class="font-bold">{{ product.brand }}</span>
            <div class="my-2 text-xl font-medium text-orange-500">
              HK$ {{ product.price }}
            </div>
            <div class="text-sm text-gray-500">
              {{ product.pdesc }}
            </div>
          </h2>
        </div>
      </div>

      <div class="bg-white max-w-sm rounded-lg overflow-hidden border shadow-sm">
        <button
          type="submit"
          class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md rounded-b-none shadow-sm text-white bg-orange-600 hover:bg-orange-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-800"
        >
          Add to Shopping Cart
        </button>
        <div class="px-6 py-4">
          <div class="font-medium text-xl mb-2">Shipping to</div>
          <div class="grid grid-cols-3">
            <div class="col-span-1 text-md font-bold mb-2">{{ address.name }}</div>
            <div class="col-span-2 text-right text-md mb-2">{{ address.tel }}</div>
          </div>
          <div class="col-span-1 text-md bold mb-2">
            {{ address.city }}, {{ address.country }}
          </div>
          <div class="col-span-1 text-md bold mb-2">
            {{ address.detailed }}
          </div>
          <p class="text-gray-700 text-base"></p>
        </div>
        <div class="grid grid-cols-3 px-6 pt-4 pb-2">
          <div class="col-span-1">
            <span
              class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
              >#{{ address.tag.toUpperCase() }}</span
            >
          </div>
        </div>
      </div>
      <div>
        <button
          type="submit"
          class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          style="display: none"
        >
          Change Password
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
