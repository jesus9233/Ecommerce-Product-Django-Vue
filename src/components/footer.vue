<template>
	<div class="container-fluid pt-5 bg-lightgrey">
		<div class="container">
			<div class="row">
				<div class="col-md-4 d-flex flex-column social">
					<p class="heading">Social Links</p>
					<a href="https://facebook.com">
						<font-awesome-icon :icon="['fab','facebook-square']"/>
					</a>
					<a href="https://twitter.com">
						<font-awesome-icon :icon="['fab','twitter-square']"/>

					</a>
					<a href="https://instagram.com">
						<font-awesome-icon :icon="['fab','instagram']"/>
					</a>
				</div>
				<div class="col-md-4 d-flex flex-column menu">
					<p class="heading">Menu</p>
					<a href="#"><p>Home</p></a>
					<a href="#"><p>Shop</p></a>
					<a href="#"><p>Contact</p></a>
					<a href="#"><p>Favourites</p></a>
				</div>
				<div class="col-md-4 d-flex flex-column menu">
					<p class="heading">Help</p>
					<a href="#"><p>Shipping Information</p></a>
					<a href="#"><p>Returns & Exchange</p></a>
					<a href="#"><p>Terms & Conditions</p></a>
					<a href="#"><p>Privacy Policy</p></a>
				</div>
			</div>
			<hr>
			<div class="row pb-5 mt-1 text-center">
				<div class="col-12">
					This Website Is Made By <a href="https://www.instagram.com/prrrince3/">Prince</a>
				</div>
			</div>
		</div>

	</div>
</template>

<style scoped>
	.heading{
		font-size: 2rem;
	}
	.social{
		font-size: 2rem;
	}
	a{
		color: black;
		font-weight: 600;
	}
	a:hover{
		text-decoration: none;
	}
	.menu a:first{
		margin-top: 1rem;
	}
</style>
