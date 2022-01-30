<script setup lang="ts">
import { ref } from "vue";

// const count = ref(0)
</script>

<template>
  <!-- This example requires Tailwind CSS v2.0+ -->
  <div class="max-w-screen">
    <div class="grid md:grid-cols-1 lg:grid-cols-3">
      <div class="lg:col-span-2">
        <div class="flex-1 py-6 overflow-y-auto px-4 sm:px-6">
          <div class="flex items-start justify-between">
            <h2 class="text-2xl font-medium text-gray-900" id="slide-over-title">
              Shopping cart
            </h2>
            <div class="ml-3 h-7 flex items-center"></div>
          </div>

          <div class="mt-8">
            <div class="flow-root">
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
                      <div
                        class="flex justify-between text-base font-medium text-gray-900"
                      >
                        <h3>
                          <a href="#"> Throwback Hip Bag </a>
                        </h3>
                        <p class="ml-4">$90.00</p>
                      </div>
                      <p class="mt-1 text-sm text-gray-500">Salmon</p>
                    </div>
                    <div class="flex-1 flex items-end justify-between text-sm">
                      <p class="text-gray-500">Qty 1</p>

                      <div class="flex">
                        <button
                          type="button"
                          class="font-medium text-indigo-600 hover:text-indigo-500"
                        >
                          Remove
                        </button>
                      </div>
                    </div>
                  </div>
                </li>

                <li class="py-6 flex">
                  <div
                    class="flex-shrink-0 w-24 h-24 border border-gray-200 rounded-md overflow-hidden"
                  >
                    <img
                      src="https://tailwindui.com/img/ecommerce-images/shopping-cart-page-04-product-02.jpg"
                      alt="Front of satchel with blue canvas body, black straps and handle, drawstring top, and front zipper pouch."
                      class="w-full h-full object-center object-cover"
                    />
                  </div>

                  <div class="ml-4 flex-1 flex flex-col">
                    <div>
                      <div
                        class="flex justify-between text-base font-medium text-gray-900"
                      >
                        <h3>
                          <a href="#"> Medium Stuff Satchel </a>
                        </h3>
                        <p class="ml-4">$32.00</p>
                      </div>
                      <p class="mt-1 text-sm text-gray-500">Blue</p>
                    </div>
                    <div class="flex-1 flex items-end justify-between text-sm">
                      <p class="text-gray-500">Qty 1</p>

                      <div class="flex">
                        <button
                          type="button"
                          class="font-medium text-indigo-600 hover:text-indigo-500"
                        >
                          Remove
                        </button>
                      </div>
                    </div>
                  </div>
                </li>

                <!-- More products... -->
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="col-span-1 h-full flex flex-col">
        <div class="py-6 px-4 sm:px-6">
          <div class="flex justify-between text-base font-medium text-gray-900">
            <p>Subtotal</p>
            <p>$262.00</p>
          </div>
          <p class="mt-0.5 text-sm text-gray-500">
            Shipping and taxes calculated at checkout.
          </p>
          <div class="mt-6">
            <button
              href="#"
              class="w-full flex justify-center items-center px-6 py-3 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-indigo-600 hover:bg-indigo-700"
            >
              Checkout
            </button>
          </div>
          <div class="mt-6 flex justify-center text-sm text-center text-gray-500"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
