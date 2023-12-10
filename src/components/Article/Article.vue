<script setup>
import { ref, onMounted, onBeforeUnmount,computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import alertStore from '../../alertStore';
import axios from "axios";
const methods = alertStore.methods;
const router = useRouter();
const route = useRoute();
const id = ref(route.params.id);
const comments = ref(null);
const commentContent = ref("");
const isCommentting = ref(false);
const articleInfo = ref(null);
const likes = ref(0);
const commentForm = ref(null);
const liked = ref(false);
const commentPage = ref(1);
const maxComentPageSize = 8;
const isAuthor = ref(false);
const slicedComments = computed(() => {
  return comments.value.slice(
    (commentPage.value - 1) * maxComentPageSize,
    commentPage.value * maxComentPageSize
  );
});
const pages = computed(() => {
  return Math.ceil(comments.value.length / maxComentPageSize);
});
const getArticle = async function () {
  try {
    const res = await axios.get(
      axios.defaults.baseURL + "/api/article/" + id.value
    );
    if (res.data.status == 0) {
      articleInfo.value = res.data.data;
      liked.value = res.data.data.liked;
      likes.value = res.data.data.likes;
      isAuthor.value = res.data.data.isAuthor;
    } else {
      methods.addAlert({
        type: "error",
        message: res.data.message,
        timeout: 3000
      });
    
    }
  } catch (err) {
    methods.addAlert({
        type: "error",
        message: err.toString(),
        timeout: 3000
      });
  }
};

const onClickLikeBtn = async function () {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/like", {
      article_id: id.value,
    });
    if (res.data.status === 0) {
      methods.addAlert({
        type:"success",
        message:"点赞成功",
        timeout: 3000
      });
      fetchLikes();
      liked.value = true;
    } else {
      methods.addAlert({
        type: "error",
        message: res.data.message,
        timeout: 3000
      });
    
    }
  } catch (err) {
    methods.addAlert({
        type: "error",
        message: err.toString(),
        timeout: 3000
      });
  }
};

const onClickUnLikeBtn = async function () {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/unlike", {
      article_id: id.value,
    });
    if (res.data.status === 0) {
      methods.addAlert({
        type:"success",
        message:"点赞取消成功",
        timeout: 3000
      });
      fetchLikes();
      liked.value = false;
    } else {
      methods.addAlert({
        type: "error",
        message: res.data.message,
        timeout: 3000
      });
    }
  } catch (err) {
    methods.addAlert({
        type: "error",
        message: err.toString(),
        timeout: 3000
      });
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
      methods.addAlert({
        type: "error",
        message: res.data.message,
        timeout: 3000
      });
    }
  } catch (err) {
    methods.addAlert({
        type: "error",
        message: err.toString(),
        timeout: 3000
      });
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
  const isValid = await commentForm.value.validate();
  if (!isValid.valid) {
    methods.addAlert({
        type: "warning",
        message: "请检查你的输入",
        timeout: 3000
      });
    return;
  }
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/newComment", {
      article_id: id.value,
      content: commentContent.value,
    });
    if (res.data.status === 0) {
      methods.addAlert({
        type: "success",
        message: "评论成功",
        timeout: 3000
      });
      onClickCommentBackBtn();
      fetchComments();
    } else {
      methods.addAlert({
        type: "error",
        message: res.data.message,
        timeout: 3000
      });
    }
  } catch (err) {
    methods.addAlert({
        type: "error",
        message: err.toString(),
        timeout: 3000
      });
  }
};

const onClickDeleteCommentBtn = async function (comment_id) {
  try {
    console.log(comment_id);
    const res = await axios.post(axios.defaults.baseURL + "/api/delComment", {
      comment_id: comment_id,
    });
    if (res.data.status === 0) {
      methods.addAlert({
        type: "success",
        message: "删除评论成功",
        timeout: 3000
      });
      fetchComments();
    } else {
      methods.addAlert({
        type: "error",
        message: res.data.message,
        timeout: 3000
      });
    }
  } catch (err) {
    methods.addAlert({
        type: "error",
        message: err.toString(),
        timeout: 3000
      });
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
      methods.addAlert({
        type: "error",
        message: res.data.message,
        timeout: 3000
      });
    }
  } catch (err) {
    methods.addAlert({
        type: "error",
        message: err.toString(),
        timeout: 3000
      });
  }
};

const onClickDeleteArticleBtn = async function () {
  try{
    const res = await axios.post(axios.defaults.baseURL + "/api/deleteArticle", {
      article_id: id.value,
    });
    methods.addAlert({
        type: "success",
        message: "删除文章成功",
        timeout: 3000
      });
    router.push("/main/articles");
  } catch(err) {
    methods.addAlert({
        type: "error",
        message: err.toString(),
        timeout: 3000
      });
  }
};
const goToCategory = function (id) {
  router.push("/main/category/" + id);
};
const goToUserProfile = function (id) {
  router.push("/main/user/" + id);
};

const commentRules = [
  (v) => !!v || "评论不能为空",
  (v) => (v && v.length <= 100) || "评论不能超过100个字符",
];

const onClickUpdateBtn = function () {
  router.push("/main/article/" + id.value + "/update");
};

onMounted(() => {
  getArticle();
  fetchLikes();
  fetchComments();
});
onBeforeUnmount(() => {
});
</script>

<template>
  <Transition>
    <v-container v-if="articleInfo !== null && comments !== null">
      <v-container class="pa-0 article-detail-container">
        <v-container class="pa-0 border border-2 rounded-sm mt-2 mb-3 elevation-2">
          <v-img cover height="120" :src="axios.defaults.baseURL + articleInfo.cover"></v-img>
          <v-container class="d-flex flex-column align-center justify-center">
            <h1>{{ articleInfo.title }}</h1>
            <v-container class="pa-0 d-flex justify-center  align-center">
              <v-btn variant="plain" @click="goToCategory(articleInfo.category_id)">{{ articleInfo.category }}</v-btn>
              <!-- <router-link :to="'/main/category/' + articleInfo.category_id">{{ articleInfo.category }}</router-link> -->
              <div>{{ articleInfo.created_time }}前</div>
            </v-container>

          </v-container>
        </v-container>
      </v-container>
      <v-container class="border border-2 rounded-sm elevation-2 d-flex flex-row align-center justify-center">
        <v-avatar class="cursor-pointer mr-4" size="50" tile>
          <v-img @click="goToUserProfile(articleInfo.author_id)"
            :src="axios.defaults.baseURL + articleInfo.author_avatar"></v-img>
        </v-avatar>
        <v-btn @click="goToUserProfile(articleInfo.author_id)" variant="plain">{{ articleInfo.author }}</v-btn>
      </v-container>
      <v-container class="border boder-2 mt-4 rounded-sm elevation-2">
        <v-md-preview :text="articleInfo.content" />
        <v-divider thickness="3" />
        <v-container class="d-flex max-width align-center justify-center">

          <v-badge :content="likes" class="mr-10">
            <v-btn elevated v-if="!liked"  @click="onClickLikeBtn">点赞</v-btn>
            <v-btn elevated v-else @click="onClickUnLikeBtn">取消点赞</v-btn>
          </v-badge>
          <v-btn class="mr-10" @click="onClickCommentBtn">评论</v-btn>
          <v-btn v-if="isAuthor" @click="onClickDeleteArticleBtn">删除文章</v-btn>
          <v-btn @click="onClickUpdateBtn" v-if="isAuthor" class="ml-4">修改文章</v-btn>
        </v-container>
      </v-container>

      <v-container class="border border-2 rounded-sm elevation-2 mt-2">
          <v-container v-if="isCommentting">
            <v-form @submit.prevent="onClickCommentReleaseBtn" ref="commentForm">
              <v-textarea label="评论" v-model="commentContent" :rules="commentRules" />
              <v-container>
                <v-btn type="submit">发布</v-btn>
                <v-btn @click="onClickCommentBackBtn">返回</v-btn>
              </v-container>
            </v-form>
            <v-divider thickness="2" />
          </v-container>


        <span>所有评论</span>
        <v-divider thickness="2" />
        <v-container v-for="comment in slicedComments" class="cmt-whl-container bl-1">
          <v-container class="d-flex pa-0 mb-2 flex-row align-center justify-start">
            <v-avatar class="cursor-pointer" @click="goToUserProfile(comment.user_id)">
              <v-img :src="axios.defaults.baseURL + comment.user_avatar" /> 
            </v-avatar>
            <v-btn variant="plain" @click="goToUserProfile(comment.user_id)">{{ comment.commentUser }}</v-btn>
            <span>:</span><!-- <span>{{comment.created_time}}前:</span> -->
          </v-container>
          <v-container class="pa-0 ml-2">
            <p>{{ comment.content }}</p>
          </v-container>
          <v-container class="cmt-container d-flex flex-row align-center">
            <p>发布时间：{{ comment.created_time }}</p>
            <v-spacer />
            <v-btn v-if="comment.canDelete"  @click="onClickDeleteCommentBtn(comment.id)" class="mr-4">删除</v-btn>
          </v-container>
        </v-container>
        <v-pagination v-model="commentPage" :length="pages" />
      </v-container>

    </v-container>

  </Transition>





  <!-- <p>avatar:{{ }}</p>
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
  </div> -->
</template>

<style scoped>
.cursor-pointer {
  cursor: pointer;
}
.cmt-container {
  border-top: 1px solid;
}

</style>
