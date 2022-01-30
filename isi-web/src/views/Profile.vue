<script setup lang="ts">
import { computed } from "vue";
import { useStore } from "vuex";

const store = useStore();

const userName = computed(() => {
  return store.state.userName;
});

const userEmail = computed(() => {
  return store.state.userEmail;
});
</script>

<template>
  <div class="min-h-full flex items-center justify-center py-6 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <h2 class="text-left text-2xl font-medium text-gray-900">
        Hello, <span class="font-bold">{{ userName }}</span>
        <div class="text-sm text-gray-500">
          {{ userEmail }}
        </div>
      </h2>
      <div class="max-w-sm rounded-lg overflow-hidden border shadow-lg">
        <div class="px-6 py-4">
          <div class="font-medium text-xl mb-2">Primary Address</div>
          <div class="grid grid-cols-3">
            <div class="col-span-1 text-md font-bold mb-2">Zhongbo Yan</div>
            <div class="col-span-2 text-right text-md mb-2">(853) 6886-0187</div>
          </div>
          <div class="col-span-1 text-md bold mb-2">Macao SAR, China</div>
          <div class="col-span-1 text-md bold mb-2">
            Rua de Bruxelas, Nam On Gardon, Macao Polytechnic Institute Student Hostel
          </div>
          <p class="text-gray-700 text-base"></p>
        </div>
        <div class="grid grid-cols-3 px-6 pt-4 pb-2">
          <div class="col-span-1">
            <span
              class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
              >#Home</span
            >
          </div>
        </div>
      </div>
      <div>
        <button
          type="submit"
          class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Change Password
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
