import { createStore } from 'vuex'
import axios from 'axios'



export default createStore({
  state: {
    hello: 'Vue-SPA-Quickstart',
    userStatus: 'visitor', // active vendor visitor
    activeTab: '',
    viewingProduct: '',
    userEmail: 'yzb.ex10si0n@icloud.com',
    userName: 'Ex10si0n',
    accId: 'c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa',
    primaryAddress: {
      addrId: 'e224b00e-eb86-4203-9090-31de3970a0af',
      // name: 'Zhongbo Yan',
      // tel: '(853) 6886-0187',
      // country: 'China',
      // city: 'Macao',
      // detailed: 'Rua de Bruxelas, Nam On Gardon, Macao Polytechnic Institute Student Hostel',
      // tag: 'home',
    },
  },
  mutations: {
    setPrimaryAddress(state, addrId) {
      state.primaryAddress.addrId = addrId;
    },
    chgActiveTab(state, tab) {
      state.activeTab = tab;
      console.log('[debug] active tab change to ' + tab)
    },
    chgViewingProduct(state, pid) {
      state.viewingProduct = pid;
    }
  },
  actions: {
  }
})
