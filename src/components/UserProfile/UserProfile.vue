<script setup>
import Test from "@/components/Test.vue"
import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import {computed, onMounted, ref} from "vue";
import downArrow from "@/assets/downArrow.svg";
import upArrow from "@/assets/upArrow.svg";
import ArticleList from "@/components/ArticleList/ArticleList.vue";
import GoTopBtn from "@/components/SubComponents/GoTopBtn.vue";

const userInfoHeight = ref(0 + "px");
const loadBtnImg = ref(downArrow);
const loadBtnText = ref("展开个人资料");
const username = ref("funnySunShine");
const curExp = ref("");
const email = ref("");
const phone = ref("");
const introduction = ref("");

let isLoadProfile = false;
onMounted(() => {
})
const userInfoStyle = computed(() => {
  return `height : ${userInfoHeight.value}`;
})

const onClickLoadBtn = function () {
  if (!isLoadProfile) {
    isLoadProfile = true;
    userInfoHeight.value = 180 + "px";
    loadBtnImg.value = upArrow;
    loadBtnText.value = "收起个人资料";
  } else {
    isLoadProfile = false;
    userInfoHeight.value = 0 + "px";
    loadBtnImg.value = downArrow;
    loadBtnText.value = "展开个人资料";

  }
}
const onClickUploadProfileBtn = function () {

}
const onChangeInfoBtn = function () {

}
</script>

<template>
  <header>
    <NavigationBar/>
  </header>
  <main>
    <div id="user-profile-container">
      <div id="user-profile">
        <div id="profile-img-container">
          <button id="load-profile-img-btn">上传封面</button>

        </div>
        <div id="user-info-container">
          <div id="avatar-container">
            <div id="avatar-img-container">

            </div>

          </div>
          <h2>{{ username }}</h2>
          <div id="user-info" :style="userInfoStyle">
            <p>当前经验值:{{ curExp }}</p>
            <p>电子邮箱:{{ email }}</p>
            <p>电话:{{ phone }}</p>
            <p>个人介绍:{{ introduction }}</p>
          </div>
          <div>
            <button id="load-Info-btn" @click="onClickLoadBtn">
              <img :src="loadBtnImg" id="load-Info-btn-decorate">
              {{ loadBtnText }}
            </button>
            <button id="change-info-btn" @click="">修改资料</button>
          </div>
        </div>
        <div id="article-card-list">
                  <article-list/>

        </div>

      </div>
    </div>
    <GoTopBtn />
  </main>

</template>

<style scoped>
#load-Info-btn {
  border: none;
  background-color: transparent;
  font-size: 15px;
  padding: 5px;
  cursor: pointer;
  color: #8493a5;
  position: relative;
  transition: background-color 0.1s;
  bottom: 5%;
  left: 5%;

  & #load-Info-btn-decorate {
    width: 15px;
    top: 20%;
  }
}

#article-card-list {
  background-color: whitesmoke;
  margin-top: 10px;
}
#profile-img-container {
  height: 200px;
  background-color: rgb(245, 245, 24,10%);

  & #load-profile-img-btn {
    background-color: transparent;
    position: absolute;
    top: 121px;
    left: 1180px;
    font-size: 17px;
    border-radius: 4px;
    padding: 4px 8px;
  }
    & #load-profile-img-btn:hover {
      background-color: rgba(0,0,0,0.1);
  }
}

#avatar-container {
  position: absolute;
  width: 140px;
  height: 140px;
  left: 13%;
  top: 28%;
    box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
}

#user-info-container {
  box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
  min-height: 100px;

  flex-direction: column;
  background-color: white;
  & h2 {
    position: absolute;
    top: 272px;
    left: 363px;
  }

  & #load-Info-btn {
    position: relative;
    margin-left: 150px;
    transition: 0.1s;
  }

  & #avatar-container {
    border-radius: 5px;
    display: flex;
    position: absolute;
    top: 200px;
    left: 198px;
    & #avatar-img-container {
      margin: 1%;
      width: 98%;
      border-radius: 5px;
      overflow: hidden;
      background-image: url("@/assets/avatar.jpg");
      background-size: cover;
      cursor: pointer;
    }

  }

  & #change-info-btn {
    margin-left: 700px;
    margin-bottom: 15px;
    font-size: 17px;
    padding: 6px 8px;
    background-color: transparent;
    border-radius: 4px;
  }

  & #change-info-btn:hover {
    background-color: rgba(0,0,0,0.1);
  }
}

#user-info {
  overflow: hidden;
  transition: height 300ms ease-out 0s;
  height: 0;
  padding-top: 60px;

  & p {
    margin-left: 200px;
  }
}

#user-profile-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 1500px;
  & #user-profile {
    width: 80%;

  }
}

button {
  cursor: pointer;
  transition: 0.1s;
}


</style>