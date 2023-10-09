<script setup>
import like from "@/assets/like.svg";
import avatar from '@/assets/avatar.jpg';
import {reactive, ref} from "vue";
import {useRoute, useRouter} from "vue-router";
import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import GoTopBtn from "@/components/SubComponents/GoTopBtn.vue";
import markdownIt from "@kangc/v-md-editor/es/utils/markdown-it";
import MarkdownItHightlightJS from 'markdown-it-highlightjs';

const router = useRouter();
const route = useRoute();
const md = new markdownIt({}).use(MarkdownItHightlightJS);

const info = reactive({
  articleTitle: "这是文章的标题",
  category: "板块1",
  avatar: avatar,
  username: "cc",
  createTime: "1999-01-01"
});
const articleContent = ref(md.render("# 1 \n \`\`\`C \n printf(\"asd\\n\"); \`\`\` \n asd \n"));


</script>

<template>
  <header>
    <NavigationBar></NavigationBar>
  </header>
  <div id="article-show-container">
    <div id="article-show-article-container">
      <div id="article-show-userinfo-container">
        <h1>{{ info.articleTitle }}</h1>
        <div>
          <div>
            <img :src="avatar" alt="">
            <span>{{ info.username }}</span>
            <span>发表时间:{{ info.createTime }}</span>
            <span>所属板块:{{ info.category }}</span>
          </div>
        </div>
      </div>
      <div id="article-show-content-container">
        <div v-html="articleContent"></div>
      </div>
      <div id="article-show-like-container">
        <button><img :src="like" alt="">点 赞</button>
      </div>
    </div>
    <div id="comment-container">

    </div>
  </div>
  <GoTopBtn/>
</template>

<style scoped>

#article-show-container {
  position: relative;
  width: 1100px;
  height: 100px;
  left: 13%;

  & > div {
    margin-bottom: 10px;
    background-color: white;
    border-radius: 10px;
    border: 1px solid #e4e7ed;
    box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
  }


  & #article-show-article-container {

    display: flex;
    flex-direction: column;

    & #article-show-content-container {
      margin-top: 30px;
      margin-bottom: 30px;
      padding-left: 30px;
      padding-right: 100px;
      position: relative;
      width: 80%;
      left: 4%;
      border-left: 2px solid #e4e7ed;
      border-right: 2px solid #e4e7ed;

    }


    & #article-show-like-container {
      margin-top: 20px;
      position: relative;
      width: 80%;
      left: 10%;
      border-top: 1px solid #e4e7ed;
      height: 100px;
      display: flex;
      justify-content: center;
      align-items: center;
      & > button {
        display: flex;
        background-color: #c45656;
        color: white;
        padding: 8px 16px;
        border-radius: 5px;
        font-size: 15px;
        justify-content: center;
        align-items: center;
        & img {
          margin-right: 10px;
          width: 26px;
        }
        transition: 0.1s;
        cursor: pointer;
        &:hover {
          background-color: #d35e5e;
        }
      }
    }

    & #article-show-userinfo-container {
      display: flex;
      justify-content: center;
      align-items: center;
      padding-bottom: 10px;
      border-bottom: 4px solid black;
      flex-direction: column;
      position: relative;

      & > div {
        position: relative;

        & > div {
          position: relative;
          display: flex;
          align-items: center;
          width: 100%;

          & > img {
            border: 2px solid #e4e7ed;
            width: 40px;
            margin-right: 8px;
            border-radius: 8px;
            box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
          }

          & span:nth-child(3) {
            position: absolute;
            width: 200px;
            left: 200px;
            color: #818283;
          }

          & span:nth-child(4) {
            position: absolute;
            width: 150px;
            left: 400px;
            color: #818283;
          }
        }
      }
    }
  }

  & #comment-container {
    height: 400px;
  }
}

</style>