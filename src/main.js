// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import animated from 'animate.css';
import axios from 'axios'
import { store } from './store/store'
import { fontAwesome } from './addons/font-awesome'
import { vpShow } from './addons/vpshow'

axios.defaults.baseUrl = process.env.API_URL

Vue.use(BootstrapVue)
Vue.use(animated)
Vue.config.productionTip = false



router.beforeEach((to, from, next) => {
  if(to.meta.requiresGuest){
    let auth = localStorage.getItem('TOKEN_KEY') || false;
    if(auth === false){
        next()
      }
    else{
      next('/')
      }
    }
  else{
    next()
  }
});


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: {
    App
  },
  template: '<App/>'
})
