<script>
import {onBeforeUnmount, onBeforeUpdate, onMounted, ref} from "vue";
import backgroundPng from '@/assets/1.png';
import {useRouter, useRoute, onBeforeRouteUpdate} from "vue-router";
import SignIn from "@/components/LoginBoard/subComponent/SignIn.vue";


export default {
  setup() {
    const username = ref('');
    const password = ref('');
    const router = useRouter();
    const route = useRoute();
    let underline;
    onMounted(() => {
      document.body.style.backgroundImage = `url(${backgroundPng})`;
      document.body.style.backgroundSize = "cover";
      document.body.style.backgroundRepeat = "no-repeat";
      document.body.style.height = "95vh";
      underline = document.getElementById("underline");
    });

    const changeToSignIn = function () {
      router.push("/loginBoard/signIn");
      underline.style.transform = `translateX(0px)`;
    }
    const changeToSignUp = function () {
      router.push("/loginBoard/signUp");
      underline.style.transform = `translateX(93px)`;

    }
    onBeforeUnmount(() => {
      document.body.style.backgroundImage = `none`;

    })
    return {username, password,changeToSignUp,changeToSignIn};
  },

}


</script>

<template>
  <div id="just-title-wrap">
    <p id="just-title-1">You can (not) redo.</p>
    <p id="just-title-2">You can (not) advance</p>
    <p id="just-title-3">You are (not) alone</p>

  </div>
<!--  <div id="pic-decorate"></div>-->
  <div id="login-board">
    <div id="board-decorate"></div>
    <div id="info-input">
      <div id="change-sign-in-up">
        <button class="sign-in-or-up" @click="changeToSignIn">登录</button>
        <div id="just-decorate-for-line"></div>
        <button class="sign-in-or-up" @click="changeToSignUp">注册</button>
      </div>
      <div id="underline"></div>
      <router-view id="user-input-view"></router-view>
    </div>
  </div>
</template>

<style scoped>
* {
  font-family: "Microsoft YaHei UI", serif;
}



#just-title-wrap {
  position: absolute;
  color: antiquewhite;
  font-size: 30px;
  top: 10px;
  left: 60%;
  width: 300px;

  & #just-title-2 {
    width: 400px;
    position: absolute;
    top: 20%;
    left: 30%;
  }

  & #just-title-3 {
    width: 400px;
    position: absolute;
    top: 40%;
    left: 70%;
  }
}

#login-board {
  display: flex;
  position: absolute;
  top: 20%;
  left: 60%;
  width: 500px;
  height: 400px;
  border: 2px solid black;
  box-shadow: 0 0 10px 2px rgba(0, 0, 0, 0.5);

  & #board-decorate {
    background-image: url("@/assets/5.jpg");
    background-size: cover;
    width: 40%;
  }


}

#info-input {
  width: 60%;
  justify-content: center;

  backdrop-filter: blur(20px);

  & #change-sign-in-up {
    display: flex;
    position: relative;
    top: 5%;
    left: 5%;

    & #just-decorate-for-line {
      border: 2px solid black;
    }
  }

}

.sign-in-or-up {
  font-size: 32px;
  border: none;

  background-color: transparent;
  padding: 0 14px;
  transition: 0.1s;
}

.sign-in-or-up:hover {
  transform: scale(1.05);
}

.sign-in-or-up:active {
  transform: scale(0.95);
}

.sign-in-or-up:last-child {
  border-right: none;
}

#underline {
  position: absolute;
  transition: transform 0.1s ease-in-out;
  width: 60px;
  top: 18%;
  left: 10%;
  border: 2px solid black;
}

#user-input-view {
  position: absolute;
  top: 20%;
  left: 0;
  margin: 10px;
}

@media(min-width: 1280px) {

#pic-decorate {
  background-image: url("@/assets/111.jpg");
  background-size: cover;
  width: 600px;
  height: 400px;

}
}

</style>
