import router from "./router";

router.beforeEach((to, from, next) => {
    if (to.path === '/signup' || to.path === '/login') {
      next();
    } else {
      let token = localStorage.getItem('Authorization');
      if (token === 'null' || token === '') {
        next('/login');
      } else {
        next();
      }
    }
  });
 