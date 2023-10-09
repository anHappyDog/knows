<script setup>
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router";

const searchKeyWord = ref("");
const router = useRouter();
const fixDiv = ref();
const scrollHeader = ref();

onMounted(() => {
  window.addEventListener("scroll", () => {
    scrollHeader.value.style.left = `${-window.scrollX}px`;
  })
})

const onClickFriend = function () {
  router.push("/friendBoard");
}

const onClickPublishArticle = function () {
  router.push("/writeArticle");
}

const goToMainPage = function () {
  router.push("/mainPage");
}

const goToCategoryPage = function () {
  router.push("/category");
}

const gotoUserProfile = function () {
  router.push("/userProfile");
}

const gotoTaskBoard = function () {
  router.push("/taskBoard");
}

const gotoArticleRank = function () {
  router.push("/articleRank");
}

const onClickSearch = function () {
  router.push({path: "/searchResult", query: {q: searchKeyWord.value}})
}

</script>

<template>
  <div class="navigation-scroll-container">
    <div ref="fixDiv" id="navigation-bar-container">
      <div ref="scrollHeader" id="navigation-bar">
        <div class="just-decorate-for-header"></div>
        <ul id="navigation-choice-list">
          <li>
            <button class="navigation-choice" @click="goToMainPage">主界面</button>
          </li>
          <li>
            <button class="navigation-choice" @click="goToCategoryPage">板块</button>
          </li>
          <li>
            <button class="navigation-choice" @click="gotoUserProfile">个人中心</button>
          </li>
          <li>
            <button class="navigation-choice" @click="gotoTaskBoard">任务</button>
          </li>
          <li>
            <button class="navigation-choice" @click="gotoArticleRank">排行</button>
          </li>
        </ul>
        <div id="search-container">
          <input @keydown.enter="onClickSearch" v-model="searchKeyWord" type="text" placeholder="请搜索"
                 id="search-edit">
          <button title="搜索按钮" @click="onClickSearch" id="navigation-search-btn"></button>
        </div>
        <button id="publish-article" @click="onClickPublishArticle">发表文章</button>
        <button title="好友按钮" @click="onClickFriend" id="navigation-friend-btn"></button>
        <div class="just-decorate-for-header"></div>
      </div>
    </div>
  </div>
  <div id="navigation-margin-empty-div"></div>
</template>

<style scoped>
* {
  font-family: "Microsoft YaHei UI", serif;
}


#navigation-margin-empty-div {
  margin-bottom: 70px;
}

#navigation-bar-container {
  position: fixed;
  top: 0;
  left: 0;
  min-width: 1500px;
  width: 100%;
  margin-bottom: 10px;
  background-color: white;
  z-index: 10;
}

#navigation-bar {
  position: relative;
  width: 100%;
  height: 54px;
  top: 0;
  box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
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

    & #navigation-search-btn {
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
    cursor: pointer;
  }

  & #navigation-friend-btn {
    width: 32px;
    height: 32px;
    margin-left: 16px;
    background-image: url("@/assets/friend.svg");
    border-radius: 50%;
    background-size: cover;
    border: none;
    padding-left: 16px;
    cursor: pointer;
  }

  & #publish-article:hover {
    background-color: wheat;

  }
}

.just-decorate-for-header {
  margin: 0 40px;
  width: 15%;
  border: 2px solid black;
}

.navigation-choice {
  border: none;
  background-color: transparent;
  font-size: 16px;
  cursor: pointer;
}

</style>