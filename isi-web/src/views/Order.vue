<script setup lang="ts">
import {computed, reactive} from "vue";
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
};

const purchases = reactive([] as Array<PurchaseState>);

const accId = computed(() => {
  return store.state.accId;
});

const getOrders = () => {
  axios
      .get("http://" + config.apiServer + ":" + config.port + "/api/order/" + accId.value)
      .then((res) => {
        // console.log(res.data.product_list);
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
</script>

<template>
  <div class="min-h-full flex items-center justify-center py-6 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <h2 class="text-left text-2xl font-medium text-gray-900">
        <span class="font-bold">{{ userName }}'s</span> Orders
        <div class="text-sm text-gray-500">
          {{ userEmail }}
        </div>
      </h2>
      <div>
        <ul role="list" class="-my-6 divide-y divide-gray-200">
          <li v-for="purchase in purchases" class="py-6 flex">
            <!-- <div
              class="flex-shrink-0 w-24 h-24 border border-gray-200 rounded-md overflow-hidden"
            >
              <img
                src="https://tailwindui.com/img/ecommerce-images/shopping-cart-page-04-product-01.jpg"
                alt="Salmon orange fabric pouch with match zipper, gray zipper pull, and adjustable hip belt."
                class="w-full h-full object-center object-cover"
              />
            </div> -->

            <div class="ml-4 flex-1 flex flex-col">
              <div>
                <div class="flex justify-between text-base font-medium text-gray-900">
                  <h3>
                    <a> Created at: {{purchase.date}}</a>
                  </h3>
                  <p class="ml-4 text-right">HK$&nbsp;{{ purchase.amount }}</p>
                </div>
                <p class="mt-1 text-sm text-gray-500">Status: {{ purchase.status }}</p>
              </div>
              <div class="flex-1 flex items-end justify-between text-sm">
                <p class="text-gray-500">ID: {{ purchase.pono.substring(0, 18) }}</p>

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
