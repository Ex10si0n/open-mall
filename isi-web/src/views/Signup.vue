<script setup lang="ts">
import {ref} from "vue";
import axios from "axios";
import config from '../config'
import {useRouter} from 'vue-router'
import {useStore} from 'vuex'

const router = useRouter()
const store = useStore()

const email = ref("")
const password = ref("")
const passwordVal = ref("")
const name = ref("")

const createAccount = () => {
  if (passwordVal.value === password.value) {
    // create account
    const query = "http://" + config.apiServer + ":" + config.port + "/api/register/"
    axios.post(query, {
      email: email.value,
      password: password.value
    }).then((res) => {
      if (res.data.status === 'success') {
        console.log(email.value + " created account")
        store.commit('chgUser', {
          accId: res.data.uuid,
          userEmail: email.value,
          userName: name.value,
        })
        store.commit('chgStatus', 'active')
        router.push('/address_list/create')
      } else {
        alert(res.data.status)
      }
    })
  }
}
</script>

<template>
  <div class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <img
            class="mx-auto h-12 w-auto"
            src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg"
            alt="Workflow"
        />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Create a new account
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600"></p>
      </div>
      <div class="mt-8 space-y-6" action="#" method="POST">
        <input type="hidden" name="remember" value="true"/>
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="email-address" class="sr-only">Email address</label>
            <input
                id="email-address"
                name="email"
                type="email"
                autocomplete="email"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-4 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Email address"
                v-model="email"
            />
          </div>
          <div>
            <label for="email-address" class="sr-only">User Name</label>
            <input
                id="user_name"
                name="email"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-4 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="User Name"
                v-model="name"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
                id="password"
                name="password"
                type="password"
                autocomplete="current-password"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-4 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Password"
                v-model="password"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Confirm Password</label>
            <input
                id="password"
                name="password"
                type="password"
                autocomplete="current-password"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-4 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Confirm Password"
                v-model="passwordVal"
            />
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
                id="remember-me"
                name="remember-me"
                type="checkbox"
                class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                checked
            />
            <label for="remember-me" class="ml-2 block text-gray-900">
              I agree with the
            </label>
            <a class="px-1 font-medium text-indigo-600 hover:text-indigo-500"
            >User Policy</a
            >
          </div>

          <div class="text-sm"></div>
        </div>

        <div>
          <button
              class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              @click="createAccount"
          >
            Continue to add address
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
