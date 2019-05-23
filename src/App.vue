<template>
  <div id="app" class="bg-lightgrey">
    <div class="loading" v-if="loading === true ">
      <div class="cssload-dots">
      	<div class="cssload-dot"></div>
      	<div class="cssload-dot"></div>
      	<div class="cssload-dot"></div>
      	<div class="cssload-dot"></div>
      	<div class="cssload-dot"></div>
      </div>

      <svg version="1.1" xmlns="http://www.w3.org/2000/svg">
      	<defs>
      		<filter id="goo">
      			<feGaussianBlur in="SourceGraphic" result="blur" stdDeviation="12" ></feGaussianBlur>
      			<feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0	0 1 0 0 0	0 0 1 0 0	0 0 0 18 -7" result="goo" ></feColorMatrix>
      			<!--<feBlend in2="goo" in="SourceGraphic" result="mix" ></feBlend>-->
      		</filter>
      	</defs>
      </svg>
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
@import url('./assets/fonts/fonts.css');

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

.poppins{
  font-family:"poppins";
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

.loading{
  position:fixed;
  top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background-color:rgba(0,0,0,0.2);
  z-index:20;
  transition:0.1s;
}

.cssload-dots {
	width: 0;
	height: 0;
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	margin: auto;
	outline: 1px solid red;
	filter: url(#goo) contrast(200%);
		-o-filter: url(#goo) contrast(200%);
		-ms-filter: url(#goo) contrast(200%);
		-webkit-filter: url(#goo) contrast(200%);
		-moz-filter: url(#goo) contrast(200%);
}

.cssload-dot {
	width: 0;
	height: 0;
	position: absolute;
	left: 0;
	top: 0;
}
.cssload-dot:before {
	content: "";
	width: 31px;
	height: 31px;
	border-radius: 45px;
	background: rgb(251,211,1);
	position: absolute;
	left: 50%;
	transform: translateY(0);
		-o-transform: translateY(0);
		-ms-transform: translateY(0);
		-webkit-transform: translateY(0);
		-moz-transform: translateY(0);
	margin-left: -15.5px;
	margin-top: -15.5px;
}



.cssload-dot:nth-child(5):before {
	z-index: 100;
	width: 40.5px;
	height: 40.5px;
	margin-left: -20.75px;
	margin-top: -20.75px;
	animation: cssload-dot-colors 4.6s ease infinite;
		-o-animation: cssload-dot-colors 4.6s ease infinite;
		-ms-animation: cssload-dot-colors 4.6s ease infinite;
		-webkit-animation: cssload-dot-colors 4.6s ease infinite;
		-moz-animation: cssload-dot-colors 4.6s ease infinite;
}


.cssload-dot:nth-child(1) {
	animation: cssload-dot-rotate-1 4.6s 0s linear infinite;
		-o-animation: cssload-dot-rotate-1 4.6s 0s linear infinite;
		-ms-animation: cssload-dot-rotate-1 4.6s 0s linear infinite;
		-webkit-animation: cssload-dot-rotate-1 4.6s 0s linear infinite;
		-moz-animation: cssload-dot-rotate-1 4.6s 0s linear infinite;
}
.cssload-dot:nth-child(1):before {
	background-color: rgb(255,50,112);
	animation: cssload-dot-move 4.6s 0s ease infinite;
		-o-animation: cssload-dot-move 4.6s 0s ease infinite;
		-ms-animation: cssload-dot-move 4.6s 0s ease infinite;
		-webkit-animation: cssload-dot-move 4.6s 0s ease infinite;
		-moz-animation: cssload-dot-move 4.6s 0s ease infinite;
}

.cssload-dot:nth-child(2) {
	animation: cssload-dot-rotate-2 4.6s 1.15s linear infinite;
		-o-animation: cssload-dot-rotate-2 4.6s 1.15s linear infinite;
		-ms-animation: cssload-dot-rotate-2 4.6s 1.15s linear infinite;
		-webkit-animation: cssload-dot-rotate-2 4.6s 1.15s linear infinite;
		-moz-animation: cssload-dot-rotate-2 4.6s 1.15s linear infinite;
}
.cssload-dot:nth-child(2):before {
	background-color: rgb(32,139,241);
	animation: cssload-dot-move 4.6s 1.15s ease infinite;
		-o-animation: cssload-dot-move 4.6s 1.15s ease infinite;
		-ms-animation: cssload-dot-move 4.6s 1.15s ease infinite;
		-webkit-animation: cssload-dot-move 4.6s 1.15s ease infinite;
		-moz-animation: cssload-dot-move 4.6s 1.15s ease infinite;
}

.cssload-dot:nth-child(3) {
	animation: cssload-dot-rotate-3 4.6s 2.3s linear infinite;
		-o-animation: cssload-dot-rotate-3 4.6s 2.3s linear infinite;
		-ms-animation: cssload-dot-rotate-3 4.6s 2.3s linear infinite;
		-webkit-animation: cssload-dot-rotate-3 4.6s 2.3s linear infinite;
		-moz-animation: cssload-dot-rotate-3 4.6s 2.3s linear infinite;
}
.cssload-dot:nth-child(3):before {
	background-color: rgb(255,145,94);
	animation: cssload-dot-move 4.6s 2.3s ease infinite;
		-o-animation: cssload-dot-move 4.6s 2.3s ease infinite;
		-ms-animation: cssload-dot-move 4.6s 2.3s ease infinite;
		-webkit-animation: cssload-dot-move 4.6s 2.3s ease infinite;
		-moz-animation: cssload-dot-move 4.6s 2.3s ease infinite;
}

.cssload-dot:nth-child(4) {
	animation: cssload-dot-rotate-4 4.6s 3.45s linear infinite;
		-o-animation: cssload-dot-rotate-4 4.6s 3.45s linear infinite;
		-ms-animation: cssload-dot-rotate-4 4.6s 3.45s linear infinite;
		-webkit-animation: cssload-dot-rotate-4 4.6s 3.45s linear infinite;
		-moz-animation: cssload-dot-rotate-4 4.6s 3.45s linear infinite;
}
.cssload-dot:nth-child(4):before {
	background-color: rgb(201,45,6);
	animation: cssload-dot-move 4.6s 3.45s ease infinite;
		-o-animation: cssload-dot-move 4.6s 3.45s ease infinite;
		-ms-animation: cssload-dot-move 4.6s 3.45s ease infinite;
		-webkit-animation: cssload-dot-move 4.6s 3.45s ease infinite;
		-moz-animation: cssload-dot-move 4.6s 3.45s ease infinite;
}

@keyframes cssload-dot-move {
	0% {
		transform: translateY(0);
	}
	18%, 22% {
		transform: translateY(-63px);
	}
	40%, 100% {
		transform: translateY(0);
	}
}

@-o-keyframes cssload-dot-move {
	0% {
		-o-transform: translateY(0);
	}
	18%, 22% {
		-o-transform: translateY(-63px);
	}
	40%, 100% {
		-o-transform: translateY(0);
	}
}

@-ms-keyframes cssload-dot-move {
	0% {
		-ms-transform: translateY(0);
	}
	18%, 22% {
		-ms-transform: translateY(-63px);
	}
	40%, 100% {
		-ms-transform: translateY(0);
	}
}

@-webkit-keyframes cssload-dot-move {
	0% {
		-webkit-transform: translateY(0);
	}
	18%, 22% {
		-webkit-transform: translateY(-63px);
	}
	40%, 100% {
		-webkit-transform: translateY(0);
	}
}

@-moz-keyframes cssload-dot-move {
	0% {
		-moz-transform: translateY(0);
	}
	18%, 22% {
		-moz-transform: translateY(-63px);
	}
	40%, 100% {
		-moz-transform: translateY(0);
	}
}

@keyframes cssload-dot-colors {
	0% {
		background-color: rgb(251,211,1);
	}
	25% {
		background-color: rgb(255,50,112);
	}
	50% {
		background-color: rgba(32,139,241,0.98);
	}
	75% {
		background-color: rgb(98,237,174);
	}
	100% {
		background-color: rgb(242,75,175);
	}
}

@-o-keyframes cssload-dot-colors {
	0% {
		background-color: rgb(251,211,1);
	}
	25% {
		background-color: rgb(255,50,112);
	}
	50% {
		background-color: rgba(32,139,241,0.98);
	}
	75% {
		background-color: rgb(98,237,174);
	}
	100% {
		background-color: rgb(242,75,175);
	}
}

@-ms-keyframes cssload-dot-colors {
	0% {
		background-color: rgb(251,211,1);
	}
	25% {
		background-color: rgb(255,50,112);
	}
	50% {
		background-color: rgba(32,139,241,0.98);
	}
	75% {
		background-color: rgb(98,237,174);
	}
	100% {
		background-color: rgb(242,75,175);
	}
}

@-webkit-keyframes cssload-dot-colors {
	0% {
		background-color: rgb(251,211,1);
	}
	25% {
		background-color: rgb(255,50,112);
	}
	50% {
		background-color: rgba(32,139,241,0.98);
	}
	75% {
		background-color: rgb(98,237,174);
	}
	100% {
		background-color: rgb(242,75,175);
	}
}

@-moz-keyframes cssload-dot-colors {
	0% {
		background-color: rgb(251,211,1);
	}
	25% {
		background-color: rgb(255,50,112);
	}
	50% {
		background-color: rgba(32,139,241,0.98);
	}
	75% {
		background-color: rgb(98,237,174);
	}
	100% {
		background-color: rgb(242,75,175);
	}
}

@keyframes cssload-dot-rotate-1 {
	0% {
		transform: rotate(-105deg);
	}
	100% {
		transform: rotate(270deg);
	}
}

@-o-keyframes cssload-dot-rotate-1 {
	0% {
		-o-transform: rotate(-105deg);
	}
	100% {
		-o-transform: rotate(270deg);
	}
}

@-ms-keyframes cssload-dot-rotate-1 {
	0% {
		-ms-transform: rotate(-105deg);
	}
	100% {
		-ms-transform: rotate(270deg);
	}
}

@-webkit-keyframes cssload-dot-rotate-1 {
	0% {
		-webkit-transform: rotate(-105deg);
	}
	100% {
		-webkit-transform: rotate(270deg);
	}
}

@-moz-keyframes cssload-dot-rotate-1 {
	0% {
		-moz-transform: rotate(-105deg);
	}
	100% {
		-moz-transform: rotate(270deg);
	}
}

@keyframes cssload-dot-rotate-2 {
	0% {
		transform: rotate(165deg);
	}
	100% {
		transform: rotate(540deg);
	}
}

@-o-keyframes cssload-dot-rotate-2 {
	0% {
		-o-transform: rotate(165deg);
	}
	100% {
		-o-transform: rotate(540deg);
	}
}

@-ms-keyframes cssload-dot-rotate-2 {
	0% {
		-ms-transform: rotate(165deg);
	}
	100% {
		-ms-transform: rotate(540deg);
	}
}

@-webkit-keyframes cssload-dot-rotate-2 {
	0% {
		-webkit-transform: rotate(165deg);
	}
	100% {
		-webkit-transform: rotate(540deg);
	}
}

@-moz-keyframes cssload-dot-rotate-2 {
	0% {
		-moz-transform: rotate(165deg);
	}
	100% {
		-moz-transform: rotate(540deg);
	}
}

@keyframes cssload-dot-rotate-3 {
	0% {
		transform: rotate(435deg);
	}
	100% {
		transform: rotate(810deg);
	}
}

@-o-keyframes cssload-dot-rotate-3 {
	0% {
		-o-transform: rotate(435deg);
	}
	100% {
		-o-transform: rotate(810deg);
	}
}

@-ms-keyframes cssload-dot-rotate-3 {
	0% {
		-ms-transform: rotate(435deg);
	}
	100% {
		-ms-transform: rotate(810deg);
	}
}

@-webkit-keyframes cssload-dot-rotate-3 {
	0% {
		-webkit-transform: rotate(435deg);
	}
	100% {
		-webkit-transform: rotate(810deg);
	}
}

@-moz-keyframes cssload-dot-rotate-3 {
	0% {
		-moz-transform: rotate(435deg);
	}
	100% {
		-moz-transform: rotate(810deg);
	}
}

@keyframes cssload-dot-rotate-4 {
	0% {
		transform: rotate(705deg);
	}
	100% {
		transform: rotate(1080deg);
	}
}

@-o-keyframes cssload-dot-rotate-4 {
	0% {
		-o-transform: rotate(705deg);
	}
	100% {
		-o-transform: rotate(1080deg);
	}
}

@-ms-keyframes cssload-dot-rotate-4 {
	0% {
		-ms-transform: rotate(705deg);
	}
	100% {
		-ms-transform: rotate(1080deg);
	}
}

@-webkit-keyframes cssload-dot-rotate-4 {
	0% {
		-webkit-transform: rotate(705deg);
	}
	100% {
		-webkit-transform: rotate(1080deg);
	}
}

@-moz-keyframes cssload-dot-rotate-4 {
	0% {
		-moz-transform: rotate(705deg);
	}
	100% {
		-moz-transform: rotate(1080deg);
	}
}
</style>
