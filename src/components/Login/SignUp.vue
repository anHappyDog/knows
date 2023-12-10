<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import axios from 'axios';
import alertStore from '../../alertStore';
import Alert from '../Alert.vue';
const methods = alertStore.methods;
const router = useRouter();
const username = ref('');
const email = ref('');
const password = ref('');
const passwordConfirm = ref('');
const errorMessage = ref('');
const successMessage = ref('');
const form = ref(null);
const loading = ref(false);
const msgExistTime = 2000;

const showErrorMessage = function (err) {
    errorMessage.value = err;
    setTimeout(() => {
        errorMessage.value = '';
    }, msgExistTime);
}

const showSuccessMessage = function (msg) {
    successMessage.value = msg;
    setTimeout(() => {
        successMessage.value = '';
    }, msgExistTime);
}

const onClickSignUpBtn = async function () {
    const isValid = await form.value.validate();
    if (!isValid.valid) {
        methods.addAlert({
            type: "error",
            message: "请先检查您的输入",
            timeout: 3000
        })
        return;
    }
    loading.value = true;
    try {
        const response = await axios.post(axios.defaults.baseURL + "/api/signUp", {
            username: username.value,
            email: email.value,
            password: password.value
        });
        if (response.data.status == 0) {
            loading.value = false;
            methods.addAlert({
                type: "success",
                message: "注册成功,请在登录界面登录!",
                timeout: 3000
            });
            router.push("/SignIn");
        } else {
            loading.value = false;
            methods.addAlert({
                type: "error",
                message: response.data.message,
                timeout: 3000
            });
        }
    } catch (err) {
        loading.value = false;
        methods.addAlert({
            type: "err",
            message: err.toString(),
            timeout: 3000
        });
    }
}

const onClickGoToSignInBtn = function () {
    router.push("/SignIn");
}

const usernameRules = [
    v => !!v || "用户名是必填项",
    v => v.length <= 20 || "用户名长度不能超过20个字符",
    v => /^[a-zA-Z0-9_]+$/.test(v) || "用户名只能包含字母、数字和下划线"
];
const emailRules = [
    v => !!v || "电子邮箱是必填项",
    v => /.+@.+\..+/.test(v) || "请输入正确的电子邮箱"
];
const passwordRules = [
    v => !!v || "密码是必填项",
    v => v.length <= 20 || "密码长度不能超过20个字符",
    v => v.length >= 6 || "密码长度不能少于6个字符",
    v => /^[a-zA-Z0-9_]+$/.test(v) || "密码只能包含字母、数字和下划线"
];
const passwordConfirmRules = [
    v => !!v || "确认密码是必填项",
    v => v == password.value || "两次输入的密码不一致"
];
</script>



<template>
    <v-container>
        <Alert />
        <v-container id="signup-container">
            <h1>Sign Up</h1><br />
            <v-sheet width="300px" class="mx-auto" id="signup-form">
                <v-form ref="form" @submit.prevent="onClickSignUpBtn">
                    <v-text-field type="text" v-model="username" label="用户名" :rules="usernameRules" />
                    <v-text-field type="text" v-model="email" label="电子邮箱" :rules="emailRules" />
                    <v-text-field type="password" v-model="password" label="密码" :rules="passwordRules" />
                    <v-text-field type="password" v-model="passwordConfirm" label="确认密码" :rules="passwordConfirmRules" />
                    <v-btn :loading="loading" type="submit" block class="mt-2">注册</v-btn>
                </v-form>
                <v-container display="flex">
                    <span>已经有了账号？</span>
                    <v-btn variant="plain" id="go-sign-in-btn" @click="onClickGoToSignInBtn">登录</v-btn>
                </v-container>
            </v-sheet>

        </v-container>
        <v-fade-transition>
            <v-alert class="log-msg" v-if="errorMessage" type="error" dismissible @input="errorMessage = null">{{
                errorMessage }}</v-alert>
            <v-alert class="log-msg" v-if="successMessage" type="success" dismissible @input="successMessage = null">{{
                successMessage }}</v-alert>
        </v-fade-transition>
    </v-container>
</template>


<style scoped>
#go-sign-in-btn {
    position: relative;
    left: 40%;
    font-size: medium;
}

#signup-form {
    margin-bottom: 10px;

}

.log-msg {
    position: absolute;
    top: 4%;
    right: 4%;
    width: 20%;
}

#signup-container {
    margin-top: 5%;
    display: flex;
    flex-direction: column;
    align-items: center;

}
</style>