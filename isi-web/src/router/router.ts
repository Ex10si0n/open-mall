import { createRouter, createWebHashHistory, Router } from "vue-router"
import Shop from "../views/Shop.vue";

const webHistory = createWebHashHistory()

export default createRouter({
  history: webHistory,
  routes: [
    { path: "/", component: Shop },
    { path: "/about", component: () => import(/* webpackChunkName: "home" */ "../views/About.vue") },
    { path: "/login", component: () => import(/* webpackChunkName: "home" */ "../views/Login.vue") },
    { path: "/signup", component: () => import(/* webpackChunkName: "home" */ "../views/Signup.vue") },
    { path: "/cart", component: () => import(/* webpackChunkName: "home" */ "../views/Cart.vue") },
    { path: "/profile", component: () => import(/* webpackChunkName: "home" */ "../views/Profile.vue") },
    { path: "/order", component: () => import(/* webpackChunkName: "home" */ "../views/Order.vue") },
    { path: "/address_list", component: () => import(/* webpackChunkName: "home" */ "../views/AddressList.vue") },
    { path: "/product/:pid", component: () => import(/* webpackChunkName: "home" */ "../views/Product.vue") },
  ]
})