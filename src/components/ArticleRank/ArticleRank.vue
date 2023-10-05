<script setup>

import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import GoTopBtn from "@/components/SubComponents/GoTopBtn.vue";
import ArticleList from "@/components/ArticleList/ArticleList.vue";
</script>

<template>
  <header>
    <NavigationBar />
  </header>
  <div id="rank-container">
    <div id="day-select"></div>
    <div id="week-select"></div>
    <div id="month-select"></div>
    <ArticleList />
  </div>
  <GoTopBtn/>
</template>

<style scoped>
#rank-container {
  position: absolute;
  min-width: 1000px;
  left: 250px;
}
</style>