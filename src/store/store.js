import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../router';

Vue.use(Vuex);
axios.defaults.baseUrl = process.env.API_URL

export const store = new Vuex.Store({
  state:{
    loading:false,
    products:'',
    productDetail:'',
    cartItems:'',
    isAuth:localStorage.getItem('TOKEN_KEY') ? true : false,
    login:{
      "errors":{},
      "showDismissibleAlert":false,
    }
  },
  getters:{
    headerToken(state){
      let token = localStorage.getItem('TOKEN_KEY') || '';
      return token ? {'Authorization':'Token '+token}  : {};
    },
    checkAuth(state){
      return state.isAuth;
    }
  },
  mutations:{
    getProducts(state, url) {
      state.loading = true;
      var path = process.env.API_URL + url
     axios.get(path)
       .then((response) => {
         state.products = response.data;
         state.loading = false;
         })
       .catch((err) => {
         console.log(err+" in -> getProducts");
        })
      },
    getProductDetail(state,slug) {
      state.loading = true;
     axios.get(process.env.API_URL+'/api/product/detail/'+slug+'/')
       .then((response) => {
         state.productDetail = response.data;
         state.loading = true;
         })
       .catch((err) => {
         console.log(err+" in -> getProductDetail");
        })
      },
      getCartItems(state, headers){
				state.loading = true;
        axios.get(process.env.API_URL+'/api/cart/', {headers})
				.then((response) => {
					state.cartItems = response.data;
          state.loading=false;
				})
				.catch((err) => {
          if(err.response){
					console.log(err.response, ' --> in getCartItems');
        }
        console.log(err);
				})
			},
      login(state, data) {
        state.loading = true;
        axios.post(process.env.API_URL+'/api/user/login/', data)
          .then(res => {
            localStorage.setItem('TOKEN_KEY', res.data.token);
            state.isAuth = true;
            router.push('/');
            state.loading = false;
          })
          .catch(err => {
            if(err.response){
              state.login.errors = err.response.data;
              state.login.showDismissibleAlert = true;
            }
            if(err.response){
              console.log(err.response);
            }
            console.log(err);
            state.loading = false;
          })
      },
      isAuth(state, headers){
        state.loading = true;
        axios.get(process.env.API_URL+'/api/user/is_auth/', {headers})
        .then((res) => {
          if(res.data === true){
            state.isAuth = true;
          }
          else{
            state.isAuth = false;
            localStorage.removeItem('TOKEN_KEY');
          }
          state.loading = false;
        })
        .catch((err) => {
          if(err.response.status >= 400){
            state.isAuth = false;
            localStorage.removeItem('TOKEN_KEY');
          }
          console.log(err,'err in isAuth mutation');
        })
      }
      // getVariantDetails(state, variantIds){
			// 	state.loading = true;
			// 	let variables = '';
			// 	let seprator = ',';
			// 	let count = variantIds.length;
			// 	for (var i = 0; i < count; i++) {
			// 		if(count == i+1){
			// 			seprator = '';
			// 		}
			// 		variables += variantIds[i]+seprator;
			// 	}
			// 	axios.get('/api/variants/details/'+variables+'/')
			// 	.then((response) => {
			// 		state.variants = response.data;
			// 		console.log(this.products, '<-->');
			// 		state.loading = false;
			// 	})
			// 	.catch((err) => {
			// 		console.log(err, '--> in getVariantDetails')
			// 	})
			// }
    },
    actions:{
      cartToggle(store, productId){
          store.state.loading = true;
          let headers = store.getters.headerToken;
          axios.get(process.env.API_URL+'/api/cart/edit/'+productId+'/', {headers})
          .then((response) => {
            store.commit('getCartItems',headers);
            store.state.loading = false;
          })
          .catch((err) => {
            console.log(err, ' ----> cart Toggle');
          })
        },
        getCartAction(store){
          let header = store.getters.headerToken;
          store.commit('getCartItems',header);
        },
        isAuthAction(store){
          let header = store.getters.headerToken;
          store.commit('isAuth', header);
        }
      }
});
