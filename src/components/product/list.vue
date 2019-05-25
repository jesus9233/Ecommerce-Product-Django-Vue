<template>

  <div class="row justify-content-center">
    <div class="col-lg-12 col-md-10 col-sm-12 col-11">
      <div class="row">
          <div class="col-lg-3 col-sm-6 col-12 mb-4" v-for="product in productsValue">
            <app-product-thumb :product="product"></app-product-thumb>
          </div>
        </div>
    </div>
  </div>

</template>
<script>

  import ProductThumb from './productThumb'

  export default {
    props: ['productsValue'],
    components: {
      appProductThumb: ProductThumb
    }
  }

</script>
