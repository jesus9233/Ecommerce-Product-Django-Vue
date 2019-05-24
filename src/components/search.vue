<template>
	<div class="pt-6">
		<div class="container">
			<form>
				<div class="form-group mb-3">
					<div class="input-group">
						<input type="text" v-model="searchValue" class="form-control">
						<div class="input-group-append">
							<button type="submit" class="btn btn-info" @click.prevent="search">
								Search
							</button>
						</div>
					</div>
				</div>
			</form>
			<h4>Search Results : {{$route.params.query}}</h4>
		</div>
		<div class="container-fluid py-5 ">
			<app-list :productsValue="productsValue"></app-list>
		</div>
		<app-pagination :url="'/api/product?search='+$route.params.query+'&'"></app-pagination>
	</div>
</template>
<script>
import Header from './header/header';
import List from './product/list';
import Pagination from './product/pagination'


export default{
	data(){
		return {
			searchValue:this.$route.params.query,
		}
	},
	components:{
		appHeader:Header,
		appList:List,
		appPagination:Pagination
	},
	methods:{
			search(){
				if(this.searchValue != ''){
					this.$router.push('/search/'+this.searchValue+'/');
				}
			 },
	},
	computed:{
		productsValue(){
			return this.$store.state.products.results;
		},
	}
}
</script>

<style scoped>
	.pt-6{
		padding-top:6rem;
	}
</style>
