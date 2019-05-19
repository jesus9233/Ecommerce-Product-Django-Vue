<template>
	<div>
		<app-header>Checkout</app-header>
		<div class="container-fluid pt-5">
			<div class="container pt-5">
				<div class="row justify-content-center">
					<div class="col-lg-8 billing">
							<form method="post" class="bg-lightgrey p-5 mb-5">
								<h3 class="poppins">Billing Details</h3>
								<div class="row">
									<div class="col-md-6">
										<div class="form-group">
											<label for="fName">First Name</label>
											<input type="text" class="form-control" id="fName"name="">
										</div>
									</div>
									<div class="col-md-6">
										<div class="form-group">
											<label for="lName">Last Name</label>
											<input type="text" class="form-control" id="lName"name="">
										</div>
									</div>
									<div class="w-100"></div> <!-- divider -->
									<div class="col-md-12">
										<div class="form-group">
												<label for="country">Select Country</label>
												<select name="" class="custom-select">
													<option value="">Select Country</option>}
													<option value="Australia">Australia</option>
													<option value="India">India</option>
													<option value="Korea">Korea</option>
												</select>
										</div>
									</div>
									<div class="w-100"></div> <!-- divider -->
									<div class="col-md-6">
										<div class="form-group">
											<label for="city">City/Town</label>
											<input type="text" class="form-control" id="city"name="">
										</div>
									</div>
									<div class="col-md-6">
										<div class="form-group">
											<label for="zip">Zip Code</label>
											<input type="text" class="form-control" id="zip"name="">
										</div>
									</div>
									<div class="w-100"></div> <!-- divider -->
									<div class="col-md-6">
										<div class="form-group">
											<label for="phone">Phone No.</label>
											<input type="text" class="form-control" id="phone"name="">
										</div>
									</div>
									<div class="col-md-6">
										<div class="form-group">
											<label for="email">Email Address</label>
											<input type="email" class="form-control" id="email"name="">
										</div>
									</div>

								</div>
							</form>

							<div class="row">
								<div class="col-md-6  pb-5">
									<div class="border p-3 total-cart bg-lightgrey">
										<h3 class="poppins p-1">Cart Totals</h3>
										<p class="d-flex p-2">
											<span>Subtotal</span>
											<span>Rs ####.##</span>
										</p>
										<p class="d-flex p-2">
											<span>Delivery</span>
											<span>Rs 00.00</span>
										</p>
										<p class="d-flex p-2">
											<span>Discount</span>
											<span>Rs 30.00</span>
										</p>
										<p class="d-flex p-2 total border-top">
											<span>Total</span>
											<span>Rs ####.##</span>
										</p>
									</div>
								</div>
								<div class="col-md-6  pb-5">
									<div class="payment p-3 bg-lightgrey h-100">
										<h3 class="poppins p-1">Payment Method</h3>
										<div class="col-md-12 p-1">
											<div class="custom-control custom-radio">
    											<input type="radio" class="custom-control-input" id="first" name="billing_radio">
											    <label class="custom-control-label" for="first">Direct Bank Transfer</label>
											</div>
										</div>
										<div class="col-md-12 p-1">
											<div class="custom-control custom-radio">
    											<input type="radio" class="custom-control-input" id="second" name="billing_radio">
											    <label class="custom-control-label" for="second">Paytm</label>
											</div>
										</div>
										<div class="col-md-12 p-1">
											<div class="custom-control custom-radio">
    											<input type="radio" class="custom-control-input" id="third" name="billing_radio">
											    <label class="custom-control-label" for="third">Paypal</label>
											</div>
										</div>
										<div class="col-md-12 p-1">
											<div class="custom-control custom-radio">
    											<input type="radio" class="custom-control-input" id="fourth" name="billing_radio">
											    <label class="custom-control-label" for="fourth">Cash on Delivery</label>
											</div>
										</div>
										<div class="col-md-12 p-1">
											<div class="custom-control custom-checkbox">
    											<input type="checkbox" class="custom-control-input" id="fifth" name="billing_check">
											    <label class="custom-control-label" for="fifth">I have read and accept the terms and conditions</label>
											</div>
										</div>
										<div class="col-md-12 p-1 mt-2 d-flex justify-content-end">
											<button class="btn btn-outline-success">Place an order</button>
										</div>
									</div>
								</div>
							</div>
						</div>
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
</style>
