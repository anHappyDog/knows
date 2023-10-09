<script setup>
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
const cardList = ref([
  {id: 1, title: 'Card 1', header: "asd1", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},
  {id: 2, title: 'Card 2', header: "asd2", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},
  {id: 3, title: 'Card 3', header: "asd3", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},
  {id: 4, title: 'Card 1', header: "asd4", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},
  {id: 5, title: 'Card 2', header: "asd5", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},
  {id: 6, title: 'Card 3', header: "asd6", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},
  {id: 7, title: 'Card 1', header: "asd7", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},
  {id: 8, title: 'Card 2', header: "asd8", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},
  {id: 9, title: 'Card 3', header: "asd9", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},
  {id: 10, title: 'Card 1', header: "asd10", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},
  {id: 11, title: 'Card 2', header: "asd11", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},
  {id: 12, title: 'Card 3', header: "asd12", authorName: "123", publishTime: "2023-01-01", likeCount: 1, commentCount: 1},

]);



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
          <article-list :page-size="10" :card-list="cardList"/>

        </div>

      </div>
    </div>
    <GoTopBtn/>
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
  position: absolute;
  transition: background-color 0.1s;
  bottom: 5%;
  left: 8%;

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
  background-color: rgb(245, 245, 24, 10%);

  & #load-profile-img-btn {
    background-color: transparent;
    position: absolute;
    top: 121px;
    left: 1130px;
    font-size: 17px;
    border-radius: 4px;
    padding: 4px 8px;
  }

  & #load-profile-img-btn:hover {
    background-color: rgba(0, 0, 0, 0.1);
  }
}


#user-info-container {
  box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
  min-height: 100px;
  display: flex;
  flex-direction: column;
  background-color: white;
  position: relative;
  & h2 {
    position: absolute;
    left: 22%;
  }

  & #load-Info-btn {
    position: relative;
    margin-left: 150px;
    transition: 0.1s;
  }

  & #avatar-container {
    width: 140px;
    height: 140px;
    border-radius: 5px;
    display: flex;
    position: absolute;
    left: 50px;
    top: -60px;
    box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
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
    position: absolute;
    left: 16%;
    top: 40px;
  }

  & #change-info-btn:hover {
    background-color: rgba(0, 0, 0, 0.1);
  }
}

#user-info {
  overflow: hidden;
  transition: height 300ms ease-out 0s;
  height: 0;
  padding-top: 60px;
  padding-left: 40px;
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
    width: 70%;

  }
}

button {
  cursor: pointer;
  transition: 0.1s;
}


</style>