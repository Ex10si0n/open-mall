<script setup lang="ts">
// @ts-nocheck
import {computed, ref} from "vue";
import {useStore} from "vuex";
import axios from "axios";
import config from "../config";
// import router from "../router/router";
import {useRouter} from "vue-router";

const store = useStore();
const router = useRouter();

const userType = computed(() => store.state.userStatus);

const activeTab = computed(() => {
  return store.state.activeTab;
});

const addrId = computed(() => {
  return store.state.primaryAddress.addrId;
});

const userEmail = computed(() => {
  return store.state.userEmail;
});

type ProductState = {
  pid: any;
  pname: any;
  price: any;
  thumbnail: any;
  quantity: any;
};

const orderList = ref<ProductState>();

const getOrders = () => {
  const pono = router.currentRoute.value.params.pono
  store.commit('setCurrentViewOrder', pono)
  const query = "http://" + config.apiServer + ":" + config.port + "/api/order/detailed/" + pono;
  axios.get(query).then((res) => {
    orderList.value = res.data.order_list as ProductState
  })
}

const accId = computed(() => {
  return store.state.accId;
});

const subtotal = ref(0);
const info = ref();
const uuid = ref(router.currentRoute.value.params.pono)


const getInfo = () => {
  const pono = router.currentRoute.value.params.pono
  const query = "http://" + config.apiServer + ":" + config.port + "/api/purchase/" + pono;
  axios.get(query).then((res) => {
    info.value = res.data.purchase_info
    console.log(info.value)
  })
}

getOrders()
getInfo()

const cancel = () => {
  const pono = router.currentRoute.value.params.pono
  const query = "http://" + config.apiServer + ":" + config.port + `/api/order/cancel/${userType.value}/${pono}`;
  axios.get(query).then((res) => {
    location.reload()
  })
}

const hold = () => {
  const pono = router.currentRoute.value.params.pono
  const query = "http://" + config.apiServer + ":" + config.port + `/api/order/hold/${pono}`;
  axios.get(query).then((res) => {
    location.reload()
  })
}

const shipOrder = () => {
  const pono = router.currentRoute.value.params.pono
  const query = "http://" + config.apiServer + ":" + config.port + `/api/order/deliver/${pono}`;
  axios.get(query).then((res) => {
    location.reload()
  })
}

const unhold = () => {
  const pono = router.currentRoute.value.params.pono
  const query = "http://" + config.apiServer + ":" + config.port + `/api/order/unhold/${pono}`;
  axios.get(query).then((res) => {
    location.reload()
  })
}

const buildSrc = (thumbnail) => {
  const res = "http://" + config.apiServer + ":" + config.port + "/api/img/" + thumbnail;
  return res;
}

</script>

<template>
  <!-- This example requires Tailwind CSS v2.0+ -->
  <div class="max-w-screen">
    <div class="grid md:grid-cols-1 lg:grid-cols-5">
      <div class="lg:col-span-1"></div>
      <div class="lg:col-span-3">
        <div class="flex-1 py-6 overflow-y-auto px-4 sm:px-6">
          <router-link to="/order">
            <div class="pb-3 text-indigo-800">
              <div class="inline text-xl">&lsaquo;&nbsp;</div>
              <div class="inline text-md">Go Back</div>
            </div>
          </router-link>
          <div class="flex items-start justify-between">
            <h2 class="text-left text-2xl font-medium text-gray-900">
              Checking Order
              <div class="text-sm text-gray-500">
                {{ userEmail }}
              </div>
            </h2>
            <div class="ml-3 h-7 flex items-center"></div>
          </div>
          <div
              v-if="info.STATUS === 'pending'"
              class="text-white bg-blue-500 rounded-lg p-4 mt-8 shadow-sm border-gray-300 border-b-0 rounded-b-none"
          >
            <span class="font-bold">Status: </span>Pending<br>
            <span class="font-bold">Purchase Date: {{ info.DATE }}<br></span>
            <div class="pt-1 font-mono text-xs">PONO: {{ uuid }}</div>
          </div>
          <div
              v-if="info.STATUS === 'cancelled'"
              class="text-white bg-orange-400 rounded-lg p-4 mt-8 shadow-sm border-gray-300 border-b-0 rounded-b-none"
          >
            <span class="font-bold">Status: </span>Cancelled by {{info.CANCELBY}}<br>
            <span class="font-bold">Purchase Date: {{ info.DATE }}<br></span>
            <span class="font-bold">Cancel Date: {{ info.CANCELDATE }}<br></span>
            <div class="pt-1 font-mono text-xs">PONO: {{ uuid }}</div>
          </div>
          <div
              v-if="info.STATUS === 'hold'"
              class="text-white bg-purple-500 rounded-lg p-4 mt-8 shadow-sm border-gray-300 border-b-0 rounded-b-none"
          >
            <span class="font-bold">Status: </span>Held by Vendor<br>
            <span class="font-bold">Purchase Date: {{ info.DATE }}<br></span>
            <div class="pt-1 font-mono text-xs">PONO: {{ uuid }}</div>
          </div>
          <div
              v-if="info.STATUS === 'shipped'"
              class="text-white bg-green-400 rounded-lg p-4 mt-8 shadow-sm border-gray-300 border-b-0 rounded-b-none"
          >
            <span class="font-bold">Status: </span>Shipped<br>
            <span class="font-bold">Purchase Date: {{ info.DATE }}<br></span>
            <span class="font-bold">Ship Date: {{ info.SHIPDATE }}<br></span>
            <div class="pt-1 font-mono text-xs">PONO: {{ uuid }}</div>
          </div>
          <div
              class="bg-white  p-4 shadow-sm border-gray-300 border-b-0 "
          >

            <div class="flow-root">
              <ul role="list" class="-my-6 divide-y divide-gray-200">
                <li v-for="product in orderList" class="py-6 flex">
                  <div
                      class="flex-shrink-0 w-24 h-24 border border-gray-200 rounded-md overflow-hidden"
                  >
                    <img
                        :src="buildSrc(product.thumbnail)"
                        class="w-full h-full object-center object-cover"
                    />
                  </div>

                  <div class="ml-4 flex-1 flex flex-col">
                    <div>
                      <div
                          class="flex justify-between text-base font-medium text-gray-900"
                      >
                        <router-link :to="`/product/${product.pid}`">
                          <h3>
                            {{ product.pname }}
                          </h3></router-link>

                        <p class="ml-4">HK$&nbsp;{{ product.price }}</p>
                      </div>
                    </div>
                    <div class="flex-1 flex items-end justify-between text-sm">
                      Qty: {{ product.quantity }}
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
          <div
              class="bg-white text-black"
          >
            <div class="px-6 py-4">
              <div class="mb-2 text-xl font-medium">Shipping to</div>
              <div class="grid grid-cols-3">
                <div class="mb-2 font-bold col-span-1 text-md"> {{ info.NAME }}</div>
                <div class="mb-2 text-right col-span-2 text-md"> {{ info.TEL }}</div>
              </div>
              <div class="mb-2 col-span-1 text-md bold">
                {{ info.CITY }}, {{ info.COUNTRY }}
              </div>
              <div class="mb-2 col-span-1 text-md bold">
                {{ info.ADDRESS }}
              </div>
              <p v-if="info.STATUS === 'pending' && userType === 'vendor'"
                 class="mb-3 col-span-1 text-base text-green-500 font-bold" @click="shipOrder">Mark as Delivered</p>
              <div class="grid grid-cols-2 ">
                <p v-if="info.STATUS !== 'cancelled' && info.STATUS !== 'shipped'"
                   class="col-span-1 text-base text-red-500" @click="cancel">Cancel Order</p>
                <p v-if="info.STATUS !== 'hold' && info.STATUS !== 'shipped' && info.STATUS !== 'cancelled' && userType === 'vendor'"
                   class="col-span-1 text-right text-base text-blue-700" @click="hold">Hold Order</p>
                <p v-if="info.STATUS === 'hold' && userType === 'vendor'"
                   class="col-span-1 text-right text-base text-blue-700" @click="unhold">Unhold and Deliver order</p>
              </div>
            </div>
          </div>
          <div
              class="p-4 border-t-transparent rounded-lg rounded-t-none shadow-sm border-gray-300 bg-gray-200 text-white"
          >
            <div class="flow-root">
              <div class="col-span-1 flex flex-col">
                <div class="">
                  <div class="flex justify-between text-base font-medium text-gray-900">
                    <p>Subtotal</p>
                    <p>HK$&nbsp;{{ info['AMOUNT'] }}</p>
                  </div>
                  <p class="mt-0.5 text-sm text-gray-600">
                    Shipping and taxes calculated.
                  </p>
                  <div
                      class="flex justify-center text-sm text-center text-gray-500"
                  ></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
