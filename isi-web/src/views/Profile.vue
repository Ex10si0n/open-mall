<script setup lang="ts">
import {computed, ref} from "vue";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import config from "../config";
import axios from "axios";

const store = useStore();
const router = useRouter();

const userName = computed(() => {
  return store.state.userName;
});

const userEmail = computed(() => {
  return store.state.userEmail;
});

const addrId = computed(() => {
  return store.state.primaryAddress.addrId;
});

type AddressState = {
  ADDRID: string;
  TEL: string;
  NAME: string;
  CITY: string;
  COUNTRY: string;
  DETAILED: string;
  ACCID: string;
  TAG: string;
};

const address = ref({} as AddressState);

const hasAddress = ref(false);

const signOut = () => {
  store.commit("signOut");
  router.push("/");
};

const changePassword = () => {
  router.push('/change_password')
}
const query =
    "http://" + config.apiServer + ":" + config.port + "/api/address_by_id/" + addrId.value;
axios.get(query).then((res) => {
  const paddr = res.data.address;
  if (res.data.status === "success") {
    hasAddress.value = true;
  }
  address.value = paddr as AddressState;
});
</script>

<template>
  <div class="flex items-center justify-center min-h-full px-4 py-6 sm:px-6 lg:px-8">
    <div class="w-full max-w-md space-y-8">
      <h2 class="text-2xl font-medium text-left text-gray-900">
        Hello, <span class="font-bold">{{ userName }}</span>
        <div class="text-sm text-gray-500">
          {{ userEmail }}
        </div>
      </h2>
      <div class="overflow-hidden bg-white border rounded-lg shadow-sm">
        <div class="px-6 py-4">
          <div class="flex items-center justify-around">
            <div class="place-items-center text-md">
              <svg
                  style="display: none"
                  t="1644207695805"
                  class="icon alipay-off"
                  viewBox="0 0 1024 1024"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  p-id="2768"
                  width="32"
                  height="32"
              >
                <path
                    d="M621.866667 641.706667c-74.88 89.813333-152.106667 144.64-269.44 144.64s-194.56-72.32-184.746667-159.573334c5.12-57.386667 45.013333-152.106667 217.173333-137.173333 89.813333 7.466667 132.266667 24.96 207.146667 49.92 19.84-36.48 35.84-74.88 47.36-114.773333H309.973333v-32.426667h162.133334v-57.6h-197.12v-37.546667h197.12V212.48c1.92-7.893333 9.386667-13.226667 17.493333-12.586667h82.346667v97.28h209.493333v34.986667h-212.053333v57.386667h172.16c-14.08 61.44-37.76 120.32-69.76 174.72 42.453333 14.933333 214.613333 67.413333 264.533333 82.346666V210.133333A125.418667 125.418667 0 0 0 811.306667 85.333333H210.133333A125.098667 125.098667 0 0 0 85.333333 210.133333v603.946667a125.098667 125.098667 0 0 0 124.8 124.8h603.946667a125.098667 125.098667 0 0 0 124.8-124.8v-30.08c-42.666667-20.053333-232.32-102.4-317.013333-142.293333zM202.666667 619.306667c-7.466667 32.426667 12.373333 109.866667 137.173333 109.866666 74.88 0 149.76-47.36 209.493333-124.8-84.906667-42.453333-154.666667-62.293333-234.453333-62.293333-69.973333 2.346667-104.746667 44.586667-112.213333 77.226667z"
                    p-id="2769"
                    fill="#bfbfbf"
                ></path>
              </svg>
              <svg
                  t="1644207695805"
                  class="icon alipay-on"
                  viewBox="0 0 1024 1024"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  p-id="2768"
                  width="32"
                  height="32"
              >
                <path
                    d="M621.866667 641.706667c-74.88 89.813333-152.106667 144.64-269.44 144.64s-194.56-72.32-184.746667-159.573334c5.12-57.386667 45.013333-152.106667 217.173333-137.173333 89.813333 7.466667 132.266667 24.96 207.146667 49.92 19.84-36.48 35.84-74.88 47.36-114.773333H309.973333v-32.426667h162.133334v-57.6h-197.12v-37.546667h197.12V212.48c1.92-7.893333 9.386667-13.226667 17.493333-12.586667h82.346667v97.28h209.493333v34.986667h-212.053333v57.386667h172.16c-14.08 61.44-37.76 120.32-69.76 174.72 42.453333 14.933333 214.613333 67.413333 264.533333 82.346666V210.133333A125.418667 125.418667 0 0 0 811.306667 85.333333H210.133333A125.098667 125.098667 0 0 0 85.333333 210.133333v603.946667a125.098667 125.098667 0 0 0 124.8 124.8h603.946667a125.098667 125.098667 0 0 0 124.8-124.8v-30.08c-42.666667-20.053333-232.32-102.4-317.013333-142.293333zM202.666667 619.306667c-7.466667 32.426667 12.373333 109.866667 137.173333 109.866666 74.88 0 149.76-47.36 209.493333-124.8-84.906667-42.453333-154.666667-62.293333-234.453333-62.293333-69.973333 2.346667-104.746667 44.586667-112.213333 77.226667z"
                    p-id="2769"
                    fill="#0f57ef"
                ></path>
              </svg>
            </div>
            <div class="text-md">
              <svg
                  style="display: none"
                  t="1644207831698"
                  class="icon wechat-off"
                  viewBox="0 0 1024 1024"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  p-id="5128"
                  width="32"
                  height="32"
              >
                <path
                    d="M395.846 603.585c-3.921 1.98-7.936 2.925-12.81 2.925-10.9 0-19.791-5.85-24.764-14.625l-2.006-3.864-78.106-167.913c-0.956-1.98-0.956-3.865-0.956-5.845 0-7.83 5.928-13.68 13.863-13.68 2.965 0 5.928 0.944 8.893 2.924l91.965 64.43c6.884 3.864 14.82 6.79 23.708 6.79 4.972 0 9.85-0.945 14.822-2.926L861.71 282.479c-77.149-89.804-204.684-148.384-349.135-148.384-235.371 0-427.242 157.158-427.242 351.294 0 105.368 57.361 201.017 147.323 265.447 6.88 4.905 11.852 13.68 11.852 22.45 0 2.925-0.957 5.85-2.006 8.775-6.881 26.318-18.831 69.334-18.831 71.223-0.958 2.92-2.013 6.79-2.013 10.75 0 7.83 5.929 13.68 13.865 13.68 2.963 0 5.928-0.944 7.935-2.925l92.922-53.674c6.885-3.87 14.82-6.794 22.756-6.794 3.916 0 8.889 0.944 12.81 1.98 43.496 12.644 91.012 19.53 139.48 19.53 235.372 0 427.24-157.158 427.24-351.294 0-58.58-17.78-114.143-48.467-163.003l-491.39 280.07-2.963 1.98z"
                    fill="#bfbfbf"
                    p-id="5129"
                ></path>
              </svg>
              <svg
                  t="1644207831698"
                  class="icon wechat-on"
                  viewBox="0 0 1024 1024"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  p-id="5128"
                  width="32"
                  height="32"
              >
                <path
                    d="M395.846 603.585c-3.921 1.98-7.936 2.925-12.81 2.925-10.9 0-19.791-5.85-24.764-14.625l-2.006-3.864-78.106-167.913c-0.956-1.98-0.956-3.865-0.956-5.845 0-7.83 5.928-13.68 13.863-13.68 2.965 0 5.928 0.944 8.893 2.924l91.965 64.43c6.884 3.864 14.82 6.79 23.708 6.79 4.972 0 9.85-0.945 14.822-2.926L861.71 282.479c-77.149-89.804-204.684-148.384-349.135-148.384-235.371 0-427.242 157.158-427.242 351.294 0 105.368 57.361 201.017 147.323 265.447 6.88 4.905 11.852 13.68 11.852 22.45 0 2.925-0.957 5.85-2.006 8.775-6.881 26.318-18.831 69.334-18.831 71.223-0.958 2.92-2.013 6.79-2.013 10.75 0 7.83 5.929 13.68 13.865 13.68 2.963 0 5.928-0.944 7.935-2.925l92.922-53.674c6.885-3.87 14.82-6.794 22.756-6.794 3.916 0 8.889 0.944 12.81 1.98 43.496 12.644 91.012 19.53 139.48 19.53 235.372 0 427.24-157.158 427.24-351.294 0-58.58-17.78-114.143-48.467-163.003l-491.39 280.07-2.963 1.98z"
                    fill="#09BB07"
                    p-id="5129"
                ></path>
              </svg>
            </div>
            <div class="text-md">
              <svg
                  style=""
                  t="1644208162555"
                  class="icon paypal-off"
                  viewBox="0 0 1024 1024"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  p-id="9075"
                  width="32"
                  height="32"
              >
                <path
                    d="M941.142857 369.142857q10.285714 48-2.285714 116.571429-49.714286 253.714286-322.857143 253.714285h-25.142857q-14.285714 0-25.142857 9.428572t-13.714286 24.285714l-2.285714 10.857143-31.428572 197.714286-1.142857 8.571428q-2.857143 14.857143-14 24.285715T477.714286 1024H334.285714q-12 0-18.857143-8.571429t-5.142857-20.571428q5.142857-32 15.142857-96t15.142858-96 15.428571-95.714286 15.428571-95.714286q2.857143-21.142857 24.571429-21.142857h74.857143q76 1.142857 134.857143-12 100-22.285714 164-82.285714 58.285714-54.285714 88.571428-140.571429 13.714286-40 20-76 0.571429-3.428571 1.428572-4.285714t2-0.571428 3.428571 2q45.142857 33.714286 56 92.571428z m-98.285714-161.142857q0 61.142857-26.285714 134.857143-45.714286 133.142857-172.571429 180-64.571429 22.857143-144 24 0 0.571429-51.428571 0.571428l-51.428572-0.571428q-57.142857 0-67.428571 54.857143-1.142857 4.571429-48.571429 302.857143-0.571429 5.714286-6.857143 5.714285H105.714286q-12.571429 0-20.857143-9.428571T78.285714 878.857143L210.857143 38.285714q2.857143-16.571429 15.714286-27.428571T256 0h341.714286q19.428571 0 55.714285 7.428571T717.142857 25.714286q61.142857 23.428571 93.428572 70.285714t32.285714 112z"
                    p-id="9076"
                    fill="#bfbfbf"
                ></path>
              </svg>
              <svg
                  t="1644208048553"
                  style="display: none"
                  class="icon paypal-on"
                  viewBox="0 0 1024 1024"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  p-id="7409"
                  width="30"
                  height="30"
              >
                <path
                    d="M449.28 241.002667H738.133333c155.093333 0 213.461333 78.506667 204.458667 194.005333-14.869333 190.442667-130.005333 295.744-282.730667 295.744h-77.098666c-20.906667 0-35.008 13.824-40.704 51.413333l-33.066667 218.325334c-2.154667 14.165333-9.6 22.506667-20.821333 23.509333h-181.12c-17.045333 0-23.104-13.034667-18.645334-41.28l110.613334-700.288c4.416-28.074667 19.776-41.429333 50.282666-41.429333z"
                    fill="#009DE2"
                    p-id="7410"
                ></path>
                <path
                    d="M268.714667 0H557.866667c81.450667 0 178.026667 2.645333 242.645333 59.626667 43.157333 38.058667 65.792 98.709333 60.586667 163.84C843.306667 444.202667 711.253333 567.893333 534.186667 567.893333h-142.613334c-24.277333 0-40.362667 16.064-47.210666 59.626667l-39.786667 253.141333c-2.56 16.426667-9.706667 26.112-22.698667 27.264H103.765333c-19.754667 0-26.773333-15.104-21.610666-47.850666L210.410667 48.042667C215.530667 15.488 233.344 0 268.714667 0z"
                    fill="#113984"
                    p-id="7411"
                ></path>
                <path
                    d="M348.522667 602.005333l50.496-319.573333c4.416-28.074667 19.776-41.429333 50.282666-41.429333H738.133333c47.808 0 86.442667 7.466667 116.714667 21.226666-29.013333 196.48-156.096 305.664-322.538667 305.664H389.76c-18.773333 0-32.789333 9.6-41.216 34.112z"
                    fill="#172C70"
                    p-id="7412"
                ></path>
              </svg>
            </div>
            <div class="text-md">
              <svg
                  t="1644208113997"
                  class="icon apple-pay"
                  viewBox="0 0 1152 1024"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  p-id="7809"
                  width="32"
                  height="32"
              >
                <path
                    d="M604.4 436.8c0 34.4-21 54.2-58 54.2h-48.6v-108.4h48.8c36.8 0 57.8 19.6 57.8 54.2z m95 125.2c0 16.6 14.4 27.4 37 27.4 28.8 0 50.4-18.2 50.4-43.8v-15.4l-47 3c-26.6 1.8-40.4 11.6-40.4 28.8zM1152 158v704c0 53-43 96-96 96H96c-53 0-96-43-96-96V158c0-53 43-96 96-96h960c53 0 96 43 96 96zM255.6 394.4c16.8 1.4 33.6-8.4 44.2-20.8 10.4-12.8 17.2-30 15.4-47.4-14.8 0.6-33.2 9.8-43.8 22.6-9.6 11-17.8 28.8-15.8 45.6z m121.2 149c-0.4-0.4-39.2-15.2-39.6-60-0.4-37.4 30.6-55.4 32-56.4-17.6-26-44.8-28.8-54.2-29.4-24.4-1.4-45.2 13.8-56.8 13.8-11.8 0-29.4-13.2-48.6-12.8-25 0.4-48.4 14.6-61 37.2-26.2 45.2-6.8 112 18.6 148.8 12.4 18.2 27.4 38.2 47 37.4 18.6-0.8 26-12 48.4-12 22.6 0 29 12 48.6 11.8 20.4-0.4 33-18.2 45.6-36.4 13.8-20.8 19.6-40.8 20-42z m270.8-106.8c0-53.2-37-89.6-89.8-89.6h-102.4v272.8h42.4v-93.2h58.6c53.6 0 91.2-36.8 91.2-90z m180 47.4c0-39.4-31.6-64.8-80-64.8-45 0-78.2 25.8-79.4 61h38.2c3.2-16.8 18.8-27.8 40-27.8 26 0 40.4 12 40.4 34.4v15l-52.8 3.2c-49.2 3-75.8 23.2-75.8 58.2 0 35.4 27.4 58.8 66.8 58.8 26.6 0 51.2-13.4 62.4-34.8h0.8V620h39.2v-136zM1032 421.8h-43l-49.8 161.2h-0.8l-49.8-161.2H844l71.8 198.6-3.8 12c-6.4 20.4-17 28.4-35.8 28.4-3.4 0-9.8-0.4-12.4-0.6v32.8c2.4 0.8 13 1 16.2 1 41.4 0 60.8-15.8 77.8-63.6L1032 421.8z"
                    p-id="7810"
                ></path>
              </svg>
            </div>
          </div>
        </div>
      </div>
      <div class="overflow-hidden bg-white border rounded-lg shadow-sm">
        <router-link to="/address_list">
          <div v-if="hasAddress === true">

            <div class="px-6 py-4">
              <div class="mb-2 text-xl font-medium">Primary address</div>
              <div class="grid grid-cols-3">
                <div class="mb-2 font-bold col-span-1 text-md">{{ address.NAME }}</div>
                <div class="mb-2 text-right col-span-2 text-md">{{ address.TEL }}</div>
              </div>
              <div class="mb-2 col-span-1 text-md bold">
                {{ address.CITY }}, {{ address.COUNTRY }}
              </div>
              <div class="mb-2 col-span-1 text-md bold">
                {{ address.DETAILED }}
              </div>
              <p class="text-base text-gray-700"></p>
            </div>
            <div class="px-6 pt-4 pb-2 grid grid-cols-3">
              <div class="col-span-1">
              <span
                  class="inline-block px-3 py-1 mb-2 mr-2 text-sm font-semibold text-gray-700 bg-gray-200 rounded-full"
              >#{{ address.TAG }}</span
              >
              </div>
            </div>
          </div>
          <div v-else>
            <router-link
                v-if="address == null"
                to="/address_list/create">
              <button
                  type="submit"
                  class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md rounded-t-none shadow-sm text-white bg-teal-700 hover:bg-teal-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-800"
              >
                Add Address
              </button>
            </router-link>
            <router-link v-else to="address_list">
              <button
                  type="submit"
                  class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md rounded-t-none shadow-sm text-white bg-teal-600 hover:bg-teal-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-800"
              >
                Select Primary Address
              </button>
            </router-link>
          </div>
        </router-link>
      </div>
      <div>
        <button
            type="submit"
            class="relative flex justify-center w-full px-6 py-3 font-medium text-white bg-indigo-600 border border-transparent group rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-offset-2"
            @click="changePassword"
        >
          Change Password
        </button>
      </div>
      <div>
        <button
            type="submit"
            class="relative flex justify-center w-full px-6 py-3 font-medium text-white bg-red-500 border border-transparent group rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-offset-2"
            @click="signOut"
        >
          Log Out
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
