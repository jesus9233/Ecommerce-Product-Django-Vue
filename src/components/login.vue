<template>

  <div class="container-fluid bg-lightgrey pt-5">
    <div class="container pt-5">
      <div class="row">
        <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
          <div class="card card-signin my-5">
            <div class="card-body">
              <h4 class="card-title text-center">Sign In</h4>
              <form class="form-signin" @submit.prevent="login()">
                <div class="form-group mb-4">
                  <div class="p-relative">
                    <input type="email" id="inputEmail" class="form-control" v-model="email"
                    placeholder="Email address" required autofocus>
                    <font-awesome-icon icon="at" :class="{'active':email}" class="icon"/>
                  </div>
                </div>

                <div class="form-group mb-4">
                  <div class="p-relative">
                    <input :type="passType ? 'text' : 'password'" id="inputPassword"
                           class="form-control" placeholder="Password"
                           v-model="password" required>
                    <font-awesome-icon icon="lock-open" :class="{'active':password}"
                                       class="icon" v-if="passType"/>
                    <font-awesome-icon icon="lock" :class="{'active':password}"
                                       class="icon" v-else/>
                    <font-awesome-icon icon="eye" class="see-password icon" @click="passType = !passType"
                                       :class="{'active':passType}"/>
                  </div>
                </div>

                <button class="btn btn-lg btn-primary btn-block text-uppercase"
                type="submit" :disabled="!(email && password)">Sign in</button>
              </form>
                <b-alert
                 variant="danger"
                 dismissible
                 class="mt-4"
                 fade
                 :show="loginData.showDismissibleAlert"
                 @dismissed="loginData.showDismissibleAlert=false"
               >
                 {{loginData.errors}}
               </b-alert>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>


  export default {
    data() {
      return{
        email:'',
        password:'',
        passType:false,
      }
    },
    computed:{
      loginData(){
        return this.$store.state.login;
      }
    },
    methods: {
      login() {
          const data = {
          email: this.email.trim(),
          password: this.password.trim()
          }
          this.$store.commit('login', data);
      }
    }
  }

</script>

<style scoped>
  @import '../assets/css/form.css';
</style>
