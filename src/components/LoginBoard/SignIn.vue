<script setup>
import {useRouter} from "vue-router";
import {ref, watch} from "vue";

const router = useRouter();
const username = ref('');
const password = ref('');
const isUsernameError = ref(false);
const isPasswordError = ref(false);
const usernameErrMessage = ref('sad');
const passwordErrMessage = ref('');
const handleUsernameError = function (message) {
  isUsernameError.value = true;
  usernameErrMessage.value = message;
}

const restorePasswordError = function () {
  isPasswordError.value = false;
  passwordErrMessage.value = "";
}

const getResult = function (api, method) {
  return {status: 0};
}

const restoreUsernameError = function () {
  isUsernameError.value = false;
  usernameErrMessage.value = "";
}

watch(username, (value, oldValue) => {
  if (isUsernameError) {
    restoreUsernameError();
  }
})

watch(password, (value, oldValue) => {
  if (isPasswordError) {
    restorePasswordError();
  }
})

const handlePasswordError = function (message) {
  isPasswordError.value = true;
  passwordErrMessage.value = message;
}
const onClickSignInBtn = function () {
  if (username.value === "") {
    handleUsernameError("你永远无法达到空用户名的真实!");
    return;
  } else if (password.value === "") {
    handlePasswordError("你永远不能用空密码来到达Stein's Gate!");
    return;
  }
  //get result from backend
  let result = getResult();
  if (result.status === 0) {
    router.push("/mainPage");
  } else if (result.status === -1) {
    handleUsernameError("用户名不存在");
  } else if (result.status === -2) {
    handlePasswordError("密码不正确");
  } else if (result.status === -3) {
    //其他错误。
  }
}


</script>

<template>
  <div>
    <div id="sign-container">
      <span id="title">Asuka</span>
      <input :class="{'input-info':true,'error':isUsernameError}" type="text" v-model="username" placeholder="用户名">
      <span class="error-show" v-if="isUsernameError">{{ usernameErrMessage }}</span>
      <input :class="{'input-info':true,'error':isPasswordError}" type="password" v-model="password" placeholder="密码">
      <span class="error-show" v-if="isPasswordError">{{ passwordErrMessage }}</span>
      <button class="sign-btn" @click="onClickSignInBtn">登录</button>
      <a id="forgot-password">忘记密码</a>
    </div>
  </div>
</template>

<style scoped>
@import "LoginBoard.css";
#title {
  color: #e4e7ed;
  font-weight: bold;
  font-size: 32px;
  position: absolute;
  width: 40%;
  left: 30%;
  top: -40%;
  user-select: none;
}
#forgot-password {
  position: absolute;
  top: 100%;
  left: 70%;
  cursor: pointer;
  text-decoration-line: underline;

}
</style>