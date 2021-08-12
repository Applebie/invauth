import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

// new Vue({
//   router
// }).$mount('#app')

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
// new Vue({
//   el: 'body',
//    render: function(createElement) {
//       return createElement(hello)
//   } });

