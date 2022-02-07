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
        <span class="font-bold">{{ userName }}'s</span> Orders
        <div class="text-sm text-gray-500">
          {{ userEmail }}
        </div>
      </h2>
      <div>
        <ul role="list" class="-my-6 divide-y divide-gray-200">
          <li class="py-6 flex">
            <div
              class="flex-shrink-0 w-24 h-24 border border-gray-200 rounded-md overflow-hidden"
            >
              <img
                src="https://tailwindui.com/img/ecommerce-images/shopping-cart-page-04-product-01.jpg"
                alt="Salmon orange fabric pouch with match zipper, gray zipper pull, and adjustable hip belt."
                class="w-full h-full object-center object-cover"
              />
            </div>

            <div class="ml-4 flex-1 flex flex-col">
              <div>
                <div class="flex justify-between text-base font-medium text-gray-900">
                  <h3>
                    <a href="#"> Throwback Hip Bag </a>
                  </h3>
                  <p class="ml-4">$90.00</p>
                </div>
                <p class="mt-1 text-sm text-gray-500">
                  Salmon | Qty 1 | Status: Delivered
                </p>
              </div>
              <div class="flex-1 flex items-end justify-between text-sm">
                <p class="text-gray-500">SF21376126328832651</p>

                <div class="flex">
                  <button
                    type="button"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
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
