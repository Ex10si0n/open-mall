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
      <div>
        <button
          type="submit"
          class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          My Orders
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
