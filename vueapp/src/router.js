import Vue from 'vue'
import VueRouter  from 'vue-router'
//import HelloWorld from './components/HelloWorld'
// import Home from './views/Home.vue'
// import Login from './views/Login.vue'
// import Logout from './views/Logout.vue'


Vue.use(VueRouter)

const router = new VueRouter({
    routes: [
      {
          path: "/login",
          name: "Login",
          component: () => import('./views/Login.vue')
      },
      {
          path: "/logout",
          name: "Logout",
          component: () => import('./views/Logout.vue')
      }
      ,
      {
          path: "/profile",
          name: "Profile",
          component: () => import('./views/Profile.vue')
      }
      ,
      {
          path: "/home",
          name: "Home",
          component: () => import('./views/Home.vue')
      }
    ]
  })

  export default router;
// const Home  = {
//     template: '<div>Home</div>'
//   }
  
//   const Login = {
//     template: '<div>Login</div>'
//   }
  
//   const Home = {
//     template: '<div>About</div>'
//   }


// const router = new VueRouter({
//     routes: [
//       { path: '/', component: Home },
//       {  path: '/login', component: Login },
//       {  path: '/logout', component: Logout },
 
//     ]
//   })

// export default router;

