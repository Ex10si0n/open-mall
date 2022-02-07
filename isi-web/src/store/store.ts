import { createStore } from 'vuex'

export default createStore({
  state: {
    hello: 'Vue-SPA-Quickstart',
    userStatus: 'active', // active vendor visitor
    userEmail: 'yzb.ex10si0n@icloud.com',
    userName: 'Ex10si0n',
    primaryAddress: {
      addrId: 'e224b00e-eb86-4203-9090-31de3970a0af',
      name: 'Zhongbo Yan',
      tel: '(853) 6886-0187',
      country: 'China',
      city: 'Macao',
      detailed: 'Rua de Bruxelas, Nam On Gardon, Macao Polytechnic Institute Student Hostel',
      tag: 'home',
    },
    shoppingCart: {}
  },
  mutations: {},
  actions: {}
})