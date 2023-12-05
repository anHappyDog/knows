<script setup>
import { ref } from 'vue';
import axios from 'axios';
const username = ref('');
const email = ref('');
const password = ref('');
const passwordConfirm = ref('');

const onClickSignUpBtn = async function() {
    try{
        const response = await axios.post(axios.defaults.baseURL + "/api/signUp", {
            username: username.value,
            email: email.value,
            password: password.value
        });
        if (response.data.status == 0) {
            console.log("yes");
        }  else {
            console.log("no");
        }
    } catch( err) {
        console.log(err.toString());
    }
}

</script>



<template>
    <form @submit.prevent="onClickSignUpBtn" id="signup-form">
        <label for="username">Username</label>
        <input type="username" id="username" v-model="username" />
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" />
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" />
        <label for="passwordConfirm">Password Confirm</label>
        <input type="password" id="passwordConfirm" v-model="passwordConfirm" />
        <button type="submit">Sign Up</button>
    </form>
</template>


<style scoped>
#signup-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>