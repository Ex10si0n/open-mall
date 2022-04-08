<script setup lang="ts">
import axios from "axios";
import {computed, reactive} from "vue";
import {useStore} from "vuex";
import config from "../config";

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

const activeTab = computed(() => {
  return store.state.activeTab;
});

const viewingProduct = computed(() => {
  return store.state.viewingProduct;
});
</script>

<template>
  <div class="min-h-full flex items-center justify-center py-6 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <h2 class="text-left font-medium text-gray-900">
        <router-link v-if="viewingProduct !== ''" :to="'/product/' + viewingProduct">
          <div class="pb-3 text-teal-800">
            <div class="inline text-xl">&lsaquo;&nbsp;</div>
            <div class="inline text-md">Go Back</div>
          </div>
        </router-link>
        <router-link v-else :to="'/' + activeTab">
          <div class="pb-3 text-teal-800">
            <div class="inline text-xl">&lsaquo;&nbsp;</div>
            <div class="inline text-md">Go Back</div>
          </div>
        </router-link>
        <div class="text-2xl">Manage Addresses</div>
        <div class="text-sm text-gray-500">{{ userEmail }}</div>
      </h2>
      <div class="bg-white w-full rounded-lg overflow-hidden border shadow-lg">
        <div v-for="a in addr">
          <hr/>
          <div
              v-if="address.addrId === a.addrId"
              class="px-6 py-4 bg-teal-50 border-2 border-teal-500 rounded-sm"
              @click="setPrimaryAddress(a.addrId)"
          >
            <router-link to="/address/edit"></router-link>
            <div class="font-medium text-xl mb-2">Primary Addresses</div>

            <div class="grid grid-cols-3">
              <div class="col-span-1 text-md font-bold mb-2">{{ a.name }}</div>
              <div class="col-span-2 text-right text-md mb-2">{{ a.tel }}</div>
            </div>
            <div class="col-span-1 text-md bold mb-2">{{ a.city }}, {{ a.country }}</div>
            <div class="col-span-1 text-md bold mb-2">
              {{ a.detailed }}
            </div>
            <p class="text-gray-700 text-base"></p>
            <div class="grid grid-cols-3 pt-4">
              <div class="col-span-1">
                <span
                    class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
                >#{{ a.tag }}</span
                >
              </div>
            </div>
          </div>
          <div v-else @click="setPrimaryAddress(a.addrId)" class="px-6 py-4">
            <!-- <div class="font-medium text-xl mb-2">Alternative Addresses</div> -->
            <div class="grid grid-cols-3">
              <div class="col-span-1 text-md font-bold mb-2">{{ a.name }}</div>
              <div class="col-span-2 text-right text-md mb-2">{{ a.tel }}</div>
            </div>
            <div class="col-span-1 text-md bold mb-2">{{ a.city }}, {{ a.country }}</div>
            <div class="col-span-1 text-md bold mb-2">
              {{ a.detailed }}
            </div>
            <p class="text-gray-700 text-base"></p>
            <div class="grid grid-cols-3 pt-4">
              <div class="col-span-1">
                <span
                    class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
                >#{{ a.tag }}</span
                >
              </div>
            </div>
          </div>
        </div>
        <div>
          <router-link to="/address_list/create">
            <button
                type="submit"
                class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md rounded-t-none shadow-sm text-white bg-teal-700 hover:bg-teal-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-800"
            >
              Add Address
            </button>
          </router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
