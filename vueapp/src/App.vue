<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <!-- <Login/> -->
        <div>    
            <router-link :to="{ name: 'Home'}">Home</router-link>    
            <router-link :to="{ name: 'Login'}">Login</router-link>    
            <a href="#" v-on:click="logout">Logout</a>    
        </div>    
        <router-view/>   
        <!-- <router-view></router-view> -->
  </div>
</template>

<script>
// import Login from './views/Login.vue'
import axios from "axios"    
export default {
  name: 'App',
   methods: {
     logout(evt) {
       if(confirm("Are you sure you want to log out?")) {
         axios.get('api/logout').then(response => {
          localStorage.removeItem('auth_token');

          // remove any other authenticated user data you put in local storage

          // Assuming that you set this earlier for subsequent Ajax request at some point like so:
          // axios.defaults.headers.common['Authorization'] = 'Bearer ' + auth_token ;
          delete axios.defaults.headers.common['Authorization'];
          console.log(response)
          // If using 'vue-router' redirect to login page
          this.$router.go('/login');
        })
        .catch(error => {
          // If the api request failed then you still might want to remove
          // the same data from localStorage anyways
          // perhaps this code should go in a finally method instead of then and catch
          // methods to avoid duplication.
          localStorage.removeItem('auth_token');
          delete axios.defaults.headers.common['Authorization'];
          this.$router.go('/login');
          console.log(error)
        });     
        console.log(evt)  
       }
     }
   },
  components: {
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
