<template>
	<router-link :to="'/product/'+product.slug" active-class="active" class="trend bg-lightgrey" >
		<div class="bg-lightgrey" >
			<div class="o-h d-flex align-items-center h-100">
				<img :src="product.thumb" class="product-image" alt="product image">
			</div>
			<div class="ml-1 p-2">
				<p class="mt-2 mb-0 text-capitalize">{{product.title}}</p>
				<p class="mb-0 p-1 text-success">Rs. {{product.price}}</p>
			</div>
		</div>
	</router-link>
</template>
<script>
	export default{
	props:['product']
	}
</script>
<style scoped>

.row .trend{
	text-decoration: none;
	color: black;
}

.o-h{
	overflow: hidden;
}

.favourites{
	color: #F7444E;
}

img.product-image{
	max-width: 100%;
	transition: .3s;
}
img.product-image:hover{
	-webkit-transform: scale(1.1);
	-ms-transform: scale(1.1);
	transform: scale(1.1);
}
</style>
