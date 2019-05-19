<template>

  <div>

    <b-navbar toggleable="lg" type="light" id="navbar" :class="{'scrolled':scrolled,'awake':awake,'sleep':sleep}">
      <div class="container">
        <b-navbar-brand :to="{name:'Home'}"><font-awesome-icon icon="shoe-prints" class="mr-2"/>Shoe Store</b-navbar-brand>
        <div class="menu-buttons">
          <b-navbar-toggle target="nav-collapse" class="ml-auto btn btn-outline-dark">
            <font-awesome-icon icon="bars" class="icon"/>
          </b-navbar-toggle>

          <b-button variant="outline-dark ml-1" class="navbar-toggler" @click="searchToggle">
            <font-awesome-icon icon="search" class="icon"/>
          </b-button>

          <router-link class="btn btn-outline-dark navbar-toggler ml-1"
                       type="button"
                       tag="button"
                       :to="{name:'Cart'}"
                       active-class="active"
                       exact>
            <font-awesome-icon icon="shopping-cart" class="mr-1 icon"/>
            <b-badge :class="cartClass()" v-if="$store.state.cartItems">
              {{cartCount}}
            </b-badge>
          </router-link>
        </div>

        <b-collapse id="nav-collapse" is-nav>
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown right>
              <template slot="button-content"><font-awesome-icon icon="store" class="mr-1"/>Shop</template>
              <b-dropdown-item active-class="active" :to="{name:'Shop'}" exact>
                All Categories
              </b-dropdown-item>
              <div class="dropdown-divider"></div>
              <b-dropdown-item v-for="category in categories"
                               active-class="active"
                               :to="{name:'Shop', params:{ category: category }}"
                               :key="category"
                               exact>
                               {{category}}
              </b-dropdown-item>
            </b-nav-item-dropdown>

            <b-nav-item  v-if="isAuth" @click="logOut()">
              <font-awesome-icon icon="sign-in-alt" class="mr-1"/>Sign Out
            </b-nav-item>
            <template  v-else>
              <b-nav-item :to="{name:'Login'}" active-class="active" exact>
                <font-awesome-icon icon="sign-in-alt" class="mr-1"/>Sign In
              </b-nav-item>
              <b-nav-item :to="{name:'Register'}" active-class="active" exact>
                <font-awesome-icon icon="user-plus" class="mr-1"/>Register
              </b-nav-item>
            </template>

            <b-nav-item :to="{name:'Contact'}" active-class="active" exact>
              <font-awesome-icon icon="comment-alt" class="mr-1"/>Contact
            </b-nav-item>
            <li class="nav-item">
              <a class="nav-link d-none d-lg-inline-block" @click="searchToggle">
                  <font-awesome-icon icon="search" class="mr-1"/>Search
                </a>
            </li>
            <li class="nav-item">
              <router-link :to="{name:'Cart'}"
                           class="nav-link d-none d-lg-inline-block"
                           active-class="active"
                           exact>
                <font-awesome-icon icon="shopping-cart" class="mr-1"/>Cart
                <b-badge class="ml-1"
                         :class="cartClass()"
                         v-if="$store.state.cartItems">
                  {{cartCount}}
                </b-badge>
              </router-link>
            </li>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
    <transition enter-active-class="animated slideInDown faster" leave-active-class="animated slideOutUp faster">
      <div class="searchBar" v-if="searchOpen" :class="position" :style="'top:'+navPos+'px;'">
        <b-input-group class="mb-3 w-75 m-auto">
          <b-form-input v-model="query"></b-form-input>
          <b-input-group-append>
            <b-button variant="primary" @click.prevent="search">
              <font-awesome-icon icon="search"/></b-button>
          </b-input-group-append>
        </b-input-group>
      </div>
    </transition>
  </div>

</template>
<script>

  import axios from 'axios'

  export default {
    data() {
      return {
        expand: false,
        scrolled: false,
        awake: false,
        sleep: false,
        searchOpen: false,
        query: '',
        categories: '',
        navPos: 0,
        position: ''
      }
    },
    created() {
      window.addEventListener('scroll', this.handleScroll);
      this.$store.dispatch('isAuthAction');
    },
    mounted() {
      this.getCart();
      this.getCategories();
    },
    computed: {
      cartCount() {
        return this.$store.state.cartItems.cart.products.length
      },
      isAuth(){
        return this.$store.state.isAuth;
      },
    },
    methods: {
      logOut(){
        localStorage.removeItem('TOKEN_KEY');
        this.$store.state.isAuth = false;
      },
      searchToggle() {
        this.searchOpen = !this.searchOpen
        if (this.searchOpen) {
          let elmt = document.getElementById('navbar')
          let pos = elmt.offsetTop
          this.navPos = pos + elmt.offsetHeight
          this.position = 'position-absolute'
          for (var i = 0; i < elmt.classList.length; i++) {
            if (elmt.classList[i] == 'awake') {
              this.position = 'position-fixed'
            }
          }
        }
      },
      getCategories() {
        this.$store.state.loading = true
        axios.get(process.env.API_URL+'/api/product/categories/')
          .then(response => {
            this.categories = response.data
            this.$store.state.loading = false
          })
          .catch(err => {
            console.log(err, ' in get Categories')
          })
      },
      getCart() {
        this.$store.dispatch('getCartAction');
      },
      cartClass() {
        var count = this.cartCount
        return count > 0 ? 'badge-success' : 'badge-danger'
      },
      search(){
        if (this.query != '') {
          this.searchOpen = false
          this.$router.push('/search/' + this.query)
        }
      },
      handleScroll() {
        scroll = window.scrollY
        if (scroll > 200) {
          this.scrolled = true
        } else {
          this.scrolled = false
        }

        if (scroll > 500) {
          this.awake = true
        } else {
          this.awake = false
          if (scroll > 300) {
            this.sleep = true
          } else {
            this.sleep = false
          }
        }
        this.searchOpen = false
      }
    }
  }

</script>
<style scoped>

  nav.navbar {
    position: absolute;
    left: 0;
    right: 0;
    padding: 0;
    z-index: 5;
    background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  }

  .btn:hover .icon {
    color: white;
  }
  nav.scrolled {
    position: fixed !important;
    top: 0rem !important;
    margin-top: -6rem;
  }
  nav.scrolled.awake {
    margin-top: 0rem;
    transition: 0.3s;
  }
  nav.scrolled.sleep {
    transition: 0.3s;
  }
  nav.scrolled.awake .navbar-brand {
    font-size: 1.5rem;
    margin-right:0;
  }
  nav.navbar .navbar-brand {
    font-family: 'Pacifico', cursive;
    font-size: 1.8rem;
    margin-right:0;
    transition: 0.3s;
  }

  .searchBar {
    background-color: #ebeaed;
    padding: 1rem;
    width: 100%;
    z-index: 4;
  }

  .navbar-toggler {
    border: 2px solid;
  }
  .menu-buttons{
    display:flex;
  }
  .navbar-toggler{
    padding:0.3rem 0.5rem;
  }
</style>
