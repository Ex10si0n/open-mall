<script lang="ts" setup>
import {computed, ref} from "vue";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import config from "../config";
import axios from "axios";

const store = useStore();
const router = useRouter();
const pono = ref('')
const markDeliver = () => {
  const query = "http://" + config.apiServer + ":" + config.port + "/api/order/deliver/" + pono.value
  console.log(query)
  axios.get(query).then(res => {
    if (res.data.status == "success") {
      alert("Success")
      router.push("/manage")
    } else {
      if (res.data.status == "forbidden") {
        alert("Purchase Already Delivered")
      } else {
        alert("Wrong Purchase Number")
      }
    }
  })
}

const userName = computed(() => {
  return store.state.userName;
});

const userEmail = computed(() => {
  return store.state.userEmail;
});

const addrId = computed(() => {
  return store.state.primaryAddress.addrId;
});

</script>

<template>
  <div class="flex items-center justify-center min-h-full px-4 py-6 sm:px-6 lg:px-8">
    <div class="w-full max-w-md space-y-8">
      <h2 class="text-2xl font-medium text-left text-gray-900">
        Vendor Dashboard<br>
        <div class="text-sm text-gray-500">
          {{ userEmail }}
        </div>
      </h2>
      <div class="w-full overflow-hidden bg-white border rounded-lg shadow-sm">
        <div class="px-6 pt-4 pb-2 ">
          <h3 class="font-bold text-xl">Product Management</h3>
          <p class="text-gray-700 text-base">
            Manage your products and their inventory.</p>
          <button @click='$router.push("/product/create")'
                  class="my-3 w-full col-span-1 shadow-lg hover:shadow-none rounded-lg h-10 text-center border-2 bg-cyan-100 text-cyan-500 border-cyan-500 ">
            Create New
          </button>

          <div class="grid grid-cols-2 mt-3 mb-3 gap-4">
            <button @click="$router.push('/')"
                    class="col-span-2 shadow-lg hover:shadow-none rounded-lg h-10 text-center border-2 bg-indigo-100 text-indigo-600 border-indigo-600 ">
              Modify / Delete
            </button>


          </div>
        </div>
      </div>
      <div class="w-full overflow-hidden bg-white border rounded-lg shadow-sm">
        <div class="px-6 pt-4 pb-2 ">
          <h3 class="font-bold text-xl">Delivery Management</h3>
          <p class="text-gray-700 text-base">
            Manage buyer's order delivery.</p>

          <div class="mt-3 mb-3 gap-4">

            <div class="mt-4 mb-4">
              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
              >PONO (Purchase Order no.)</label
              >
              <input
                  type="text"
                  class="font-mono bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="pono"
                  required
                  v-model="pono"
              />
            </div>

            <div class="grid grid-cols-3 gap-4">
              <button @click="$router.push(`/order/${pono}`)"
                      class="col-span-1 w-full shadow-lg hover:shadow-none rounded-lg h-10 text-center border-2 bg-indigo-100 text-indigo-600 border-indigo-600 ">
                Modify
              </button>
              <button @click="markDeliver"
                      class="col-span-2 w-full shadow-lg hover:shadow-none rounded-lg h-10 text-center border-2 bg-green-100 text-green-600 border-green-600 ">
                Mark as Delivered
              </button>
            </div>

          </div>
        </div>
      </div>
      <div class="w-full overflow-hidden bg-white border rounded-lg shadow-sm">
        <div class="px-6 pt-4 pb-2 ">
          <h3 class="font-bold text-xl">User Management</h3>
          <p class="text-gray-700 text-base">
            Manage user and vendor accounts.</p>
          <div class="mt-4 mb-4">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >UID (User Account ID)</label
            >
            <input
                type="text"
                class="font-mono bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="uid"
                required
            />
          </div>

          <div class="grid grid-cols-2 mt-3 mb-3 gap-4">
            <!--            <button @click='$router.push("/manage")' class="col-span-1 shadow-lg hover:shadow-none rounded-lg h-10 text-center border-2 bg-cyan-100 text-cyan-500 border-cyan-500 ">Add</button>-->
            <button
                class="col-span-1 shadow-lg hover:shadow-none rounded-lg h-10 text-center border-2 bg-indigo-100 text-indigo-600 border-indigo-600 ">
              Modify
            </button>
            <button
                class="col-span-1 shadow-lg hover:shadow-none rounded-lg h-10 text-center border-2 bg-pink-100 text-pink-600 border-pink-600 ">
              Delete
            </button>


          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
