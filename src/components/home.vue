<template>
<div>
	<div class="header-image">
		<div class="header-text">
			<p class="animated fadeInUp">Best Shoe Store</p>
			<a href="#trending" class="header-btn animated fadeInUp">
				<font-awesome-icon icon="chevron-down" class="icon"/></a>
		</div>
	</div>
	<div class="container-fluid pt-5 ">
		<div class="section-heading " text="trending" id="trending" v-vpshow>
			Trending
		</div>
		<app-list :productsValue="latest"></app-list>
		<div class="section-heading" text="latest products" v-vpshow>
		latest products
		</div>
		<app-list :productsValue="latest"></app-list>
	</div>
	<div class="sale-image">
		<div class="header-text">
			<p>Summer Sale</p>
		</div>
	</div>
	<div class="container-fluid pb-5">
		<div class="section-heading" text="services" v-vpshow>
			Services
		</div>
		<div class="container">
			<div class="row services">
				<div class="col-4 text-center">
					<font-awesome-icon icon='thumbs-up' class="icon"/>
					<p>Refund Policy</p>
				</div>
				<div class="col-4 text-center">
					<font-awesome-icon icon="box-open" class="icon"/>
					<p>Premium Packaging</p>
				</div>
				<div class="col-4 text-center">
					<font-awesome-icon icon="award" class="icon"/>
					<p>Superior Quality</p>
				</div>
		</div>
		</div>
	</div>
</div>
</template>

<script>
import axios from 'axios'

import List from './product/list';
import ProductThumb from './product/productThumb';

export default{
	data(){
		return {
			latest:'',
		}
	},
	components:{
		appList:List,
		appProductThumb:ProductThumb,
	},
	methods:{
		getLatest: function(count) {
			this.$store.state.loading = true;
     axios.get(process.env.API_URL+'/api/product/latest/'+count+'/')
       .then((response) => {
         	this.latest = response.data;
					this.$store.state.loading = false;
         })
       .catch((err) => {
         	console.log(err+" in -> getProducts");
        })
      },
	},
	mounted(){
		this.getLatest(4);
	},
	computed:{
		productsValue(){
			return this.$store.state.products;
		}
	}
}
</script>
<style scoped>

html{
	scroll-behavior: smooth;
}
.header-image,.sale-image{
min-height: 100vh;
background-image: url('https://images.pexels.com/photos/267294/pexels-photo-267294.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940');
background-size: cover;
background-position: center;
background-attachment: fixed;
}
.sale-image{
	position: relative;
	background-image: url('https://images.pexels.com/photos/267320/pexels-photo-267320.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940');
}
.header-text{
	position: absolute;
	top: 50%;
	width: 100%;
	transform: translateY(-50%);
	font-size: 7vw;
	text-align: center;
	font-weight: 700;
	text-transform: uppercase;
	color: white;
}
.header-text p {
	text-shadow: 0 0 10px grey;
}
.header-btn{
	width: 3rem;
	height: 3rem;
	background:#fff;
	color: black;
	font-size: 2rem;
	border-radius: 50%;
	display: inline-block;
	box-shadow:  0 0 10px grey;
}
.header-btn .icon{
	animation: down 1.2s linear infinite;
}
@keyframes down{
	from{
		transform: translateY(0);
		opacity: 1;
	}
	to{
		transform: translateY(1rem);
		opacity: 0;
	}
}
.section-heading{
	padding-top: 2rem;
	font-size: 10vw;
	text-align: center;
	font-weight: 700;
	color: rgba(0, 0, 0, 0.1);
	position: relative;
	text-transform: capitalize;
}

.section-heading:after{
	content: attr(text);
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	color: black;
	font-size: 6vw;
}

.services .icon{
	font-size: 10vw;
}
</style>
