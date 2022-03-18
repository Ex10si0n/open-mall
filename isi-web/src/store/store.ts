import {createStore} from 'vuex'


// @ts-ignore
// @ts-ignore
export default createStore({
    state: {
        hello: 'Vue-SPA-Quickstart',
        userStatus: 'active', // active vendor visitor
        activeTab: '',
        viewingProduct: '',
        userEmail: 'test@email.com',
        userName: 'Unit Test',
        accId: 'd9f5b7e3-03d2-4630-9788-23ecd9242167',
        currentViewOrderId: '',
        primaryAddress: {
            addrId: '7cd49540-3d41-4eb3-b530-3a40414473d7',
        },
        Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : ""
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
        chgLogin(state, user){
            state.Authorization = user.Authorization;
            localStorage.setItem('Authorization', user.Authorization);
        }
    },
    actions: {}
})
