<template>
	<div class="pt-5">
		<div class="header-image">
			<div v-vpshow>
				<p class="page-name"><slot></slot></p >
				<router-link :to="{name:'Home'}" class="bread-crumb">Home</router-link><span class="ml-3">{{$route.name}}</span>
			</div>
		</div>
	</div>
</template>

<style scoped>
	.pt-6{
		padding-top: 4rem;
	}

	.header-image{
		min-height: 50vh;
		background-image: url('https://images.pexels.com/photos/1598505/pexels-photo-1598505.jpeg?cs=srgb&dl=air-jordan-design-footwear-1598505.jpg&fm=jpg');
		background-size: cover;
		background-position: center;
		background-attachment: fixed;
		padding: 6rem 0;
		text-align: center;
		color: white;
		font-family: poppins;
		text-transform: capitalize;
		text-shadow: 0 0 10px grey;
	}

	.page-name{
		font-size: 3rem;
	}

	.bread-crumb{
		color: white;
		font-size: 1.2rem;
	}

	.header-image span{
		color: rgba(255, 255, 255, 0.8);
	}
</style>
