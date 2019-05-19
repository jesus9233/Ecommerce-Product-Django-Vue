<template>
  <div>
    <app-header>Single</app-header>
    <div class="pt-5">
      <div class="container">
        <div class="row pb-5 text-capitalize">
          <div class="col-lg-4">
            <div class="image">
              <img v-if="product" :src="image ? image :  product.product.thumb" alt="product image">
            </div>
          </div>
          <div class="col-lg-8">
            <h3 class="poppins" v-if="product">{{product.product.title}}</h3>
            <span v-if="product">{{fetchMain}}</span><div>
              <p class="font-weight-bold d-inline-block" v-if="product">{{price ? price : product.product.price}}</p>
              <span class="text-monospace"></span>
            </div>
            <div class="my-3">
                <label>Color</label>
                <div v-if="product">
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
            <p v-if="product">Department : {{product.product.gender}}</p>
            <p v-if="product">Category : {{product.product.category}}</p>
            <p v-if="product">Brand : {{product.product.brand}}</p>
            <p v-if="product">Material : {{product.product.material_type}}</p>
            <div v-if="product">
              <button :class="inCart(variantId) ? 'btn-danger' :'btn-success'"
              @click="cartToggle(variantId)"  type="button" class="btn"
              :disabled="(variantId === '' || qty === 0) && !inCart(variantId)">
                <span v-if="product && inCart(variantId)">Remove from Cart</span>
                <span v-else>Add to Cart</span>
              </button>
            </div>
          </div>
        </div>
        <ul class="nav nav-pills">
          <li class="nav-item">
            <a class="nav-link active" data-toggle="pill" for="home" href="#home" @click="tabToggle">Description</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" data-toggle="pill" href="#desc" @click="tabToggle" for="desc">Reviews</a>
          </li>
        </ul>
        <!-- Tab panes -->
        <div class="tab-content">
          <div class="tab-pane container active" id="home" v-if="product">{{product.product.description}}</div>
          <div class="tab-pane container" id="desc">desc</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from './header/header.vue'
import axios from 'axios';

export default{
  data() {
    return {
      image:'',
      variants:'',
      price:'',
      qty:'',
      qtyText:'',
      qtyClass:'',
      variantId:''
    }
  },
  components:{
    appHeader:Header
  },
  computed:{
    product(){
      var product = this.$store.state.productDetail;
      if(product){
        return product;
      }
      return null;
    },
    fetchMain(){
      var obj = this.$store.state.productDetail.children;
      for (var i = 0; i < obj.length; i++) {
        if(obj[i].is_main == true){
          this.fetchVariant(obj[i].id, obj[i].color);
        }
      }
    }
  },
  methods:{
    fetchProduct(){
      var slug = this.$route.params.slug;
      this.$store.commit('getProductDetail',slug);
    },
    fetchVariant(id,color){
      var color = color.replace('#','');
      this.$store.state.loading = true;
      axios.get(process.env.API_URL+'/api/variants/'+id+'/'+color)
      .then((response) => {
        this.variants = response.data;
        this.$store.state.loading = false;
        this.$refs.selectedSize.value=undefined;
        this.qty=''
      })
      .catch((err) => {
        console.log(err);
      })
    },
    cartToggle(productId){
        this.$store.dispatch('cartToggle', productId);
    },
    inCart(productId){
      return this.$store.state.cartItems.cart.products.includes(productId);
    },
    childChanger(color){
      let el = event.srcElement.parentNode;
      for (var i = 0; i < el.parentNode.childNodes.length; i++) {
        el.parentNode.childNodes[i].classList.remove('selectedColor')
      }
      el.classList.add('selectedColor');
      var product = this.$store.state.productDetail.children;
      for (var i = 0; i < product.length; i++) {
        if(product[i].color == color){
              this.image = product[i].image;
              this.price = product[i].price;
              var id = product[i].id;
              this.fetchVariant(id, color);
              this.variantId='';
          }
      }
    },
    getQty(){
      var size = this.$refs.selectedSize.value;
      for (var i = 0; i < this.variants.length; i++) {
        if(this.variants[i].size == size){
          this.qty = this.variants[i].quantity;
          this.variantId = this.variants[i].id;
          console.log(this.variantId);
          if(this.qty > 10){
            this.qtyClass = 'text-success';
            this.qtyText = 'In stock';
          }
          else if(this.qty <= 10 && this.qty > 0){
            this.qtyClass = 'text-warning';
            this.qtyText = 'Only '+this.qty+' left';
          }
          else{
            this.qtyClass = 'text-danger';
            this.qtyText = 'Out of stock';
          }
        }
      }
    },
    tabToggle(){
        let el = event.srcElement;
        let id = el.getAttribute("for");
        let data = document.getElementById(id);
        let activePill = document.querySelector('.nav-pills .nav-link.active');
        let activeData = document.querySelector('.tab-pane.active');

        if(activeData && activePill) {
          activeData.classList.remove('active');
          activePill.classList.remove('active');
        }
        data.classList.add('active');
        el.classList.add('active');
      }
  },
  mounted(){
    this.fetchProduct();
  }
}

</script>
<style scoped>
  .select-color{
    height:5rem;
    width:5rem;
    margin:0rem 0.5rem;
    cursor:pointer;
    border:1px solid;
    display:inline-block;
  }

  .image img, .select-color img{
    max-width:100%;
  }
  .selectedColor{
    outline:3px solid #00FF7F;
  }
</style>
