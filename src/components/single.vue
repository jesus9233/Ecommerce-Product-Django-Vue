<template>

  <div>
    <app-header>Single</app-header>
    <div class="pt-5">
      <div class="container">
        <template v-if="product">
          <div class="row pb-5 text-capitalize">
            <div class="col-lg-4">
              <div class="image">
                <img :src="image ? image :  product.product.thumb" alt="product image">
              </div>
            </div>
            <div class="col-lg-8">
              <h3 class="poppins">{{product.product.title}}</h3>
              <span>{{fetchMain}}</span><div>
                <p class="font-weight-bold d-inline-block">{{price ? price : product.product.price}}</p>
                <span class="text-monospace"></span>
              </div>
              <div class="my-3">
                  <label>Color</label>
                  <div>
                    <div v-for="child in product.children"
                     class="select-color" :class="{'selectedColor':child.is_main}">
                       <img :src="child.image" @click="childChanger(child.color)"
                        alt="color"
                        />
                    </div>
                  </div>
              </div>
              <div class="form-group">
                <label for="id_size">Size</label>
                <select class="custom-select" id="id_size" ref="selectedSize" @input="getQty">
                  <option value="undefined" selected>Select Size</option>9
                  <option v-for="variant in variants" :value="variant.size">{{variant.size}}</option>
                </select>
              </div>
              <h5 :class="qtyClass" v-if="qty !== '' ">{{qtyText}}</h5>
              <p>Department : {{product.product.gender}}</p>
              <p>Category : {{product.product.category}}</p>
              <p>Brand : {{product.product.brand}}</p>
              <p>Material : {{product.product.material_type}}</p>
              <div v-if="$store.state.cartItems">
                <button :class="inCart(variantId) ? 'btn-danger' :'btn-success'"
                @click="cartToggle(variantId)"  type="button" class="btn"
                :disabled="(variantId === '' || qty === 0) && !inCart(variantId) && cart">
                  <span v-if="product && inCart(variantId)">Remove from Cart</span>
                  <span v-else>Add to Cart</span>
                </button>
              </div>
            </div>
          </div>

          <div>
            <b-tabs content-class="mt-3">
              <b-tab title="Description" active><p>{{product.product.description}}</p></b-tab>
              <b-tab title="Reviews"><p>This is Review</p></b-tab>
            </b-tabs>
          </div>
        </template>
      </div>
    </div>
  </div>

</template>

<script>

  import Header from './header/header.vue'
  import axios from 'axios'

  export default {
    data() {
      return {
        image: '',
        variants: '',
        price: '',
        qty: '',
        qtyText: '',
        qtyClass: '',
        variantId: '',
        cart: ''
      }
    },
    components: {
      appHeader: Header
    },
    computed: {
      product() {
        var product = this.$store.state.productDetail
        if (product) {
          return product
        }
        return null
      },
      fetchMain() {
        var obj = this.$store.state.productDetail.children
        for (var i = 0; i < obj.length; i++) {
          if (obj[i].is_main == true) {
            this.fetchVariant(obj[i].id, obj[i].color)
          }
        }
      }
    },
    methods: {
      fetchProduct() {
        var slug = this.$route.params.slug
        this.$store.commit('getProductDetail', slug)
      },
      fetchVariant(id, color) {
        var color = color.replace('#', '')
        this.$store.state.loading = true
        axios
          .get(process.env.API_URL + '/api/variants/' + id + '/' + color)
          .then(response => {
            this.variants = response.data
            this.$store.state.loading = false
            this.$refs.selectedSize.value = undefined
            this.qty = ''
          })
          .catch(err => {
            console.log(err)
          })
      },
      cartToggle(productId) {
        this.cart = true
        this.$store.dispatch('cartToggle', productId).then((this.cart = false))
      },
      inCart(productId) {
        return this.$store.state.cartItems.cart.products.includes(productId)
      },
      childChanger(color) {
        let el = event.srcElement.parentNode
        for (var i = 0; i < el.parentNode.childNodes.length; i++) {
          el.parentNode.childNodes[i].classList.remove('selectedColor')
        }
        el.classList.add('selectedColor')
        var product = this.$store.state.productDetail.children
        for (var i = 0; i < product.length; i++) {
          if (product[i].color == color) {
            this.image = product[i].image
            this.price = product[i].price
            var id = product[i].id
            this.fetchVariant(id, color)
            this.variantId = ''
          }
        }
      },
      getQty() {
        var size = this.$refs.selectedSize.value
        for (var i = 0; i < this.variants.length; i++) {
          if (this.variants[i].size == size) {
            this.qty = this.variants[i].quantity
            this.variantId = this.variants[i].id
            if (this.qty > 10) {
              this.qtyClass = 'text-success'
              this.qtyText = 'In stock'
            } else if (this.qty <= 10 && this.qty > 0) {
              this.qtyClass = 'text-warning'
              this.qtyText = 'Only ' + this.qty + ' left'
            } else {
              this.qtyClass = 'text-danger'
              this.qtyText = 'Out of stock'
            }
          }
        }
      }
    },
    mounted() {
      this.fetchProduct()
    }
  }

</script>
<style scoped>

  .select-color {
    height: 5rem;
    width: 5rem;
    margin: 0rem 0.5rem;
    cursor: pointer;
    border: 1px solid;
    display: inline-block;
  }

  .image img,
  .select-color img {
    max-width: 100%;
  }
  .selectedColor {
    outline: 3px solid #00ff7f;
  }

</style>
