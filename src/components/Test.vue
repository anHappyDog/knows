<script setup>
import {ref,onMounted,onBeforeMount} from "vue";
import {useRouter} from "vue-router";

const router = useRouter();
const goSignIn = function (){
  router.push("signIn");
}
const goSignUp = function () {
  router.push("signUp");
}

</script>

<template>
  <div class="gradient">
      <div id="login-board-container">
        <div id="login-choice-container">
          <button @click="goSignIn">登录</button>
          <div id="decorate-line"></div>
          <button @click="goSignUp">注册</button>
        </div>
        <transition name="sign-change" mode="out-in">
        <router-view></router-view>
        </transition>
        <div id="decorate-container">
        <div class="decorate-line">
        </div>
        <div id="decorate-circle"></div>
        <div class="decorate-line">
        </div>

      </div>
  </div>

  </div>


</template>

<style scoped>
@import "test.css";

@keyframes gradientBG {
  0% {
    background-position: 0 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0 50%;
  }
}

#decorate-container {
  display: flex;
  position: absolute;
  top: 85%;
  width: 80%;
  left: 10%;
  justify-content: center;
  background-color: #e4e7ed;
  & .decorate-line {
    height: 5px;
    width: 50%;
    margin: 0 30px;
    background-color: #e4e7ed;
  }
}

.gradient {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  min-height: 500px;
  background: linear-gradient(-45deg, rgb(135, 133, 138), rgba(194, 194, 196, 0.7), rgba(225, 227, 227, 0.75), rgb(210, 228, 231),rgb(255 255 255));
  background-size: 600% 600%;
  animation: gradientBG 5s ease infinite;
}

#login-choice-container {
  display: flex;
  position: absolute;
  justify-content: center;
  top : 6%;
  left: 30%;
  right: 30%;
  width: 40%;
  & #decorate-line {
    border: 2px solid black;
  }
  & button {
    margin: 0 20px;
    border: none;
    background-color: transparent;
    font-size: 20px;
    transition: scale 0.1s;
    cursor: pointer;
}

  & button:hover {
    transform: scale(1.08);
}

}

#login-board-container {
  background-color: white;
  border: 2px solid #e4e7ed;
  box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);;
  display: flex;
  position: absolute;
  flex-direction: column;
  top: 16%;
  left: 33%;
  width: 500px;
  height: 450px;
  justify-content: center;
}

</style>