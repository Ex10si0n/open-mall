import router from "./router";
import {getToken} from "../storage"

router.beforeEach((to, from, next) => {
    if (to.path === 'signup' || to.path === 'login') {
      next();
    } else {
      let token = getToken();
      if (token === 'null' || token === '') {
        next('/login');
      } else {
        next();
      }
    }
  });
 