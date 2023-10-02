<script setup>
import {onMounted, reactive, ref, watch} from 'vue'

const errColor = "greenyellow";
const primaryInputColor = "--primary-input-color";
const inputIds = reactive(["username-edit", "password-edit", "email-edit", "phone-edit"]);
const inputName = ["用户名", "密码", "电子邮箱", "电话"];
const colorTypes = ["--primary-username-color", "--primary-password-color", "--primary-email-color", "--primary-phone-color"];
const signUpData = reactive(inputIds.reduce((acc, key) => {
  acc[key] = "";
  return acc;
}, {}));
const errorSpanIds = reactive(["username-error", "password-error", "email-error", "phone-error"]);
const inputColors = errorSpanIds.reduce((acc, key, index) => {
  acc[key] = colorTypes[index];
  return acc;
}, {});
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
  let i = 0;
  for (const inputId of inputIds) {
    const element =  document.getElementById(inputId);
    const errSpan = document.getElementById(errorSpanIds[i]);
    element.style.color = `var(${colorTypes[i]})`;
    errSpan.style.color = `var(${colorTypes[i]})`;
    i += 1;
  }


})

const restoreError = function (spanId) {
  console.log(isError[spanId]);
  isError[spanId] = false;
  errorMessages[spanId] = "";
  document.documentElement.style.setProperty(inputColors[spanId], primaryInputColor);
}

const handleError = function (spanId, message) {
  for (const errorSpanId of errorSpanIds) {
    if (spanId === errorSpanId) {
      errorMessages[spanId] = message;
      isError[spanId] = true;
      document.documentElement.style.setProperty(inputColors[spanId], errColor);
      return;
    }
  }
}

const getResult = function (api, method) {
  return {status: 0};
}

const signUpSuccess = function () {
  isSuccess.value = true;
  setTimeout(()=>{
    isSuccess.value = false;
  },3000);
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
  console.log(signUpData);
  for (const inputId of inputIds) {
    if (signUpData[inputId] === "") {
      const index = inputIds.indexOf(inputId);
      handleError(errorSpanIds[index], inputName[index] + "不能为空!");
      return;
    }
  }
  //getResult
  const result = getResult();
  if (result.status === 0) {
    signUpSuccess();
  } else if (result.status === -1) {
    //
  } else if (result.status === -2) {
  }
}
</script>

<template>
  <div>
    <div id="sign-up-view">
      <input :id="inputIds[0]" type="text" v-model="signUpData[inputIds[0]]" placeholder="用户名(<16位)">
      <span :id="errorSpanIds[0]" v-show="isError[errorSpanIds[0]]">{{ errorMessages[errorSpanIds[0]] }}</span>
      <input :id="inputIds[1]" type="password" v-model="signUpData[inputIds[1]]" placeholder="密码(8~16位)">
      <span :id="errorSpanIds[1]" v-show="isError[errorSpanIds[1]]">{{ errorMessages[errorSpanIds[1]] }}</span>
      <input :id="inputIds[2]" type="email" v-model="signUpData[inputIds[2]]" placeholder="电子邮箱">
      <span :id="errorSpanIds[2]" v-show="isError[errorSpanIds[2]]">{{ errorMessages[errorSpanIds[2]] }}</span>
      <input :id="inputIds[3]" type="tel" v-model="signUpData[inputIds[3]]" placeholder="电话号码">
      <span :id="errorSpanIds[3]" v-show="isError[errorSpanIds[3]]">{{ errorMessages[errorSpanIds[3]] }}</span>
      <button id="signup-btn" @click="onClickSignUpBtn">注册</button>
      <span id="success-msg" v-if="isSuccess" style="color : red;">注册成功!</span>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import "decoration.css";

#sign-up-view {
  display: flex;
  flex-direction: column;

  & input {
    margin: 14px;
  }

  & #signup-btn {
    border: 2px solid black;
    background-color: transparent;
    font-size: 18px;
    margin: 10px;
    transition: 0.1s;
  }

  & #signup-btn:hover {
    transform: scale(1.05);
  }

  & #signup-btn:active {
    transform: scale(0.95);
  }

}

</style>