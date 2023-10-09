<script setup>
import { ref ,reactive,onMounted} from "vue";
import {useRoute} from "vue-router";
import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import GoTopBtn from "@/components/SubComponents/GoTopBtn.vue";
import ArticleList from "@/components/ArticleList/ArticleList.vue";
const route = useRoute();
const q = ref(route.query.q);

const searchResult = reactive([]);


onMounted(()=>{
})


</script>

<template>
  <header>
    <NavigationBar />
  </header>
  <div id="search-result-container">
    <p>关于搜索"<span>{{q}}</span>"的结果共有<span>{{searchResult.length}}</span>条:</p>
    <div>
      <ArticleList :card-list="searchResult" :page-size="10"></ArticleList>
    </div>
  </div>
  <GoTopBtn />
</template>


<style scoped>
#search-result-container {
  position: relative;
  border-radius: 20px;
  width: 1100px;
  left: 200px;
  height: 400px;
  border: 1px solid #e4e7ed;
  background-color: white;
  & p:nth-child(1) {
    position: relative;
    margin-left: 6px;
    padding-left: 40px;
    padding-bottom: 10px;
    font-size: 24px;
    width: 95%;
    border-bottom: 3px solid #e4e7ed;
    & span {
      color: #c45656;
      font-size: 34px;
      margin: 4px;
    }
  }
}

</style>