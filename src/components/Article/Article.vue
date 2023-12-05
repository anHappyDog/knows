<script setup>
import { ref, onBeforeMount, computed } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const id = ref(route.params.id);
const cover = ref(null);
const title = ref("");
const content = ref("");
const author = ref("");
const author_avatar = ref("");
const created_time = ref("");
const comments = ref([]);
const commentContent = ref("");
const isCommentting = ref(false);
const liked = ref(false);
const likes = ref(0);
const isAuthor = ref(false);
const getArticle = async function () {
  try {
    const res = await axios.get(
      axios.defaults.baseURL + "/api/article/" + id.value
    );
    if (res.data.status == 0) {
      title.value = res.data.data.title;
      content.value = res.data.data.content;
      author.value = res.data.data.author;
      author_avatar.value = res.data.data.author_avatar;
      created_time.value = res.data.data.created_time;
      cover.value = res.data.data.cover;
      liked.value = res.data.data.liked;
      isAuthor.value = res.data.data.isAuthor;
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const onClickLikeBtn = async function () {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/like", {
      article_id: id.value,
    });
    if (res.data.status === 0) {
      console.log("点赞成功");
      fetchLikes();
      liked.value = true;
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const onClickUnLikeBtn = async function () {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/unlike", {
      article_id: id.value,
    });
    if (res.data.status === 0) {
      console.log("点赞取消成功");
      fetchLikes();
      liked.value = false;
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};
const fetchLikes = async function () {
  try {
    const res = await axios.get(axios.defaults.baseURL + "/api/likes", {
      params: {
        article_id: id.value,
      },
    });
    if (res.data.status === 0) {
      likes.value = res.data.likes;
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const onClickCommentBtn = function () {
  isCommentting.value = true;
};

const onClickCommentBackBtn = function () {
  isCommentting.value = false;
  commentContent.value = "";
};

const onClickCommentReleaseBtn = async function () {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/newComment", {
      article_id: id.value,
      content: commentContent.value,
    });
    if (res.data.status === 0) {
      console.log("评论成功");
      onClickCommentBackBtn();
      fetchComments();
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const onClickDeleteCommentBtn = async function (comment_id) {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/delComment", {
      comment_id: comment_id,
    });
    if (res.data.status === 0) {
      console.log("删除评论成功");
      fetchComments();
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const fetchComments = async function () {
  try {
    const res = await axios.get(axios.defaults.baseURL + "/api/comments", {
      params: {
        article_id: id.value,
      },
    });
    if (res.data.status === 0) {
      comments.value = res.data.data;
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const onClickDeleteArticleBtn = async function() {

};

onBeforeMount(() => {
  getArticle();
  fetchLikes();
  fetchComments();
});
</script>

<template>
  <h1>{{ title }}</h1>
  <p>ArticleId:{{ id }}</p>
  <p>Author:{{ author }}</p>
  <p>avatar:{{ author_avatar }}</p>
  <p>cover:{{ cover }}</p>
  <p>{{ content }}</p>
  <p>点赞数:{{ likes }}</p>
  <button @click="onClickCommentBtn">评论</button>
  <button v-if="liked" @click="onClickUnLikeBtn">取消点赞</button>
  <button v-else @click="onClickLikeBtn">点赞</button>
  <button v-if="isAuthor" @click="onClickDeleteArticleBtn">删除文章</button>
  <div v-if="isCommentting">
    <button @click="onClickCommentBackBtn">返回</button>
    <textarea v-model="commentContent"></textarea>
    <button @click="onClickCommentReleaseBtn">发布</button>
  </div>
  <h2>Comments:</h2>
  <div v-for="comment in comments">
    <div>
      <p>{{ comment.content }}</p>
      <p>{{ comment.created_time }}</p>
      <p>{{ comment.commentUser }}</p>
      <p>{{ comment.user_avatar }}</p>
      <button v-if="comment.canDelete" @click="onClickDeleteCommentBtn(comment.id)">
        删除
      </button>
    </div>
  </div>
</template>

<style scoped></style>
