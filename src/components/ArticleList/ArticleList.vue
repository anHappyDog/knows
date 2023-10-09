<script setup>
import {computed, ref, watch} from "vue";

const props = defineProps({
  cardList: {
    type: Array,
    required: true
  },
  pageSize: {
    type: Number,
    required: true
  },

});


const curPage = ref(1);
const pageCount = computed(() => {
  return props.cardList.length / props.pageSize;
});
const totalCard = computed(() => {
  return props.cardList.length;
});

watch(curPage, (value, oldValue, onCleanup) => {
  console.log(value);
});

const showCards = computed(() => {
  return props.cardList.slice((curPage.value - 1) * props.pageSize, curPage.value * props.pageSize);
});

const onPageChanged = function (val) {
  console.log(val);
  curPage.value = val;
}


</script>

<template>
  <el-card style="padding: 0;" v-for="item in showCards" :key="item.id">
    <div class="author-info">
      <img class="author-avatar" src="@/assets/avatar.jpg">
      <p class="author-name">{{ item.authorName }}</p>
      <span class="publish-time">{{ item.publishTime }}</span>
    </div>
    <div class="article-header"><a href="#">{{ item.header }}</a></div>
    <div class="article-info">
      <span class="like-count">点赞数:{{ item.likeCount }}</span>
      <span class="comment-count">评论数:{{ item.commentCount }}</span>
      <span class="category">所属板块:板块1</span>
    </div>
  </el-card>
  <div id="pagination-wrap">
    <el-pagination id="pagination"
                   :page-size="pageSize"
                   :page-count="pageCount"
                   layout="prev,pager,next"
                   :total="totalCard"
                   @current-change="onPageChanged"
    />
  </div>

</template>

<style scoped>

#pagination-wrap {
  display: flex;
  justify-content: center;
  background: white;
  margin: 8px 8px 18px;
}


.author-info {
  display: flex;
  align-items: center;
}

.article-info {
  display: flex;
  color: #8493a5;
}

.author-avatar {
  display: inline;
  position: relative;
  width: 44px;
  border-radius: 2px;
  box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
  margin-top: 14px;
  cursor: pointer;
}

.author-name {
  padding-left: 8px;
  font-size: 18px;
  font-weight: bold;
}

.article-header {
  display: flex;

  & a {
    margin: 2px 8px 4px 4px;
    padding-left: 36px;
  }

  font-size: 28px;
  text-decoration-line: underline;
  margin-bottom: 6px;
}

.publish-time {
  position: relative;
  left: 80%;
}

.like-count, .comment-count {
  margin-right: 60px;
}

.category {
  position: relative;
  left: 60%;
}

</style>