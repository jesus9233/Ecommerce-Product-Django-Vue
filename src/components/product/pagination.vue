<template>
		<ul class="pagination justify-content-center">
			<template v-if="obj.previous">
				<li class="page-item"><a class="page-link" @click.prevent="fetchProducts(url+'?page=1')">First</a></li>
				<li class="page-item"><a class="page-link" @click.prevent="fetchProducts(obj.previous)">Previous</a></li>
			</template>
				<template v-for="num in obj.lastPage">
					<li class="page-item active" v-if="obj.current == num"><span class="page-link">{{num}}</span></li>
					<li class="page-item" v-else-if="num > (obj.current-3) && num < (obj.current + 3)">
						<a class="page-link" @click.prevent="fetchProducts(url+'?page='+num)">{{num}}</a>
					</li>
				</template>
			<template v-if="obj.next">
				<li class="page-item"><a class="page-link" @click.prevent="fetchProducts(obj.next)">Next</a></li>
				<li class="page-item"><a class="page-link"
					  @click.prevent="fetchProducts(url+'?page='+obj.lastPage)">Last</a></li>
			</template>
		</ul>
</template>
<script>
  export default {
    data() {
      return {
			}
    },
		props:['url']
		,
		computed:{
			obj(){
				return this.$store.state.products;
			},
		},
		watch:{
			url(){
				this.fetchProducts(this.url);
			},
		},
		methods:{
			fetchProducts(url){
				this.$store.commit('getProducts',url);
			}
		},
		mounted(){
			this.fetchProducts(this.url);
		},
  }
</script>
