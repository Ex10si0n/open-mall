<script setup lang="ts">
/** Yajing Liu: 
 * It is the frontend about searching products. 
 * It is to find the products according to the inputting keywords */
import axios from "axios";
import {computed, reactive, ref} from "vue";
import config from "../config"
import {useRouter} from 'vue-router'
import {useStore} from 'vuex'


const router = useRouter()
const store = useStore()
// const count = ref(0)

const cnt = ref(2)

const currentPage = ref(1);

const sortPrice = ref("default")

const brandFilter = ref("all")

const content = ref("")

const products_brands = ref([])

const chgViewingProduct = (pid: string) => {
  store.commit("chgViewingProduct", pid);
};

type ProductState = {
  pid: string;
  pname: string;
  brand: string;
  price: number;
  pdesc: string;
  thumbnail: string;
  pic: string;
};

/*const products_brands = computed(() => {
  return products.map((product) => product.brand).filter((brand, index, self) => self.indexOf(brand) === index).sort();
});*/

const result = ref("");

const products = reactive([] as Array<ProductState>);

const getAllProduct = () =>{
  axios
    .get("http://" + config.apiServer + ":" + config.port + "/api/brands")
    .then((res) => {
      if (res.data.status === 'success'){
        // @ts-ignore
        res.data.brand_list.forEach((brand: string) => products_brands.value.push(brand))
      }else{
        alert(res.data.status)
      }
    })
} 

getAllProduct()

const initProduct = () => {
  result.value = ""
  if(products.length > 0){
    while(products.length > 0){
      products.pop()
    }
  }
}

const search = () => {
  var searchResult1 = true
  var searchResult2 = true
  axios
      .get("http://" + config.apiServer + ":" + config.port + "/api/search/name/" + content.value)
      .then((res) => {
        if (res.data.status === 'success') {
          const productList = res.data.products;
          initProduct()
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
            if(product.brand === brandFilter.value || brandFilter.value == "all"){
              products.push(product as ProductState);
            }
          })
          if(products.length == 0){
            result.value = "None"
          }
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

const filtered_products = computed(() => {

  if (brandFilter.value === "all") {
    if (sortPrice.value === "default") {
      return products;
    } else if (sortPrice.value === "l2h") {
      return products.sort((a, b) => a.price - b.price);
    } else if (sortPrice.value === "h2l") {
      return products.sort((a, b) => b.price - a.price);
    }
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
  // @ts-ignore
  if (Math.ceil(filtered_products.value.length / cnt.value) === 0){
    return 1
  }else{
    // @ts-ignore
    return Math.ceil(filtered_products.value.length / cnt.value);
  }
});

const displayed_products = computed(() => {
  // @ts-ignore
  const start = (currentPage.value - 1) * cnt.value;
  // @ts-ignore
  const end = start + cnt.value;
  // @ts-ignore
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
          <select class="col-span-1 bg-white rounded-lg w-full p-2  mb-3 shadow-2xl" v-model="brandFilter" @change="initPage()">
            <option value="all">All Brands</option>
            <option v-for="brand in products_brands" :value="brand">{{ brand }}</option>
          </select>
          <select class="col-span-1 bg-white rounded-lg w-full p-2  mb-3 shadow-2xl" v-model="sortPrice" @change="initPage()">
            <option value="default">Sort default</option>
            <option value="l2h">Price (Low to High)</option>
            <option value="h2l">Price (High to Low)</option>
            <option value="most">Mostly Viewed</option>
            <option value="feat">Featured</option>
          </select>
        </div>
      </div>
      <div><p>{{ result }}</p></div>
      <div class="grid grid-cols-1 gap-3">
        <div
            v-for="product in displayed_products"
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
       <div 
          v-if="maxPage > 1"
          class="w-full">
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