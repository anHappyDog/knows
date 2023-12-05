<script setup>
import { ref } from 'vue';
import {useRouter} from 'vue-router';
import axios from 'axios';
const username = ref('');
const password = ref('');
const router = useRouter();
const onClickSignInBtn = async function() {
    console.log(axios.defaults.baseURL);
    try{
        const res = await axios.post(axios.defaults.baseURL + "/api/signIn", {
            username: username.value,
            password: password.value
        });
        if (res.data.status == 0) {
            localStorage.setItem('token',res.data.token);
            router.push('/main/articles');
        } else {
            console.log("no");
        }
    } catch(err) {
        console.log(err.toString());
    }
};


</script>



<template>
    <div>
        <h1>Sign In</h1>
        <form @submit.prevent="onClickSignInBtn">
            <label for="username">Username</label>
            <input type="username" id="username" v-model="username" />
            <label for="password">Password</label>
            <input type="password" id="password" v-model="password" />
            <button type="submit">Sign In</button>
        </form>
        <router-link to="/signUp">Sign Up</router-link>
    </div>
</template>


<style>
</style>