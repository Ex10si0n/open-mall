<script setup lang="ts">
import {computed, reactive, ref} from "vue";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import axios from "axios";
import config from "../config";
import InputNumber from "../components/InputNumber.vue";

const store = useStore();
const router = useRouter();

const userEmail = computed(() => {
  return store.state.userEmail;
});


type ProductState = {
  pid: string;
  pname: string;
  brand: string;
  price: number;
  pdesc: string;
  thumbnail: string;
  pic: string;
  quantity: number;
};

const accId = computed(() => {
  return store.state.accId;
});

const subtotal = ref(0);

const products = reactive([] as Array<ProductState>);
/*const query_token =
    "http://" + config.apiServer + ":" + config.port + "/api/current_user";
  axios.get(query_token,{headers:{'Authorization':"Bearer " + localStorage.getItem('Authorization')}}).then((res) => {
    store.commit('chgUser', {
          accId: res.data.uuid,
          userEmail: res.data.email,
          userName: res.data.email.value.split('@')[0]})
      if (res.data.type === 'vendor') {
        store.commit('chgStatus', 'vendor')
      } else {
        store.commit('chgStatus', 'active')
      }
  });*/
const query =
    "http://" + config.apiServer + ":" + config.port + "/api/cart/products/" + accId.value;
axios.get(query).then((res) => {
  const cartItems = res.data.shopping_cart_list;
  cartItems.forEach((cartItem: ProductState) => {
    const pid = cartItem.pid;
    const quantity = cartItem.quantity;
    const innerQuery =
        "http://" + config.apiServer + ":" + config.port + "/api/product/" + pid;
    axios.get(innerQuery).then((res) => {
      const img =
          "http://" +
          config.apiServer +
          ":" +
          config.port +
          "/api/img/" +
          res.data.product.thumbnail;
      const product = {
        pid: cartItem.pid,
        pname: cartItem.pname,
        brand: res.data.product.brand,
        price: cartItem.price,
        pdesc: res.data.product.pdesc,
        thumbnail: img,
        pic: res.data.product.pic,
        quantity: quantity,
      };
      subtotal.value += product.price * product.quantity;
      products.push(product);
    });
  });
});

const sortedProducts = products.sort((a, b) => {
  if (a.pname < b.pname) {
    return -1;
  }
  if (a.pname > b.pname) {
    return 1;
  }
  return 0;
});

const removeProduct = (pid: string) => {
  const query =
      "http://" +
      config.apiServer +
      ":" +
      config.port +
      "/api/cart/del/" +
      pid +
      "/" +
      accId.value;
  axios.get(query);
  location.reload()
};
</script>

<template>
  <!-- This example requires Tailwind CSS v2.0+ -->
  <div class="max-w-screen m-2">
    <div class="grid md:grid-cols-1 lg:grid-cols-3">
      <div class="lg:col-span-2">
        <div class="flex-1 py-6 overflow-y-auto px-4 sm:px-6">
          <div class="flex items-start justify-between">
            <h2 class="text-left text-2xl font-medium text-gray-900">
              Shopping Cart
<!--              <div class="text-sm text-gray-500">-->
<!--              </div>-->
              <div class="text-sm text-gray-500">
<!--                {{ Token }}-->
                {{ userEmail }}
              </div>
            </h2>
            <div class="ml-3 h-7 flex items-center"></div>
          </div>

          <div class="mt-8">
            <div class="flow-root">
              <ul role="list" class="-my-6 divide-y divide-gray-200">
                <li
                    v-if="products.length == 0"
                    class="px-6 py-16 text-lg text-gray-500 text-center"
                >
                  Nothing in Cart
                </li>
                <li v-for="product in sortedProducts" class="py-6 flex">
                  <div
                      class="flex-shrink-0 w-24 h-24 border border-gray-200 rounded-md overflow-hidden"
                  >
                    <img
                        :src="product.thumbnail"
                        class="w-full h-full object-center object-cover"
                    />
                  </div>

                  <div class="ml-4 flex-1 flex flex-col">
                    <div>
                      <div
                          class="flex justify-between text-base font-medium text-gray-900"
                      >
                        <h3>
                          <router-link :to="`/product/${product.pid}`">
                            {{ product.pname }}
                          </router-link>
                        </h3>
                        <p class="ml-4">HK${{ product.price }}</p>
                      </div>
                      <p class="mt-1 text-sm text-gray-500">{{ product.brand }}</p>
                    </div>
                    <div class="flex-1 flex items-end justify-between text-sm">
                      <!-- <p class="text-gray-500">Qty 1</p> -->
                      <!-- <InputNumber :value="product.quantity"></InputNumber> -->
                      <InputNumber
                          :pid="product.pid"
                          :quant="product.quantity"
                      ></InputNumber>

                      <div class="flex">
                        <button
                            type="button"
                            class="font-medium text-indigo-600 hover:text-indigo-500"
                            @click="removeProduct(product.pid)"
                        >
                          Remove
                        </button>
                      </div>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="col-span-1 h-full flex flex-col">
        <div class="py-6 px-4">
          <div class="flex justify-between text-base font-medium text-gray-900">
            <p>Subtotal</p>
            <p>HK${{ subtotal }}</p>
          </div>
          <p class="mt-0.5 text-sm text-gray-500">
            Shipping and taxes calculated at checkout.
          </p>
          <div class="mt-6">
            <router-link to="/order/create">
              <button
                  class="w-full flex justify-center items-center px-6 py-3 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-indigo-600 hover:bg-indigo-700"
              >
                Checkout
              </button>
            </router-link
            >
          </div>
          <div class="mt-6 flex justify-center text-sm text-center text-gray-500"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
