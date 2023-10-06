<script setup>
import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import {ref,onMounted,onUnmounted} from 'vue'
import GoTopBtn from "@/components/SubComponents/GoTopBtn.vue";
import downArrow from "@/assets/downArrow.svg";
import upArrow from "@/assets/upArrow.svg";
const showBtnImg = ref(downArrow);
let height = 0;
let descriptionArea;
onMounted(()=>{
  descriptionArea
});
const categoryList = ref([{
  categoryId: 1,
  categoryName: "asd",
  articleCount: 112,
  categoryDescription: "This is a description of the category"
},
  {
    categoryId: 1,
    categoryName: "asd",
    articleCount: 112,
    categoryDescription: "This is a description of the This is a description of the categoryThis is a description of the categoryThis is a description of the categoryThis is a description of the categoryThis is a description of the categoryThis is a description of the categoryThis is a description of the categoryThis is a description of the category"
  },
  {categoryId: 1, categoryName: "asd", articleCount: 112, categoryDescription: "This is a description of the category"},
  {
    categoryId: 1,
    categoryName: "asd",
    articleCount: 112,
    categoryDescription: "This is a description of the category"
  },
  {categoryId: 1, categoryName: "asd", articleCount: 112, categoryDescription: "This is a description of the category"},
  {
    categoryId: 1,
    categoryName: "asd",
    articleCount: 112,
    categoryDescription: "This is a description of the category"
  },
  {categoryId: 1, categoryName: "asd", articleCount: 112, categoryDescription: "This is a description of the category"},
  {
    categoryId: 1,
    categoryName: "asd",
    articleCount: 112,
    categoryDescription: "This is a description of the category"
  },
  {categoryId: 1, categoryName: "asd", articleCount: 112, categoryDescription: "This is a description of the category"},
  {
    categoryId: 1,
    categoryName: "asd",
    articleCount: 112,
    categoryDescription: "This is a description of the category"
  }
]);


</script>

<template>
  <header>
    <NavigationBar/>
  </header>
  <div id="category-board">
    <el-card v-for="(item,index) in categoryList" :key="index">
      <a class="category-name" href="#">{{ item.categoryName }}</a>
      <span class="article-count">文章数:{{ item.articleCount }}</span>
      <p class="category-description">{{ item.categoryDescription }}</p>
      <button class="show-category-description-btn"><img :src="showBtnImg" alt="decorate-btn">展开板块介绍</button>
    </el-card>
  </div>
  <GoTopBtn/>
</template>

<style scoped>

.show-category-description-btn {
  border : none;
  background-color: transparent;
  display: flex;
  position: relative;
  & img {
     width: 1em;
  }
}

#category-board {
  position: relative;
  width: 1000px;
  left: 250px;
  height: 100%;
}

.category-name {
  font-weight: bold;
  font-size: 26px;
  margin: 0;
}

.article-count {
  position: relative;
  top: 24%;
  left: 10%;
}

.category-description {
  border-top: 2px solid black;
  padding-top: 12px;
  padding-left: 8px;
}

</style>