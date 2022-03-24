import {createStore} from 'vuex'
import VuexPersist from 'vuex-persist';

// @ts-ignore
// @ts-ignore

const vuexLocalStorage = new VuexPersist({
    key: 'vuex',
    storage: window.localStorage, // or window.sessionStorage or localForage
})

export default createStore({
    state: {
        hello: 'Vue-SPA-Quickstart',
        userStatus: 'visitor', // active vendor visitor
        activeTab: '',
        viewingProduct: '',
        userEmail: '',
        userName: '',
        accId: '',
        currentViewOrderId: '',
        primaryAddress: {
            addrId: '',
        },
    },
    mutations: {
        setPrimaryAddress(state, addrId) {
            state.primaryAddress.addrId = addrId;
            console.log('set Primary Address to', addrId);
        },
        setCurrentViewOrder(state, pono) {
            state.currentViewOrderId = pono;
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
    actions: {},
    plugins: [vuexLocalStorage.plugin]
})
