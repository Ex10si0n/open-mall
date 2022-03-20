import {createRouter, createWebHashHistory} from "vue-router"
import Shop from "../views/Shop.vue";

const webHistory = createWebHashHistory()

export default createRouter({
    scrollBehavior(to, from, position) {
        return {top: 0}
    },
    history: webHistory,
    routes: [
        {path: "/", component: Shop},
        {path: "/about", component: () => import(/* webpackChunkName: "home" */ "../views/About.vue")},
        {path: "/login", component: () => import(/* webpackChunkName: "home" */ "../views/Login.vue")},
        {path: "/:pid/login", component: () => import(/* webpackChunkName: "home" */ "../views/Login.vue")},
        {path: "/signup", component: () => import(/* webpackChunkName: "home" */ "../views/Signup.vue")},
        {
            path: "/change_password",
            component: () => import(/* webpackChunkName: "home" */ "../views/ChangePassword.vue")
        },
        {path: "/cart", component: () => import(/* webpackChunkName: "home" */ "../views/Cart.vue")},
        {path: "/profile", component: () => import(/* webpackChunkName: "home" */ "../views/Profile.vue")},
        {path: "/order", component: () => import(/* webpackChunkName: "home" */ "../views/Order.vue")},
        {path: "/order/create", component: () => import(/* webpackChunkName: "home" */ "../views/CreateOrder.vue")},
        {path: "/order/:pono", component: () => import(/* webpackChunkName: "home" */ "../views/OrderDetailed.vue")},
        {path: "/address_list", component: () => import(/* webpackChunkName: "home" */ "../views/AddressList.vue")},
        {
            path: "/address_list/create",
            component: () => import(/* webpackChunkName: "home" */ "../views/CreateAddress.vue")
        },
        {path: "/product/:pid", component: () => import(/* webpackChunkName: "home" */ "../views/Product.vue")},
        {path: "/product/create", component: () => import(/* webpackChunkName: "home" */ "../views/CreateProduct.vue")},
        {
            path: "/product/:pid/update",
            component: () => import(/* webpackChunkName: "home" */ "../views/UpdateProduct.vue")
        },
        {path: "/search", component: () => import(/* webpackChunkName: "home" */ "../views/Search.vue")},
        {path: "/manage", component: () => import(/* webpackChunkName: "home" */ "../views/Manage.vue")},
    ]
})