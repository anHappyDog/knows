<script setup>
import {ref, watch} from "vue";
import {useRouter} from 'vue-router';
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
    document.documentElement.style.setProperty("--primary-username-color","greenyellow");
  }

  const restorePasswordError = function () {
    isPasswordError.value = false;
    passwordErrMessage.value = "";
    document.documentElement.style.setProperty("--primary-password-color","var(--primary-input-color)");
  }

  const getResult = function (api,method) {
    return { status : 0 };
  }

  const restoreUsernameError = function () {
    isUsernameError.value = false;
    usernameErrMessage.value = "";
    document.documentElement.style.setProperty("--primary-username-color","var(--primary-input-color)");
  }

  watch (username,(value, oldValue) => {
    if (isUsernameError) {
      restoreUsernameError();
    }
  })

  watch(password,(value,oldValue) => {
    if (isPasswordError) {
      restorePasswordError();
    }
  })

  const handlePasswordError = function (message) {
    isPasswordError.value = true;
    passwordErrMessage.value = message;
    document.documentElement.style.setProperty("--primary-password-color","greenyellow")
  }
  const onClickSignInBtn = function () {
    if (username.value === "") {
      handleUsernameError("用户名不能为空!");
      return;
    } else if (password.value === "") {
      handlePasswordError("密码不能为空!");
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
    <div id="signin-input">
    <input id="username-edit" type="text" v-model="username" placeholder="用户名">
      <span id="username-error" v-if="isUsernameError">{{usernameErrMessage}}</span>
      <input id="password-edit" type="password" v-model="password" placeholder="密码">
      <span id="password-error" v-if="true">{{passwordErrMessage}}</span>
      <button id="signin-btn" @click="onClickSignInBtn">登录</button>
      <a href="/public">忘记密码?</a>
  </div>
  </div>

</template>

<style scoped>
@import "decoration.css";


#signin-input {
  display: flex;
  flex-direction: column;

  & #signin-btn {
    font-size: 18px;
    border: 2px solid black;
    background-color: transparent;

    transition: 0.1s;
  }
  & #signin-btn:hover {
    transform: scale(1.05);
  }
  & #signin-btn:active {
    transform: scale(0.98);
  }

  & a {
    font-size: 18px;
    text-decoration: greenyellow;
    border-bottom: 2px solid;
    color: darkslateblue;
    position: absolute;
    top : 115%;
    left: 65%;
  }
}


#username-error,
#password-error {
  color: greenyellow;
}

#username-edit {
  color: var(--primary-username-color);
}
#password-edit {
  color: var(--primary-password-color);
}

</style>