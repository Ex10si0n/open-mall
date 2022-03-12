import {createStore} from 'vuex'


// @ts-ignore
// @ts-ignore
export default createStore({
    state: {
        hello: 'Vue-SPA-Quickstart',
        userStatus: 'active', // active vendor visitor
        activeTab: '',
        viewingProduct: '',
        userEmail: 'unit_test@mockemail.com',
        userName: 'unit_test',
        accId: 'd9f5b7e3-03d2-4630-9788-23ecd9242167',
        currentViewOrderId: '',
        primaryAddress: {
            addrId: '7cd49540-3d41-4eb3-b530-3a40414473d7',
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
    actions: {}
})
