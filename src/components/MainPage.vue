<script setup>
import { ref, onBeforeMount,provide } from 'vue';
import router from '../router';
const userid = ref('');
const keyword = ref('');
provide('keyword', keyword);
onBeforeMount(() => {
  userid.value = localStorage.getItem('token');
})

const onClickWriteArticleBtn = function () {
  router.push('/main/newArticle');
}
const onClickArticleBtn = function () {
  router.push('/main/articles');
}
const onClickCategoryBtn = function () {
  router.push('/main/categories');
}

const onClickUserProfileBtn = function () {
  router.push(`/main/user/${userid.value}`);
}
const onClickFeedBackBtn = function () {
  router.push('/main/feedbacks');
}

const onSearchArticle = function () {
    router.push('/main/articles');
}
</script>

<template>
  <div>
    <v-app-bar app color="white" dark id="test">
      <v-toolbar-title>cc的混乱空间</v-toolbar-title>
      <v-spacer />
      <v-text-field class="mt-4" @keyup.enter="onSearchArticle"  v-model="keyword" label="搜索" variant="underlined" />
      <v-spacer />
      <v-btn @click="onClickArticleBtn">
        文章
      </v-btn>
      <v-btn @click="onClickCategoryBtn">
        板块
      </v-btn>
      <v-btn @click="onClickUserProfileBtn">
        用户中心
      </v-btn>
      <v-btn @click="onClickFeedBackBtn">
        反馈
      </v-btn>
      <v-btn @click="onClickWriteArticleBtn" variant="outlined" id="write-article-btn">
        写文章
      </v-btn>
    </v-app-bar>

    <v-main>
      <div id="main-container">
        <router-view />
      </div>
    </v-main>

  </div>
</template>

<style scoped>
#main-container {
  position: relative;
  width: 70%;
  left: 15%;
}

#write-article-btn {
  margin-left: 20px;
  margin-right: 40px;
}
</style>
