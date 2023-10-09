<script setup>

import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import GoTopBtn from "@/components/SubComponents/GoTopBtn.vue";
import ArticleList from "@/components/ArticleList/ArticleList.vue";
import {ref} from "vue";

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
    <NavigationBar />
  </header>
  <div id="rank-container">
    <div id="day-select"></div>
    <div id="week-select"></div>
    <div id="month-select"></div>
    <ArticleList :card-list="cardList" :page-size="10"/>
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