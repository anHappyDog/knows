<script setup>
import {ref, onMounted} from 'vue';
import upArrow from "@/assets/upArrow.svg";
import downArrow from "@/assets/downArrow.svg";

const isShow = ref(false);
let height;
let descriptionArea;
const props = defineProps({
  categoryName: {
    type: String,
    required: true,
  },
  articleCount: {
    type: Number,
    required: true,
  },
  categoryDescription: {
    type: String,
    required: true
  },
  count: {
    type: Number,
    required: true
  }
});
onMounted(() => {
  descriptionArea = document.getElementsByClassName("category-description-area")[props.count];
  height = descriptionArea.clientHeight;
  descriptionArea.style.height = "0";
});

const onClickLoad = function () {
  if (isShow.value) {
    isShow.value = false;
    descriptionArea.style.height = "0";
  } else {
    isShow.value = true;
    descriptionArea.style.height = `${height}px`;
  }
}

</script>

<template>
  <el-card>
    <div class="category-card-container">
        <a class="category-name" href="#">{{ categoryName }}</a>
    <span class="article-count">文章数:{{ articleCount }}</span>
    <div class="category-description-area">
      <p class="category-description">{{ categoryDescription }}</p>
    </div>
    <button class="show-category-description-btn" @click="onClickLoad"><img :src="isShow?upArrow:downArrow"
                                                                            alt="decorate-btn">{{ isShow ? "收起板块介绍" : "展开板块介绍" }}
    </button>
    </div>
  </el-card>
</template>

<style scoped>
.category-card-container {

}
.category-description-area {
  overflow: hidden;
  transition: height 300ms ease-out 0s;
}

.show-category-description-btn {
  border: none;
  background-color: transparent;
  display: flex;
  position: relative;
  left: 60%;
  cursor: pointer;
  color: #8493a5;
  & img {
    width: 1em;
    transition: all 750ms;
  }
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