// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'
import { store } from './store/store'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faShoePrints, faBars, faSearch, faShoppingCart, faStore, faSignInAlt,
         faUserPlus, faCommentAlt, faChevronDown, faBoxOpen, faAward, faThumbsUp,
         faTrashAlt, faMapMarkedAlt, faMobile, faEnvelopeOpenText, faAt, faLock,
         faLockOpen, faEye, faUser
       } from '@fortawesome/free-solid-svg-icons'
import { faFacebookSquare, faTwitterSquare, faInstagram } from '@fortawesome/free-brands-svg-icons'
// import { faThumbsUp as farThumbsUp } from '@fortawesome/pro-regular-svg-icons/faThumbsUp'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faShoePrints, faBars, faSearch, faShoppingCart, faSignInAlt, faUserPlus,
            faCommentAlt, faStore, faChevronDown, faThumbsUp, faBoxOpen, faAward,
            faTrashAlt, faMapMarkedAlt, faMobile, faEnvelopeOpenText, faFacebookSquare,
            faTwitterSquare, faInstagram, faAt, faLock, faLockOpen, faEye, faUser)

Vue.component('font-awesome-icon', FontAwesomeIcon)

axios.defaults.baseUrl = process.env.API_URL

Vue.use(BootstrapVue)

Vue.config.productionTip = false

Vue.directive('vpshow', {
  inViewport (el) {
    var rect = el.getBoundingClientRect()
    return !(rect.bottom < 0 || rect.right < 0 ||
             rect.left > window.innerWidth ||
             rect.top > window.innerHeight)
  },

  bind(el, binding) {
    el.classList.add('before-enter')
    el.$onScroll = function() {
      if (binding.def.inViewport(el)) {
        el.classList.add('enter')
        el.classList.remove('before-enter')
        binding.def.unbind(el, binding)
      }
    }
    document.addEventListener('scroll', el.$onScroll)
  },

  inserted(el, binding) {
    el.$onScroll()
  },

  unbind(el, binding) {
    document.removeEventListener('scroll', el.$onScroll)
    delete el.$onScroll
  }
})


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
