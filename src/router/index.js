import Vue from 'vue'
import Router from 'vue-router'

import Cart from '../components/cart'
import Checkout from '../components/checkout'
import Contact from '../components/contact'
import Home from '../components/home'
import Login from '../components/login'
import Register from '../components/register'
import Search from '../components/search'
import Single from '../components/single'
import Shop from '../components/shop'

Vue.use(Router)


export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/search/:query',
      name: 'Search',
      component: Search
    },
    {
      path: '/product/:slug',
      name: 'Detail',
      component: Single
    },
    {
      path: '/contact',
      name: 'Contact',
      component: Contact
    },
    {
      path: '/cart',
      name: 'Cart',
      component: Cart
    },
    {
      path: '/shop/:category?',
      name: 'Shop',
      component: Shop
    },
    {
      path: '/checkout',
      name: 'Checkout',
      component: Checkout
    },
    {
      path:'/login',
      name:'Login',
      component:Login,
      meta:{
        requiresGuest : true,
      }
    },
    {
      path:'/register',
      name:'Register',
      component:Register,
      meta:{
        requiresGuest : true,
      }
    }
  ],
  mode:'history'
})
