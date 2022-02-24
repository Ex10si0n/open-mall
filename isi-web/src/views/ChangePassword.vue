<script lang="ts" setup>
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
    if (store.state.userStatus != 'visitor'){
        if (checkPassword()){
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
                } else {
                    alert(res.data.status)
                }
            })
        }
    }  
}

const message = ref("At least 6 characters; \nAt least one digit;\nAt least one capital letter")

const checkPassword = () =>{
    let numberFlag = false
    let capitalFlag = false
    if ((newPassword.value.length >= 6) && (/\d/.test(newPassword.value)) && (/A-Z/.test(newPassword.value))){
        return true
    }else{
        alert(message.value)
        return false
    }
}

</script>

<template>
    <div class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-md w-full space-y-8">
            <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Change Password
            </h2>
        </div>
        <div>
        <div class="rounded-md shadow-sm -space-y-px">
            <div>
                <label class="sr-only" for="password">Old Password</label>
                <input
                id="oldPassword"
                v-model="oldPassword"
                class="appearance-none rounded-none relative block w-full px-3 py-4 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                name="oldPassword"
                placeholder="Old Password"
                required
                type="password"
                />
            </div>
            <div>
                <label class="sr-only" for="password">New Password</label>
                <input
                    id="newPassword"
                    v-model="newPassword"
                    class="appearance-none rounded-none relative block w-full px-3 py-4 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                    name="newPassword"
                    placeholder="New Password"
                    required
                    type="password"
                    />
            </div>
                <button
                class="group relative w-full flex justify-center py-3 px-6 border border-transparent font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                type="submit"
                @click="changePassword"
                >
                Change Password
                </button>
        </div>
        </div>
    </div>
</template>