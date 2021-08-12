<template>
  <div>
    <Logout>Logged out</Logout> 
  </div>
</template>


<script>
// import Login from './views/Login.vue'
import axios from "axios"    
export default {
  name: 'Logout',
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
