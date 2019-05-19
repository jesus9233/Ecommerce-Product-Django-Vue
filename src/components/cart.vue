<template>
	<div>
		<app-header>my cart</app-header>
		<div class="container-fluid pt-5 cart">
			<div class="container pt-5" >
				<div class="row cart-items">
					<table class="text-center table">
						<thead class="bg-lightgrey">
							<tr>
								<th>Image</th>

								<th>Product</th>

								<th>Price</th>

								<th>Size</th>

								<th>Remove</th>
							</tr>
						</thead>
						<tbody>
							<tr v-for="product in products" >
								<td><img :src="product.thumb" alt="product thumb"></td>
								<td>{{product.name}}</td>
								<td>{{product.price}}</td>
								<td>{{product.size}}</td>
								<td>
									<a class="btn btn-danger text-white" @click.prevent="cartToggle(product.id)">
										<font-awesome-icon icon="trash-alt" />
									</a>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
				<div class="row py-5 justify-content-end total-cart">
					<div class="col-lg-6">
						<div class="border p-3" v-if="cart">
							<h3 class="poppins p-1">Cart Totals</h3>
							<p class="d-flex p-2">
								<span>Items Count</span>
								<span>{{cart.products.length}}</span>
							</p>
							<p class="d-flex p-2">
								<span>Subtotal</span>
								<span>Rs {{cart.subtotal}}</span>
							</p>
							<p class="d-flex p-2 total border-top">
								<span>Total</span>
								<span>Rs {{cart.total}}</span>
							</p>
						</div>
						<div class="text-right">
							<router-link class="btn btn-lg btn-outline-success m-2" type="button" :to="{name:'Checkout'}" exact>
								Checkout
							</router-link>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	import Header from './header/header.vue';

	export default{
		data(){
			return{
			}
		},
		components:{
			appHeader:Header
		},
		computed:{
			products(){
				return this.$store.state.cartItems.variants;
			},
			cart(){
				return this.$store.state.cartItems.cart;
			}
		},
		methods:{
			cartToggle(productId){
				this.$store.dispatch('cartToggle', productId);
			},
		}
	}
</script>
<style scoped>
	.head{
		font-size: 1.2rem;
		padding: 1rem;
	}
	.cart img{
		max-height: 150px;
	}
	.cart input.form-control{
		max-width: 100px;
		min-width: 70px;
	}
	.cart div{
		align-items: center;
	}
	table{
		width: 100%;
		white-space: nowrap;
	}
	table.table td, .table th{
		vertical-align: middle;
	}
	table.table tbody tr:first-of-type td{
		border-top: 0;
	}
	.poppins{
		font-family: poppins;
	}
	.total-cart span{
		display: block;
		width: 50%;
	}
	.total{
		font-size: 1.2rem;
	}
	.cart-items{
		overflow-x: auto;
	}
</style>
