<script setup lang="ts">
import {computed, reactive, ref} from "vue";
import {useStore} from "vuex";
import axios from "axios";
import config from "../config";
import {useRouter} from "vue-router";

const store = useStore();
const router = useRouter();

const markDeliver = (pono: string) => {
  const query = "http://" + config.apiServer + ":" + config.port + "/api/order/deliver/" + pono
  axios.get(query).then(res => {
    if (res.data.status == "success") {
      alert("Success")
      location.reload()
    } else {
      if (res.data.status == "forbidden") {
        alert("Purchase Already Delivered")
      } else {
        alert("Wrong Purchase Number")
      }
    }
  })
}


type ProductState = {
  pid: string;
  pname: string;
  brand: string;
  price: number;
  pdesc: string;
  thumbnail: string;
  pic: string;
};

type AliasState = {
  pname: string;
  price: number;
  quantity: number;
  subtotal: number;
}

type PurchaseState = {
  amount: number;
  date: Date;
  pono: string;
  status: string;
  name: string;
  tel: string;
};

const purchases = reactive([] as Array<PurchaseState>);


const accId = computed(() => {
  return store.state.accId;
});

const userType = computed(() => {
  return store.state.userStatus;
});

const getOrders = () => {
  let query;
  if (userType.value === 'active') {
    query = "http://" + config.apiServer + ":" + config.port + "/api/order/" + accId.value;
  } else if (userType.value === 'vendor') {
    query = "http://" + config.apiServer + ":" + config.port + "/api/order/all";
  } else {
    query = ""
  }
  axios
      .get(query)
      .then((res) => {
        const productList = res.data.purchase_list;
        console.log(productList);
        productList.forEach((product: PurchaseState) => {
          purchases.push(product as PurchaseState);
        });
      })
      .catch((error) => console.log(error));
};

const userName = computed(() => {
  return store.state.userName;
});

const userEmail = computed(() => {
  return store.state.userEmail;
});

const aliases = reactive([] as Array<AliasState>);

const getOrdersByPono = (pono: string) => {
  const query = "http://" + config.apiServer + ":" + config.port + "/api/order/pono/" + pono
  let alias = ""
  axios.get(query).then((res) => {
    let i = 0;
    res.data.order_list.forEach((p: AliasState) => {
      if (i === 0) aliases.push(p)
      i += 1;
    })
  })
  return ''
}

getOrders();

const selectName = ref('')
const selectStatus = ref('All Status')

const selectUser = () => {
  console.log(selectName.value)
}
</script>

<template>
  <div class="min-h-full flex items-center justify-center py-6 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <h2 class="text-left text-2xl font-medium text-gray-900">
        <div v-if="userType === 'active'">
          <span class="font-bold">{{ userName }}'s</span> Orders
        </div>
        <div v-if="userType === 'vendor'">
          <span class="font-bold">Order Management</span>
        </div>
        <div class="text-sm text-gray-500">
          {{ userEmail }}
        </div>
      </h2>
      <div>
        <div class="bg-white rounded-lg my-6 px-5 shadow-xl border py-2">
          <div v-if="userType === 'vendor'" class="my-3">
            <input type="text" @blur="selectUser" v-model="selectName" placeholder="Name"
                   class="text-sm p-3 w-full h-10 border rounded-lg bg-slate-50">
          </div>
          <div class="my-3">
            <select
                v-model="selectStatus"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            >
              <option>All Status</option>
              <option v-if="userType === 'vendor'" value="pending">Pending</option>
              <option value="past">Past Orders</option>
<!--              <option value="shipped">Shipped</option>-->
<!--              <option value="cancelled">Cancelled</option>-->
              <option v-if="userType === 'vendor'" value="hold">On Hold</option>
              <option v-if="userType === 'active'" value="current">Current</option>
            </select>

          </div>
        </div>
        <ul role="list" class="-my-6 divide-y divide-gray-200">
          <li v-for="purchase in purchases" class="">
            <!-- <div
              class="flex-shrink-0 w-24 h-24 border border-gray-200 rounded-md overflow-hidden"
            >
              <img
                src="https://tailwindui.com/img/ecommerce-images/shopping-cart-page-04-product-01.jpg"
                alt="Salmon orange fabric pouch with match zipper, gray zipper pull, and adjustable hip belt."
                class="w-full h-full object-center object-cover"
              />
            </div> -->

            <div
                v-if="(selectName === '' || selectName === purchase.name) && (selectStatus === 'All Status' || selectStatus === purchase.status || selectStatus === 'past' && (purchase.status === 'cancelled' || purchase.status === 'shipped') || selectStatus === 'current' && (purchase.status === 'pending' || purchase.status === 'hold'))"
                class="py-6 ml-4 flex-1 flex flex-col">
              <div>
                <h3 class="text-orange-600 text-md" v-if="userType === 'vendor'">
                  <div class="font-bold">{{ purchase.name }}</div>
                  <div>{{ purchase.tel }}</div>
                </h3>
                <div class="flex justify-between text-base font-medium text-gray-900">
                  <h3>
                    <a> Created at: {{ purchase.date }}</a>
                  </h3>
                  <p class="ml-4 text-right">HK$&nbsp;{{ purchase.amount }}</p>
                </div>
                <p class="mt-1 text-sm text-gray-500">Status: {{ purchase.status }}</p>
              </div>
              <div class="flex-1 flex items-end justify-between text-sm">
                <p class="text-gray-500">ID: {{ purchase.pono.substring(0, 18) }}</p>
                <button class="text-md" v-if="userType === 'vendor' && purchase.status === 'pending'">
                  <div @click="markDeliver(purchase.pono)" class="font-bold text-green-500">Mark Delivered</div>
                </button>

                <div class="flex">
                  <button
                      type="button"
                      class="font-medium text-indigo-600 hover:text-indigo-500"
                      @click="$router.push('/order/' + purchase.pono)"
                  >
                    Detailed
                  </button>
                </div>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
