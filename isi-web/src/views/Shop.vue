<script setup lang="ts">
// import { reactive, ref, watch, computed } from 'vue'
import {computed, reactive, ref} from "vue";
import {useStore} from "vuex";
import axios from "axios";
import config from "../config";
import {useRouter} from "vue-router"
// import Pagination from '../components/Pagination.vue';

const store = useStore();
const router = useRouter();

const userStatus = computed(() => {
  return store.state.userStatus;
});

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

const cnt = ref(4)

const currentPage = ref(1);

const sortPrice = ref("default")

const brandFilter = ref("all")


// const updateCnt = () => {
//   cnt.value = cnt.value + 4;
// }

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

const search = () => {
  router.push("/search")
}

const userName = computed(() => {
  return store.state.userName;
});

const products_brands = computed(() => {
  return products.map((product) => product.brand).filter((brand, index, self) => self.indexOf(brand) === index).sort();
});

const filtered_products = computed(() => {

  if (brandFilter.value === "all") {
    return products;
  } else {
    if (sortPrice.value === 'l2h') {
      return products.sort((a, b) => a.price - b.price).filter((product) => product.brand === brandFilter.value);
    } else if (sortPrice.value === 'h2l') {
      return products.sort((a, b) => b.price - a.price).filter((product) => product.brand === brandFilter.value);
    } else {
      return products.filter((product) => product.brand === brandFilter.value);
    }
  }
});

const maxPage = computed(() => {
  return Math.ceil(filtered_products.value.length / cnt.value);
});

const displayed_products = computed(() => {
  const start = (currentPage.value - 1) * cnt.value;
  const end = start + cnt.value;
  return filtered_products.value.slice(start, end);
});

const chgPage = () => {
  // console.log(displayed_products.value);

  if (typeof currentPage.value === "number") {
    if (currentPage.value > maxPage.value) {
      currentPage.value = maxPage.value;
    } else if (currentPage.value < 1) {
      currentPage.value = 1;
    }
  } else {
    currentPage.value = 1;
  }
  window.scrollTo(0,0);
};

const prevPage = () => {
  currentPage.value = currentPage.value - 1;
  chgPage()
};

const nextPage = () => {
  currentPage.value = currentPage.value + 1;
  chgPage()
}

const initPage = () => {
  currentPage.value = 1;
  chgPage()
}

</script>

<template>
  <div
      class="flex items-center justify-center min-h-full px-4 py-6 sm:px-6 lg:px-8"
  >
    <div class="w-full max-w-md space-y-8">
      <div class="sticky top-0 z-55 w-full max-w-md bg-slate-100 space-y-8">
        <h2 v-if="userStatus !== 'vendor'" class="text-2xl grid grid-cols-2 font-medium text-gray-900">
          <span class="col-span-1"><span class="font-bold ">Open</span>Mall</span>
          <span class="col-span-1 text-gray-500 text-[19px] text-right">Hi, {{ userName }}</span>
          <div class="text-sm col-span-2 text-gray-500">Online Shopping Mall Project for ISI</div>
        </h2>
        <div v-else class="">
          <router-link to="/manage">
            <div class="text-cyan-800">
              <div class="inline text-xl">&lsaquo;&nbsp;</div>
              <div class="inline text-md">Go Back</div>
            </div>
          </router-link>
          <h2 class="text-2xl grid grid-cols-2 font-medium text-gray-900">
            <span class="col-span-1"><span class="font-bold ">Modify</span> Products</span>
          </h2></div>

        <div class="w-full max-w-md space-y-8 ">
          <div class="relative flex flex-wrap items-stretch w-full input-group backdrop-blur-sm rounded-2xl ">
            <input
                type="search"
                class="form-control relative flex-auto min-w-0 block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-slate-200 bg-clip-padding border-2 border-solid border-gray-100 rounded-lg transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none"
                placeholder="Search"
                aria-label="Search"
                aria-describedby="button-addon2"
                @click="search"
            />
            <div class="grid grid-cols-2 gap-3">
              <select @change="initPage()" v-model="brandFilter" class="col-span-1 bg-white rounded-lg w-full p-2 mt-4 mb-3 shadow-2xl">
                <option value="all">All Brands</option>
                <option v-for="brand in products_brands" :value="brand">{{ brand }}</option>
              </select>
              <select @change="initPage()" v-model="sortPrice" class="col-span-1 bg-white rounded-lg w-full p-2 mt-4 mb-3 shadow-2xl">
                <option value="default">Sort default</option>
                <option value="l2h">Price (Low to High)</option>
                <option value="h2l">Price (High to Low)</option>
                <option value="most">Mostly Viewed</option>
                <option value="feat">Featured</option>
              </select>
            </div>
          </div>
        </div>
      </div>
      <div class="grid grid-cols-1 gap-3">
        <div
            v-for="product in displayed_products"
            class="max-w-md bg-white border rounded-lg grid-cols-1 shadow-sm"
            @click="
              $router.push('/product/' + product.pid);
              chgViewingProduct(product.pid);
            "
        >
<!--          <div v-if="product.brand == brandFilter || brandFilter === 'all'">-->
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
<!--        </div>-->
      </div>
<!--      <div class="text-blue-500 text-center" @click="updateCnt">More</div>-->
      <div class="w-full">
        <div class="bg-black p-2 bg-white rounded-lg text-white rounded-b-none shadow">
          Page {{ currentPage }} of {{ maxPage }}
          </div>
          <div class="p-2 bg-white rounded-lg shadow rounded-t-none">
            <div class="text-lg text-left">
              <input @update="chgPage" class="h-6 rounded w-full text-center bg-slate-100 font-mono h-6 text-blue-500" v-model="currentPage" type="text"> <span class="p-2 "></span>
          </div>
          <div class="mt-2 grid grid-cols-2 gap-2">
            <button @click="prevPage" class="hover:bg-slate-100 hover:shadow-none border text-blue-500 h-14 rounded h-6 shadow">Previous</button>
            <button @click="nextPage" class="hover:bg-slate-100 hover:shadow-none border text-blue-500 h-14 rounded h-6 shadow">Next</button>
          </div>
        </div>

      </div>

    </div>
  </div>
</template>
