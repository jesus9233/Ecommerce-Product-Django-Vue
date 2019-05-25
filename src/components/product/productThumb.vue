<template>
  <div class="product-card o-h" :id="'product-card'+product.id"
     @mouseover="showDetails('product-card'+product.id)"
     @mouseout="hideDetails('product-card'+product.id)"
     @focus="showDetails('product-card'+product.id)"
     @blur="hideDetails('product-card'+product.id)"
     tabindex="0" ref="card">
     <div class="overlay">

     </div>
     <router-link class="view-details text-uppercase font-weight-bold poppins"
     :to="'/product/'+product.slug" tag="button">VIEW DETAILS</router-link>
    <div class="product-img">
      <img :src="product.thumb" alt="Product Thumbnail" class="w-100 h-100 product-thumb">
    </div>
    <div class="" style="height:90px;">
      <div class="details p-3 bg-white o-h">
        <h6 class="text-left text-capitalize title">{{product.title}}</h6>
        <div class="d-flex">
          <div class="d-inline-flex w-50 brand text-capitalize">
            <span class="text-secondary">{{product.brand}}</span>
          </div>
          <div class="d-inline-flex w-50 justify-content-end">
            <h6 class="text-success">Rs. {{product.price}}</h6>
          </div>
        </div>
        <div class="sizes mt-2">
          <h6 class="text-left">Sizes</h6>
          <p class="text-secondary text-left poppins ml-2">
            <template v-for="size, index in product.sizes">
              {{size}}
              <span v-if="index != product.sizes.length-1">, </span>
            </template>
          </p>
        </div>
        <div class="colors mt-2">
          <h6 class="text-left">Colors</h6>
          <p class="text-secondary text-left poppins ml-2 mb-0">
            <template v-for="color in product.colors">
                <div :style="'background-color:'+color" class="color">
                </div>
            </template>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
	export default{
	props:['product'],
	methods:{
		showDetails(id){
      let el = this.$refs["card"];
			   el.classList.add('animate');
			},
      hideDetails(id){
        let el = this.$refs["card"];
          el.classList.remove('animate');
      },
    }
	}

</script>
<style scoped>
.product-card{
  background-color:#fff;
  position:relative;
  height:380px;
  transition:0.15s;
}

.title,.brand{
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.overlay{
  content:'';
  position:absolute;
  height:100%;
  width:100%;
  background-color:#48daa1;
  top:0;
  left:0;
  opacity:0;
  transition:0.15s;
}
.animate .overlay{
  opacity:0.7;
}
.product-card.animate{
  box-shadow:0px 0px 10px 10px  #ebedee;
}
.product-img{
  height:300px;
  }
  .product-img img{
    object-fit:contain;
  }
.color{
  height:20px;
  width:20px;
  border-radius:50%;
  border:2px solid #e8e9eb;
  margin-right:5px;
  cursor:pointer;
  transition:0.15s;
  display:inline-block;
}
.color:hover{
  transform:scale(1.2);
}
.view-details{
  padding:0.5rem 1rem;
  color:#fff;
  white-space:nowrap;
  border:2px solid #fff;
  opacity:0;
  background:transparent;
  position:absolute;
  top:50px;
  left:50%;
  z-index:-1;
  transform:translateX(-50%) scale(1.2);
  transition:0.3s;
}
.view-details:hover{
  background-color:#fff;
  color:#48daa1;
}
.animate .view-details{
  opacity:1;
  z-index:1;
  transform:translateX(-50%) scale(1);
}
div:focus{
  outline:none;
}
/*
.row .trend{
	text-decoration: none;
	color: black;
}
*/
.o-h{
	overflow: hidden;
}
.details{
  height:80px;
  position:absolute;
  transition:0.15s ease-out;
  top:300px;
  width:100%;
  z-index:1;
}
.animate .details{
  height:210px;
  top:180px;
}
/*
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
} */
/* Generals resets and unimportant stuff */

/* --- Product Card ---- */
/* .make-3D-space{
    position: relative;
    perspective: 800px;
    width:340px;
    height:500px;
    transform-style: preserve-3d;
    transition: transform 5s;
    position:absolute;
    top:80px;
    left:50%;
    margin-left:-167px;
}*/
/* .product-front{
	background:#fff;
	height:300px;
	width:200px;
	-webkit-transition: all 100ms ease-out;
       -moz-transition: all 100ms ease-out;
         -o-transition: all 100ms ease-out;
            transition: all 100ms ease-out;
} */
/*
.product-card.animate .product-front{
	top:0px;
	left:0px;
	-webkit-transition: all 100ms ease-out;
       -moz-transition: all 100ms ease-out;
         -o-transition: all 100ms ease-out;
            transition: all 100ms ease-out;
}
.product-card{
	width:325px;
	height:490px;
	position:absolute;
	top:10px;
	left:10px;
	overflow:hidden;
    transform-style: preserve-3d;
	-webkit-transition:  100ms ease-out;
       -moz-transition:  100ms ease-out;
         -o-transition:  100ms ease-out;
            transition:  100ms ease-out;
}
.product-card.animate{
	top:5px;
	left:5px;
	width:335px;
	height:500px;
	box-shadow:0px 13px 21px -5px rgba(0, 0, 0, 0.3);
	-webkit-transition:  100ms ease-out;
       -moz-transition:  100ms ease-out;
         -o-transition:  100ms ease-out;
            transition:  100ms ease-out;
}
.stats-container{
	background:#fff;
	position:absolute;
	top:386px;
	left:0;
	width:100%;
	height:300px;
	padding:27px 35px 35px;
	-webkit-transition: all 200ms ease-out;
       -moz-transition: all 200ms ease-out;
         -o-transition: all 200ms ease-out;
            transition: all 200ms ease-out;
}
.product-card.animate .stats-container{
	top:272px;
	-webkit-transition: all 200ms ease-out;
       -moz-transition: all 200ms ease-out;
         -o-transition: all 200ms ease-out;
            transition: all 200ms ease-out;
}
.stats-container .product_name{
	font-size:22px;
	color:#393c45;
}
.stats-container p{
	font-size:16px;
	color:#b1b1b3;
	padding:2px 0 20px 0;
}
.stats-container .product_price{
	float:right;
	color:#48cfad;
	font-size:22px;
	font-weight:600;
}
.image_overlay{
	position:absolute;
	top:0;
	left:0;
	width:100%;
	height:100%;
	background:#48daa1;
	opacity:0;
}
.product-card.animate .image_overlay{
	opacity:0.7;
	-webkit-transition: all 200ms ease-out;
       -moz-transition: all 200ms ease-out;
         -o-transition: all 200ms ease-out;
            transition: all 200ms ease-out;
}
.product-options{
	padding:2px 0 0;
}
.product-options strong{
	font-weight:700;
	color:#393c45;
	font-size:14px;
}
.product-options span{
	color:#969699;
	font-size:14px;
	display:block;
	margin-bottom:8px;
}
.view_details{
	position:absolute;
	top:112px;
	left:50%;
	margin-left:-85px;
	border:2px solid #fff;
	color:#fff;
	font-size:19px;
	text-align:center;
	text-transform:uppercase;
	font-weight:700;
	padding:10px 0;
	width:172px;
	opacity:0;
	-webkit-transition: all 200ms ease-out;
       -moz-transition: all 200ms ease-out;
         -o-transition: all 200ms ease-out;
            transition: all 200ms ease-out;
}
.view_details:hover{
	background:#fff;
	color:#48cfad;
	cursor:pointer;

}
.product-card.animate .view_details{
	opacity:1;
	width:152px;
	font-size:15px;
	margin-left:-75px;
	top:115px;
	-webkit-transition: all 200ms ease-out;
       -moz-transition: all 200ms ease-out;
         -o-transition: all 200ms ease-out;
            transition: all 200ms ease-out;
}
div.colors div{
	margin-top:3px;
	width:15px;
	height:15px;
	margin-right:5px;
	float:left;
}
div.colors div span{
	width:15px;
	height:15px;
	display:block;
	border-radius:50%;
	border:2px solid #e8e9eb;
}
div.colors div span:hover{
	width:17px;
	height:17px;
	margin:-1px 0 0 -1px;
}
div.shadow{
	width:335px;height:520px;
	opacity:0;
	position:absolute;
	top:0;
	left:0;
	z-index:3;
	display:none;
	background: -webkit-linear-gradient(left,rgba(0,0,0,0.1),rgba(0,0,0,0.2));
    background: -o-linear-gradient(right,rgba(0,0,0,0.1),rgba(0,0,0,0.2));
    background: -moz-linear-gradient(right,rgba(0,0,0,0.1),rgba(0,0,0,0.2));
    background: linear-gradient(to right, rgba(0,0,0,0.1), rgba(0,0,0,0.2));
} */
/* #product-back div.shadow{
	z-index:10;
	opacity:1;
	background: -webkit-linear-gradient(left,rgba(0,0,0,0.2),rgba(0,0,0,0.1));
    background: -o-linear-gradient(right,rgba(0,0,0,0.2),rgba(0,0,0,0.1));
    background: -moz-linear-gradient(right,rgba(0,0,0,0.2),rgba(0,0,0,0.1));
    background: linear-gradient(to right, rgba(0,0,0,0.2), rgba(0,0,0,0.1));
}
#flip-back{
	position:absolute;
	top:20px;
	right:20px;
	width:30px;
	height:30px;
	cursor:pointer;
}
#cx, #cy{
	background:#d2d5dc;
	position:absolute;
	width:0px;
	top:15px;
	right:15px;
	height:3px;
	-webkit-transition: all 250ms ease-in-out;
	   -moz-transition: all 250ms ease-in-out;
		-ms-transition: all 250ms ease-in-out;
		 -o-transition: all 250ms ease-in-out;
			transition: all 250ms ease-in-out;
}
#flip-back:hover #cx, #flip-back:hover #cy{
	background:#979ca7;
	-webkit-transition: all 250ms ease-in-out;
	   -moz-transition: all 250ms ease-in-out;
		-ms-transition: all 250ms ease-in-out;
		 -o-transition: all 250ms ease-in-out;
			transition: all 250ms ease-in-out;
}
#cx.s1, #cy.s1{
	right:0;
	width:30px;
	-webkit-transition: all 100ms ease-out;
	   -moz-transition: all 100ms ease-out;
		-ms-transition: all 100ms ease-out;
		 -o-transition: all 100ms ease-out;
			transition: all 100ms ease-out;
}
#cy.s2{
	-ms-transform: rotate(50deg);
	-webkit-transform: rotate(50deg);
	transform: rotate(50deg);
	-webkit-transition: all 100ms ease-out;
	   -moz-transition: all 100ms ease-out;
		-ms-transition: all 100ms ease-out;
		 -o-transition: all 100ms ease-out;
			transition: all 100ms ease-out;
}
#cy.s3{
	-ms-transform: rotate(45deg);
	-webkit-transform: rotate(45deg);
	transform: rotate(45deg);
	-webkit-transition: all 100ms ease-out;
	   -moz-transition: all 100ms ease-out;
		-ms-transition: all 100ms ease-out;
		 -o-transition: all 100ms ease-out;
			transition: all 100ms ease-out;
}
#cx.s1{
	right:0;
	width:30px;
	-webkit-transition: all 100ms ease-out;
	   -moz-transition: all 100ms ease-out;
		-ms-transition: all 100ms ease-out;
		 -o-transition: all 100ms ease-out;
			transition: all 100ms ease-out;
}
#cx.s2{
	-ms-transform: rotate(140deg);
	-webkit-transform: rotate(140deg);
	transform: rotate(140deg);
	-webkit-transition: all 100ms ease-out;
	   -moz-transition: all 100ms ease-out;
		-ms-transition: all 100ease-out;
		 -o-transition: all 100ms ease-out;
			transition: all 100ms ease-out;
}
#cx.s3{
	-ms-transform: rotate(135deg);
	-webkit-transform: rotate(135deg);
	transform: rotate(135deg);
	-webkit-transition: all 100ease-out;
	   -moz-transition: all 100ms ease-out;
		-ms-transition: all 100ms ease-out;
		 -o-transition: all 100ms ease-out;
			transition: all 100ms ease-out;
}
#carousel{
	width:335px;
	height:500px;
	overflow:hidden;
	position:relative;

}
#carousel ul{
	position:absolute;
	top:0;
	left:0;
}
#carousel li{
	width:335px;
	height:500px;
	float:left;
	overflow:hidden;
}
.arrows-perspective{
	width:335px;
	height:55px;
	position: absolute;
	top: 218px;
	transform-style: preserve-3d;
    transition: transform 5s;
	perspective: 335px;
}
.carouselPrev, .carouselNext{
	width: 50px;
	height: 55px;
	background: #ccc;
	position: absolute;
	top:0;
	transition: all 200ms ease-out;
	opacity:0.9;
	cursor:pointer;
}
.carouselNext{
	top:0;
	right: -26px;
	-webkit-transform: rotateY( -117deg );
         -moz-transform: rotateY( -117deg );
           -o-transform: rotateY( -117deg );
              transform: rotateY( -117deg );
			  transition: all 200ms ease-out;

}
.carouselNext.visible{
		right:0;
		opacity:0.8;
		background: #efefef;
		-webkit-transform: rotateY( 0deg );
         -moz-transform: rotateY( 0deg );
           -o-transform: rotateY( 0deg );
              transform: rotateY( 0deg );
			  transition: all 200ms ease-out;
}
.carouselPrev{
	left:-26px;
	top:0;
	-webkit-transform: rotateY( 117deg );
         -moz-transform: rotateY( 117deg );
           -o-transform: rotateY( 117deg );
              transform: rotateY( 117deg );
			  transition: all 200ms ease-out;

}
.carouselPrev.visible{
		left:0;
		opacity:0.8;
		background: #eee;
		-webkit-transform: rotateY( 0deg );
         -moz-transform: rotateY( 0deg );
           -o-transform: rotateY( 0deg );
              transform: rotateY( 0deg );
			  transition: all 200ms ease-out;
}
#carousel .x, #carousel .y{
	height:2px;
	width:15px;
	background:#48cfad;
	position:absolute;
	top:31px;
	left:17px;
	-ms-transform: rotate(45deg);
	-webkit-transform: rotate(45deg);
	transform: rotate(45deg);
}
#carousel .x{
	-ms-transform: rotate(135deg);
	-webkit-transform: rotate(135deg);
	transform: rotate(135deg);
	top:21px;
}
#carousel .carouselNext .x{
	-ms-transform: rotate(45deg);
	-webkit-transform: rotate(45deg);
	transform: rotate(45deg);
}
#carousel .carouselNext .y{
	-ms-transform: rotate(135deg);
	-webkit-transform: rotate(135deg);
	transform: rotate(135deg);
} */
</style>
