<script setup>
import {computed, ref,watch} from "vue";

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

const pageSize = ref(10);
const curPage = ref(1);
const pageCount = computed(() => {
  return cardList.value.length / pageSize.value;
});
const totalCard = computed(() => {
  return cardList.value.length;
});

watch(curPage,(value, oldValue, onCleanup)=>{
  console.log(value);
});

const showCards = computed(()=>{
 return cardList.value.slice((curPage.value - 1) * pageSize.value,curPage.value * pageSize.value);
});

const onPageChanged = function (val) {
  console.log(val);
  curPage.value = val;
}


</script>

<template>
  <el-card v-for="item in showCards" :key="item.id">
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
                   @current-change = "onPageChanged"
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

el-card {
  display: block;

  width: 95%;
  text-align: center;
  border-bottom: 2px solid #f5f5f5;
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

.like-count,.comment-count {
  margin-right: 24px;
}
.category {
  position: relative;
  left: 70%;
}

</style>