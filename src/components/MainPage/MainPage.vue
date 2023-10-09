<script setup>
import {ref} from 'vue';
import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import ArticleList from "@/components/ArticleList/ArticleList.vue";
import GoTopBtn from "@/components/SubComponents/GoTopBtn.vue";



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
  <div id="article-list-warp">
    <ArticleList :card-list="cardList" :page-size="10" />
  </div>
  <GoTopBtn />
</template>

<style scoped>
#article-list-warp {
  position: absolute;
  width: 1100px;
  left: 200px;
}
</style>