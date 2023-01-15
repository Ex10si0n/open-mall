<script lang="ts" setup>
/** Yajing Liu: 
 * It is the frontend about changing passwords. 
 * The major function of this page of code is to show a view for users to change their passwords and send requests to backend.  */
import axios from "axios";
import {computed, ref} from "vue";
import config from "../config"
import {useRouter} from 'vue-router'
import {useStore} from 'vuex'

const router = useRouter()
const store = useStore()

const email = computed(() => {
  return store.state.userEmail;
});
const oldPassword = ref("")
const newPassword = ref("")

const changePassword = () => {
  if (store.state.userStatus != 'visitor') {
    if (checkPassword()) {
      const query = "http://" + config.apiServer + ":" + config.port + "/api/change_password/"
      axios
          .post(query,
              {
                email: email.value,
                oldPassword: oldPassword.value,
                newPassword: newPassword.value
              }).then((res) => {
        if (res.data.status === 'success') {
          alert(res.data.status)
          router.push('/profile')
        } else {
          alert(res.data.status)
        }
      })
    }
  }
}


const checkPassword = () => {
  let numberFlag = false
  let capitalFlag = false
  if (newPassword.value.length >= 6) {
    for (var char of newPassword.value) {
      for (var digit of ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) {
        if (char == digit) {
          numberFlag = true
          break
        }
      }
      for (var letter of ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) {
        if (char == letter) {
          capitalFlag = true
          break
        }
      }
    }
    if (numberFlag == true && capitalFlag == true) {
      return true
    } else if (numberFlag == false && capitalFlag == false) {
      alert("At least one digit\nAt least one capital letter")
      return false
    } else if (numberFlag == false && capitalFlag == true) {
      alert("At least one digit")
      return false
    } else {
      alert("At least one capital letter")
      return false
    }
  } else {
    alert("At least 6 characters")
    return false
  }
}

</script>

<template>
  <div class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <img
            alt="Workflow"
            class="mx-auto h-12 w-auto"
            src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg"
        />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Change Password
        </h2>
      </div>

      <div class="rounded-md shadow-sm -space-y-px">
        <div>
          <label class="sr-only" for="email-address">Email address</label>
          <input
              id="oldPassword"
              v-model="oldPassword"
              autocomplete="email"
              class="appearance-none rounded-none relative block w-full px-3 py-4 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              name="email"
              placeholder="Old Password"
              required
              type="password"
          />
        </div>
        <div>
          <label class="sr-only" for="password">Password</label>
          <input
              id="newPassword"
              v-model="newPassword"
              class="appearance-none rounded-none relative block w-full px-3 py-4 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              name="password"
              placeholder="New Password"
              required
              type="password"
          />
        </div>
      </div>

      <div class="flex items-center justify-between">
        <div class="flex items-center">
        </div>

        <div class="text-sm">
          <a class="font-medium text-indigo-600 hover:text-indigo-500" href="#">
            Forgot your password?
          </a>
        </div>

      </div>

      <div>
        <button
            class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            type="submit"
            @click="changePassword"
        >
          Submit Change
        </button>
      </div>
    </div>
  </div>
  <div class="min-h-full flex items-center justify-center">
    <div class="rounded-md shadow-sm">
    </div>
  </div>
</template>