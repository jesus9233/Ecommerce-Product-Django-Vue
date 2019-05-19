<template>
	<div>
		<app-header>collection</app-header>
		<app-list :productsValue="productsValue"></app-list>
		<app-pagination :url="url"></app-pagination>
	</div>
</template>
<script>
import Header from './header/header';
import List from './product/list';
import Pagination from './product/pagination'


export default{
	data(){
		return {
		}
	},
	components:{
		appHeader:Header,
		appList:List,
		appPagination:Pagination
	},
	// methods:{
	// 	fetchProducts(){
	// 		this.$store.commit('getProducts', this.page);
	// 	}
	// },
	// mounted(){
	// 	this.fetchProducts();
	// },
	computed:{
		productsValue(){
			return this.$store.state.products.results;
		},
		url(){
			var url = '/api/product/'
			url += this.$route.params.category ? this.$route.params.category+'/' : '';
			return url
		}
	}
}
</script>

<style scoped>

</style>
