import {createApp} from 'vue'
import App from './App.vue'
import store from './store/store'
import router from './router/router'
import naive from 'naive-ui'
import './css/index.css'
import axios from "axios";

const app = createApp(App)
app.use(router)
app.use(store)
app.use(naive)
app.mount('#app')

axios.interceptors.request.use(
    config => {
      if (config.headers === undefined) {
        config.headers = {};
      }
      if (localStorage.getItem('Authorization')) {
        config.headers.Authorization = localStorage.getItem('Authorization');
      }
 
      return config;
    },
    error => {
      return Promise.reject(error);
    });