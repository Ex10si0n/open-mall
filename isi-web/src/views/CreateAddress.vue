<script setup lang="ts">
import axios from "axios";
import { computed, h, reactive } from "vue";
import { useStore } from "vuex";
import config from "../config";
import countries from "../store/countries";

const store = useStore();

const userName = computed(() => {
  return store.state.userName;
});

const userEmail = computed(() => {
  return store.state.userEmail;
});

const address = computed(() => {
  return store.state.primaryAddress;
});

const accId = computed(() => {
  return store.state.accId;
});

type AddressState = {
  addrId: string;
  tel: string;
  name: string;
  city: string;
  country: string;
  detailed: string;
  accId: string;
  tag: string;
};

const addr = reactive([] as Array<AddressState>);

const query =
  "http://" + config.apiServer + ":" + config.port + "/api/address/" + accId.value;
axios.get(query).then((res) => {
  const addressList = res.data.address_list;
  addressList.forEach((address: AddressState) => {
    addr.push(address as AddressState);
  });
});

const setPrimaryAddress = (addrId: string) => {
  console.log("setPrimaryAddress to " + addrId);
  store.commit("setPrimaryAddress", addrId);
};
</script>

<template>
  <div class="min-h-full flex items-center justify-center py-6 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <h2 class="text-left font-medium text-gray-900">
        <router-link to="/profile">
          <div class="pb-3 text-teal-800">
            <div class="inline text-xl">&lsaquo;&nbsp;</div>
            <div class="inline text-md">Go Back</div>
          </div>
        </router-link>
        <div class="text-2xl">Create New Address</div>
        <div class="text-sm text-gray-500">{{ userEmail }}</div>
      </h2>
      <form class="creation_form">
        <div class="border rounded-lg rounded-b-none shadow-lg bg-white px-4">
          <div class="grid grid-cols-4 gap-4">
            <div class="mt-4 mb-4 col-span-2">
              <label
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >First Name</label
              >
              <input
                type="text"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder=""
                required
              />
            </div>
            <div class="mt-4 mb-4 col-span-2">
              <label
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >Last Name</label
              >
              <input
                type="text"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder=""
                required
              />
            </div>
          </div>
          <div class="grid grid-cols-6 gap-4">
            <div class="mb-4 col-span-2">
              <label
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >Area Code</label
              >
              <input
                type="text"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="+853"
                required
              />
            </div>
            <div class="mb-4 col-span-4">
              <label
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >Tel.</label
              >
              <input
                type="text"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder=""
                required
              />
            </div>
          </div>
          <label
            for="countries"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-400"
            >Country or Region</label
          >
          <select
            id="countries"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          >
            <option>Select Country or Region</option>
            <option v-for="region in countries.countryListAllIsoData">
              {{ region.code }} - {{ region.name }}
            </option>
          </select>
          <div class="mt-4 mb-4">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
              >City</label
            >
            <input
              type="text"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder=""
              required
            />
          </div>
          <div class="mt-4 mb-4">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
              >Detailed</label
            >
            <textarea
              type="text"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder=""
              required
            />
          </div>
          <div class="mt-4 mb-4">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
              >Tag</label
            >
            <input
              type="text"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Home / Work / School / Family / ..."
              required
            />
          </div>
        </div>
        <div
          class="bg-white max-w-sm rounded-lg rounded-t-none overflow-hidden border shadow-lg"
        >
          <div>
            <button
              type="submit"
              class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md rounded-t-none shadow-sm text-white bg-teal-700 hover:bg-teal-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-800"
            >
              Save
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped></style>
