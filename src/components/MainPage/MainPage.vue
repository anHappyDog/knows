<script setup>

import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import ArticleList from "@/components/ArticleList/ArticleList.vue";
import GoTopBtn from "@/components/SubComponents/GoTopBtn.vue";
</script>

<template>
  <header>
    <NavigationBar/>
  </header>
  <div id="article-list-warp">
    <ArticleList />
  </div>
  <GoTopBtn />
</template>

<style scoped>
#article-list-warp {
  position: absolute;
  width: 1200px;
  left: 150px;
}
</style>