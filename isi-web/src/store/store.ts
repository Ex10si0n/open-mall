import { createStore } from 'vuex'
import axios from 'axios'



// @ts-ignore
// @ts-ignore
export default createStore({
  state: {
    hello: 'Vue-SPA-Quickstart',
    userStatus: 'visitor', // active vendor visitor
    activeTab: '',
    viewingProduct: '',
    userEmail: '',
    userName: '',
    accId: '',
    primaryAddress: {
      addrId: '',
      // addrId: 'e224b00e-eb86-4203-9090-31de3970a0af',
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
      console.log('set Primary Address to', addrId);
    },
    chgActiveTab(state, tab) {
      state.activeTab = tab;
      console.log('[debug] active tab change to ' + tab)
    },
    chgViewingProduct(state, pid) {
      state.viewingProduct = pid;
    },
    chgUser(state, payload) {
      state.accId = payload.accId;
      state.userEmail = payload.userEmail;
      state.userName = payload.userName;
    },
    chgStatus(state, status) {
      state.userStatus = status;
    },
    signOut(state) {
      state.userStatus = 'visitor';
      state.userEmail = '';
      state.userName = '';
      state.accId = '';
      state.primaryAddress.addrId = '';
      state.activeTab = '';
    },
  },
  actions: {
  }
})
