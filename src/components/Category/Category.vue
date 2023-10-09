<script setup>
import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import {ref, onMounted, onUnmounted} from 'vue'
import GoTopBtn from "@/components/SubComponents/GoTopBtn.vue";
import downArrow from "@/assets/downArrow.svg";
import upArrow from "@/assets/upArrow.svg";
import CategoryCard from "@/components/Category/CategoryCard.vue";

const showBtnImg = ref(downArrow);
let height = 0;
let descriptionArea;
onMounted(() => {
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
    <CategoryCard v-for="(item,index) in categoryList" :count="index" :category-description="item.categoryDescription"
                  :article-count="item.articleCount" :category-name="item.categoryName" />
  </div>
  <GoTopBtn/>
</template>

<style scoped>


#category-board {
  position: relative;
  width: 1000px;
  left: 250px;
  height: 100%;
}

</style>