<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import Feedback from '../Feedback/Feedback.vue';
const username = ref('');
const password = ref('');
const router = useRouter();
const isError = ref(false);
const errorMessage = ref('');
const form = ref(null);
const msgExistTime = 2000;
const logining = ref(false);

const showErrorMessage = function (err) {
    errorMessage.value = err;
    isError.value = true;
    setTimeout(() => {
        isError.value = false;
        errorMessage.value = '';
    }, msgExistTime);
}



const onClickSignInBtn = async function () {
    const isValid = await form.value.validate();

    if (!isValid.valid) {
        showErrorMessage("请先检查您的输入");
        return;
    }
    logining.value = true;
    try {
        const res = await axios.post(axios.defaults.baseURL + "/api/signIn", {
            username: username.value,
            password: password.value
        });
        if (res.data.status == 0) {
            localStorage.setItem('token', res.data.token);
            logining.value = false;
            router.push('/main/articles');

        } else {
            logining.value = false;
            showErrorMessage(res.data.message);

        }
    } catch (err) {
        logining.value = false;
        showErrorMessage(err.toString());

    }
};
const onClickSignUpBtn = function () {
    router.push("/SignUp");
}

const usernameRules = [
    v => !!v || "用户名是必填项",
    v => (v && v.length >= 3 && v.length <= 16) || "用户名长度必须在3到16个字符之间",
    v => /^[a-zA-Z0-9_]+$/.test(v) || "用户名只能包含字母、数字和下划线",
];
const passwordRules = [
    v => !!v || "密码是必填项",
    v => (v && v.length >= 6 && v.length <= 16) || "密码长度必须在6到16个字符之间",
];



</script>



<template>
    <v-container>
        <v-container id="login-container">
            <h1>Sign In</h1>
            <br />
            <v-sheet width="300" class="mx-auto login-form" id="signin-form">
                <v-form ref="form" fast-fail @submit.prevent="onClickSignInBtn">
                    <v-text-field v-model="username" label="用户名" :rules="usernameRules"></v-text-field>

                    <v-text-field v-model="password" type="password" label="密码" :rules="passwordRules"></v-text-field>

                    <v-btn :loading="logining" type="submit" block class="mt-2">登录</v-btn>
                </v-form>
                <v-container display="flex">
                    <span>新用户？</span>
                    <v-btn variant="plain" id="go-sign-up-btn" @click="onClickSignUpBtn">注册</v-btn>
                </v-container>
            </v-sheet>

        </v-container>
        <v-fade-transition>
            <v-alert class="log-msg" type="error" v-if="isError" dismissible>
                {{ errorMessage }}
            </v-alert>
        </v-fade-transition>
    </v-container>
</template>


<style scoped>
#signin-form {
    margin-bottom: 10px;
}

#login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 10%;
    width: 50%;
}

.log-msg {
    position: absolute;
    top: 4%;
    right: 4%;
    width: 20%;
}


#go-sign-up-btn {
    position: relative;
    left: 60%;
    font-size: medium;
}
</style>