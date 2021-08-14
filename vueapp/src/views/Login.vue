
<template>
    <div>    
        <h2>Login</h2>    
        <form v-on:submit="login">    
            <input type="text" name="username" /><br>    
            <input type="text" name="email" /><br>    
            <input type="password" name="password" /><br>    
            <input type="submit" value="Login" />    
        </form>    
    </div>
</template>

<script>
    //import router from "./router"    
    import router from '../router'
    import axios from "axios"    
    axios.defaults.headers = { 'Accept': 'application/json', 'Content-Type': 'application/json' }
    
    export default {    
        name: "Login",    
        methods: {    
            login: (e) => {    
                e.preventDefault()    
                let username = "hp8"   
                let email = "quocoltd+8@gmail.com"   
                let password = "hp8@test"    
                let login = () => {    
                    let data = {    "username" : username,
                        "email": email,    
                        "password": password    
                    }    
                    
                    axios.post("http://127.0.0.1:8000/users/login/", data)    //http://127.0.0.1:8000/users/login/
                        .then((response) => {    
                            console.log("Logged in"||response)   
                            //axios.defaults.headers.common["Authorization"] ="Bearer " + localStorage.getItem("jwt");
                            localStorage.setItem("access_token",response.data.access_token);
                           // localStorage.setItem("jwt",response.data.refresh_token);
                            //localStorage.setItem("jwt",response.data.user);
                            //setCurrentUser(response.data);
                            router.push("/profile")    
                        })    
                        .catch((errors) => {    
                            console.log("Cannot log in"||errors)    
                        })    
                }    
                login()    
            }    
        }    
    }
</script>
