<template>
  <div class="container-fluid bg-lightgrey pt-5">
    <div class="container pt-5">
      <div class="row">
        <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
          <div class="card card-signin my-5">
            <div class="card-body">
              <h4 class="card-title text-center">Sign Up</h4>
              <form class="form-signin" @submit.prevent="register()">
                <div class="form-group mb-4">
                  <div class="p-relative">
                    <input type="text" id="inputUsername" class="form-control"
                           v-model="username" placeholder="Username"
                           :class="{'is-invalid':errors.username}" required>
                    <font-awesome-icon icon="user" :class="{'active':username}" class="icon" />
                    <b-form-invalid-feedback v-if="errors.username">
                      <p class="ml-2" v-for="error in errors.username">{{error}}</p>
                    </b-form-invalid-feedback>
                  </div>
                </div>

                <div class="form-group mb-4">
                  <div class="p-relative">
                    <input type="email" id="inputEmail" class="form-control" v-model="email"
                    placeholder="Email address" :class="{'is-invalid':errors.email}"
                    required autofocus>
                    <font-awesome-icon icon="at" :class="{'active':email}" class="icon"/>

                    <b-form-invalid-feedback v-if="errors.email">
                      <p class="ml-2" v-for="error in errors.email">{{error}}</p>
                    </b-form-invalid-feedback>
                  </div>
                </div>

                <div class="form-group mb-4">
                  <div class="p-relative">
                    <input :type="passType ? 'text' : 'password'" id="inputPassword"
                           class="form-control" placeholder="Password"
                           v-model="password" :class="{'is-invalid':errors.password}"
                           required>
                   <font-awesome-icon icon="lock-open" :class="{'active':password}"
                                      class="icon" v-if="passType"/>
                   <font-awesome-icon icon="lock" :class="{'active':password}"
                                      class="icon" v-else/>
                   <font-awesome-icon icon="eye" class="see-password icon" @click="passType = !passType"
                                      :class="{'active':passType}"/>
                    <b-form-invalid-feedback v-if="errors.password">
                      <p v-for="error in errors.password">{{error}}</p>
                    </b-form-invalid-feedback>
                  </div>
                </div>

                <button class="btn btn-lg btn-primary btn-block text-uppercase"
                type="submit" :disabled="!(email && username && password)">Sign up</button>
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

<script type="text/javascript">
  import axios from 'axios';
  export default{
    data(){
      return{
        username:'',
        email:'',
        password:'',
        errors:'',
        passType:false
      }
    },
    computed:{
      loginData(){
        return this.$store.state.login;
      }
    },
    methods:{
      register(){
        this.$store.state.loading = true;
        const data = {
          "username":this.username,
          "email":this.email,
          "password":this.password
        }
        axios.post(process.env.API_URL+'/api/user/register/', data)
        .then((res) => {
          this.$store.commit('login', data);
          this.username='',this.password='',this.email='',this.errors='';
          this.$store.state.loading = false;
        })
        .catch((err) => {
          if(err.response){
            this.errors = err.response.data;
            console.log(this.errors)
          }
          console.log(err);
          this.$store.state.loading = false;
        })
      },
    }
  }
</script>
<style scoped>
  @import '../assets/css/form.css';
</style>
