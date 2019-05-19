<template>
  <div id="app">
    <div class="loading" v-if="loading === true ">
      <div class="loading-progress-bar">
        <span class="bar">
          <span class="loading-progress"></span>
        </span>
      </div>
    </div>

    <app-navbar></app-navbar>
    <router-view></router-view>
    <app-footer></app-footer>
    </div>
  </div>
</template>

<script>
import Navbar from './components/header/navbar.vue'
import Footer from './components/footer.vue'
import axios from 'axios'
// <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css"
// integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
// <link href="https://fonts.googleapis.com/css?family=Pacifico|Poppins:500,600,700|Roboto:400,500,700" rel="stylesheet">
// <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css">

export default {
  name: 'App',
  data(){
    return{
    }
  },
  components: {
    appNavbar: Navbar,
    appFooter:Footer,
  },
  computed:{
    loading(){
      return this.$store.state.loading;
    },
  },
}
</script>

<style>
/* @import url('https://fonts.googleapis.com/css?family=Pacifico|Poppins:500,600,700|Roboto:400,500,700'); */

html{
  scroll-behavior: smooth;
}

#app{
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}

body a:focus{
  outline:none;
}

.btn{
  font-weight:500;
}

a{cursor:pointer}

h1,h2,h3,h4,h5,h6{
  font-family:poppins;
}
body a:hover{text-decoration: none;}

.bg-lightgrey{
  background-color: #f8f9fa;
}

/* v-vpshow classes */
.before-enter {
  transform: translateY(50%);
}

.enter {
  transition: transform 1s ease-in-out;
}
.poppins{
  font-family:poppins;
}

/* Loading */

@keyframes loader {

	0% {
		width: 0;
	}

	20% {
		width: 10%;
	}

	25% {
		width: 24%;
	}

	43% {
		width: 41%;
	}

	56% {
		width: 50%;
	}

	66% {
		width: 52%;
	}

	71% {
		width: 60%;
	}

	75% {
		width: 76%;

	}

	100% {
		width: 95%;
	}


}
.loading{
  position:fixed;
  top:0;
  left:0;
  right:0;
  z-index:30;
}
// Bar ============================================
.loading .loading-progress-bar {
	overflow: hidden;
  width: 100%;
}

.loading .bar {
  background: #fff;
  display:block;
}

.loading .loading-progress {
  animation: loader 8s ease forwards;
  background: #0ff;
  color: #fff;
  padding: 2px;
  width: 0;
  display:block;
}

</style>
