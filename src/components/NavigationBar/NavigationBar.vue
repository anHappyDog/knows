<script setup>
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router";

const searchContent = ref("");
const router = useRouter();


onMounted(() => {
})

const onClickPublishArticle = function () {

}

const goToMainPage = function () {

}

const goToCategoryPage = function () {

}

const gotoUserProfile = function () {

}

const gotoTaskBoard = function () {

}

const gotoArticleRank = function () {

}

const onClickSearch = function () {
  console.log(searchContent.value);
}

</script>

<template>
  <div id="navigation-bar-container">
    <header id="navigation-bar">
      <div class="just-decorate-for-header"></div>
      <ul id="navigation-choice-list">
        <li><button class="navigation-choice" @click="goToMainPage">主界面</button></li>
        <li><button class="navigation-choice" @click="goToCategoryPage">板块</button></li>
        <li><button class="navigation-choice" @click="gotoUserProfile">个人中心</button></li>
        <li><button class="navigation-choice" @click="gotoTaskBoard">任务</button></li>
        <li><button class="navigation-choice" @click="gotoArticleRank">排行</button></li>
      </ul>
      <div id="search-container">
        <input @keydown.enter="onClickSearch" v-model="searchContent" type="text" placeholder="请搜索" id="search-edit">
        <button id="search-btn" @click="onClickSearch"></button>
      </div>
      <button id="publish-article" @click="onClickPublishArticle">发表文章</button>
      <div class="just-decorate-for-header"></div>
    </header>
  </div>

</template>

<style scoped>
* {
  font-family: "Microsoft YaHei UI", serif;
}

#navigation-bar-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
}

#navigation-bar {
  width: 100%;
  top: 0;
  border: 2px solid black;
  z-index: 100;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;

  & #navigation-choice-list {
    list-style-type: none;
    display: flex;

    & li {
      padding-right: 12px;
    }
  }

  & #search-container {
    display: flex;
    border: thin inset black;
    border-radius: 999px;
    padding: 8px;
    -webkit-font-smoothing: subpixel-antialiased;
    background-color: #f5f5f5;
    margin: 0 10px;
    justify-content: center;

    & input {
      outline: none;
      border: none;
      font-size: 16px;
      padding-left: 8px;
      background-color: transparent;
    }

    & button {
      background-image: url("@/assets/search.svg");
      background-size: cover;
      border: none;
      padding-left: 16px;
    }

    & button:hover {
      cursor: pointer;
    }

  }

  & #publish-article {
    padding: 8px 16px;
    border: 1px solid black;
    border-radius: 999px;
    transition: 0.05s;
    font-size: 16px;
  }

  & #publish-article:hover {
    background-color: wheat;

  }
}

.just-decorate-for-header {
  margin: 0 40px;
  width: 20%;
  border: 2px solid black;
}

.navigation-choice {
  border: none;
  background-color: transparent;
  font-size: 16px;
  cursor: pointer;
}

</style>