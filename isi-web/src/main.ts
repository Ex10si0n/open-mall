import { createApp } from 'vue'
import App from './App.vue'
import store from './store/store'
import router from './router/router'
import naive from 'naive-ui'
import './css/index.css'

const app = createApp(App)
app.use(router)
app.use(store)
app.use(naive)
app.mount('#app')