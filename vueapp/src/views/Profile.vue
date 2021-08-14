<template>
  <div>
    <h1>{{user.username}}</h1>
  </div>
</template>
<script>
import axios from "axios";
axios.defaults.headers = { 'Accept': 'application/json', 'Content-Type': 'application/json'}


export default {
  name: "Profile",
   data: function () {
    return {
      user:null
    }
  },

  
// const token = user.data.id; /*take only token and save in token variable*/
  methods: {     getInfo () {
        const token = localStorage.getItem('access_token'); //JSON.parse(localStorage.getItem('access_token'));
          axios.get('http://127.0.0.1:8000/users/profile/',{ headers: {"Authorization" : `Bearer ${token}`} })
          .then((response)=> {
              this.user = response.data
              // this.username = response.data['username'];
              // this.email = response.data['email'];
              console.log(response.data);
              // console.log(this.username);
        })
        .catch(function (error) {
              console.log(error);
        });
    }
},

mounted(){
this.getInfo();
}

}
 


    //in get request
// const auth = {
//         headers: {Authorization:'JWT ' + localStorage.getItem('access_token')} 
//         //headers: {'Token': localStorage.getItem('access_token')} 
//     }

// {headers : this.headers}

//    axios.defaults.headers.common["Authorization"] =
//                 "Bearer " + localStorage.getItem("jwt");
// axios.get('http://127.0.0.1:8000/users/profile/').then(result => { 
//  console.log(result.data)
// })
// getCurrentUser: function() {

   // call rest API
//    let self = this
   
//     axios.defaults.headers.common["Authorization"] =
//                 "Bearer " + localStorage.getItem("access_token");
//     axios
//         .get("http://127.0.0.1:8000/users/profile/")
//         .then(res => {
//          console.log("RESPONSE RECEIVED: ", res);
//          self.data=res;
//     })
//     .catch(err => {
//         console.log("AXIOS ERROR: ", err);
//     });
// },
//   }

</script>
