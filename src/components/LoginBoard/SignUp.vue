<script setup>

import axios from "axios";
import {onMounted, reactive, ref, watch} from "vue";

const inputIds = reactive(["username-edit", "password-edit", "email-edit", "phone-edit"]);
const inputName = ["用户名", "密码", "电子邮箱", "电话"];
const signUpData = reactive(inputIds.reduce((acc, key) => {
  acc[key] = "";
  return acc;
}, {}));
const errorSpanIds = reactive(["username-error", "password-error", "email-error", "phone-error"]);

const errorMessages = reactive(errorSpanIds.reduce((acc, key) => {
  acc[key] = "";
  return acc;
}, {}));
const isError = reactive(errorSpanIds.reduce((acc, key) => {
  acc[key] = false;
  return acc;
}, {}));
const isSuccess = ref(false);

onMounted(() => {
});

const restoreError = function (spanId) {
  isError[spanId] = false;
  errorMessages[spanId] = "";
}

const handleError = function (spanId, message) {
  isSuccess.value = false;
  for (const errorSpanId of errorSpanIds) {
    if (spanId === errorSpanId) {
      errorMessages[spanId] = message;
      isError[spanId] = true;
      return;
    }
  }
}

const getResult = async function () {
  try {
    const result = await axios.post("http://127.0.0.1:8000/api/signUp", {
      username: signUpData[inputIds[0]],
      password: signUpData[inputIds[1]],
      email: signUpData[inputIds[2]],
      phone: signUpData[inputIds[3]]
    });
    return result.data;
  } catch (error) {
    console.log(error);
    throw error;
  }

}

const signUpSuccess = function () {
  isSuccess.value = true;
  setTimeout(() => {
    isSuccess.value = false;
  }, 3000);
}
watch(signUpData, (value, oldValue, onCleanup) => {
  let i = 0;
  for (const errorSpanId of errorSpanIds) {
    if (isError[errorSpanId]) {
      restoreError(errorSpanId);
    }
    ++i;
  }
})

const onClickSignUpBtn = function () {
  for (const inputId of inputIds) {
    if (signUpData[inputId] === "") {
      const index = inputIds.indexOf(inputId);
      handleError(errorSpanIds[index], inputName[index] + "不能为空!");
      return;
    }
  }
  //getResult
  getResult().then(result => {
    if (result.status === 0) {
      signUpSuccess();
    } else if (result.status === -1) {
      handleError(errorSpanIds[0], "用户名已存在!")
    } else if (result.status === -2) {
    }
  }).catch(err => {
    console.log(err);
  });
}
</script>

<template>
  <div>
    <div id="sign-container">
      <input :class="{'input-info':true,'error':isError[errorSpanIds[0]]}" :id="inputIds[0]" maxlength="16" type="text"
             v-model="signUpData[inputIds[0]]" placeholder="用户名(<16位)">
      <span class="error-show" :id="errorSpanIds[0]" v-show="isError[errorSpanIds[0]]">{{
          errorMessages[errorSpanIds[0]]
        }}</span>
      <input :class="{'input-info':true,'error':isError[errorSpanIds[1]]}" :id="inputIds[1]" maxlength="16"
             type="password" v-model="signUpData[inputIds[1]]" placeholder="密码(8~16位)">
      <span class="error-show" :id="errorSpanIds[1]" v-show="isError[errorSpanIds[1]]">{{
          errorMessages[errorSpanIds[1]]
        }}</span>
      <input :class="{'input-info':true,'error':isError[errorSpanIds[2]]}" :id="inputIds[2]" maxlength="40" type="email"
             v-model="signUpData[inputIds[2]]" placeholder="电子邮箱">
      <span class="error-show" :id="errorSpanIds[2]" v-show="isError[errorSpanIds[2]]">{{
          errorMessages[errorSpanIds[2]]
        }}</span>
      <input :class="{'input-info':true,'error':isError[errorSpanIds[3]]}" :id="inputIds[3]" maxlength="20" type="tel"
             v-model="signUpData[inputIds[3]]" placeholder="电话号码">
      <span class="error-show" :id="errorSpanIds[3]" v-show="isError[errorSpanIds[3]]">{{
          errorMessages[errorSpanIds[3]]
        }}</span>
      <button class="sign-btn" @click="onClickSignUpBtn">注册</button>
      <span id="success-msg" v-if="isSuccess" style="color : #c45656;">注册成功!</span>
    </div>
  </div>
</template>

<style scoped>
@import "LoginBoard.css";

#success-msg {
  position: absolute;
  top: 100%;
  left: 40%;
}
</style>