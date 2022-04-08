<script setup lang="ts">
import axios from "axios";
import {computed, ref} from "vue";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import config from "../config";
import countries from "../store/countries";

const router = useRouter();
const accId = computed(() => {
  return store.state.accId;
});

const fname = ref("")
const lname = ref("")
const code = ref("")
const tel = ref("")
const country = ref("Select Country or Region")
const city = ref("")
const detailed = ref("")
const tag = ref("")
const store = useStore();

const createAddress = () => {
  if (fname.value === "" || lname.value === "" || code.value === "" || tel.value === "" || country.value === "" || city.value === "" || detailed.value === "" || tag.value === "") {
    alert("Please fill all the fields");
    return
  }
  const query = "http://" + config.apiServer + ":" + config.port + "/api/address/create/"
  axios.post(query, {
    accId: accId.value,
    name: fname.value + " " + lname.value,
    tel: code.value + " " + tel.value,
    country: country.value,
    city: city.value,
    detailed: detailed.value,
    tag: tag.value,
  }).then((res) => {
    const addrId = res.data.addrId
    store.commit('setPrimaryAddress', addrId)
    router.push("/profile")
  })
}

const userName = computed(() => {
  return store.state.userName;
});

const userEmail = computed(() => {
  return store.state.userEmail;
});

const address = computed(() => {
  return store.state.primaryAddress;
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

</script>

<template>
  <div class="min-h-full flex items-center justify-center py-6 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <h2 class="text-left font-medium text-gray-900">
        <router-link to="/address_list">
          <div class="pb-3 text-teal-800">
            <div class="inline text-xl">&lsaquo;&nbsp;</div>
            <div class="inline text-md">Go Back</div>
          </div>
        </router-link>
        <div class="text-2xl">Create New Address</div>
        <div class="text-sm text-gray-500">{{ userEmail }}</div>
      </h2>
      <div class="creation_form">
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
                  v-model="fname"
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
                  v-model="lname"
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
                  v-model="code"
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
                  v-model="tel"
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
              v-model="country"
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
                v-model="city"
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
                v-model="detailed"
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
                v-model="tag"
            />
          </div>
        </div>
        <div
            class="bg-white w-full rounded-lg rounded-t-none overflow-hidden border shadow-lg"
        >
          <div>
            <button
                type="submit"
                class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md rounded-t-none shadow-sm text-white bg-teal-700 hover:bg-teal-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-800"
                @click="createAddress"
            >
              Save
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
