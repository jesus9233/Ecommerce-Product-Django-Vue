<template>
  <div class="container py-5">
    <div class="row">
      <div class="col-lg-3 col-6 py-3 text-center" v-for="product in productsValue">
        <app-product-thumb :product="product"></app-product-thumb>
      </div>
    </div>
  </div>
</template>
<script>
import ProductThumb from './productThumb';

    export default{
      props:['productsValue'],
      components:{
        appProductThumb:ProductThumb,
      }
    }
</script>
