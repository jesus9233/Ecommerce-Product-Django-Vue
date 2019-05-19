<template>
	<div>
		<app-header>Contact Us</app-header>
		<div class="container-fluid bg-lightgrey">
			<div class="container">
				<div class="row py-5">
					<div class="col-md-6 p-5">
						<h1>Map</h1>
						 ----   Area For Map   -----
					</div>
					<div class="col-md-6 p-5 bg-white">
						<h1>Contact-Form</h1>
						<form method="post">
							<div class="form-group mb-4">
							<input type="text" class="form-control" placeholder="Your Name">
							</div>
							<div class="form-group mb-4">
							<input type="email" class="form-control" placeholder="Your Email">
							</div>
							<div class="form-group mb-4">
							<input type="text" class="form-control" placeholder="Subject">
							</div>
							<div class="form-group mb-4">
							<textarea class="form-control" placeholder="Message"></textarea>
							</div>
							<button @click.prevent class="btn  btn-outline-primary">Send Message</button>
						</form>
					</div>
				</div>
			</div>
		</div>

		<div class="container contact p-5">
			<div class="row">
				<div class="col-4 text-center">
					<font-awesome-icon class="icon" icon="map-marked-alt" />
					<p class="p-2">Dummy Address Here</p>
				</div>
				<div class="col-4 text-center">
					<font-awesome-icon class="icon" icon="mobile" />
					<p class="p-2">987654321</p>
				</div>
				<div class="col-4 text-center">
					<font-awesome-icon class="icon" icon="envelope-open-text" />
					<p class="p-2">Dummy@mail.com</p>
				</div>
			</div>
		</div>

	</div>
</template>
<script>
	import Header from './header/header.vue'
	export default{
		components:{
			appHeader:Header
		}
	}
</script>

<style scoped>
	.contact .icon{
		font-size: 10vw;
	}

</style>
