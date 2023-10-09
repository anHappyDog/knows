<script setup>
import {ref, reactive, onMounted, watch} from 'vue'
import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import UploadImg from "@/assets/uploadImg.svg";
import UploadVideo from "@/assets/uploadVideo.svg";
import UploadDialog from "@/components/WriteArticle/UploadDialog.vue";
import UploadImgBoard from "@/components/WriteArticle/UploadImgBoard.vue";
import MarkdownIt from "@kangc/v-md-editor/es/utils/markdown-it";
import MarkdownItVideo from 'markdown-it-video';
import MarkdownItHightlightJS from 'markdown-it-highlightjs';
import '@/assets/code.css';

const choiceContainer = ref();
const categoryChoice = ref({});
const categoryOptions = ref([{value: "板块1", label: "板块1"},
  {value: "板块2", label: "板块2"},
  {value: "板块3", label: "板块3"},
  {value: "板块4", label: "板块4"},]);
const inputArea = ref(null);
const inputText = ref('');
const dialogComponent = ref(UploadImg);

const md = new MarkdownIt({}).use(MarkdownItHightlightJS, {inline: true, auto: true});
MarkdownItVideo(md);
onMounted(() => {
  document.addEventListener("scroll", () => {
    choiceContainer.value.style.left = `${-window.scrollX}px`;
  });

})

const autoResize = function () {
  inputArea.value.style.height = "auto";
  inputArea.value.style.height = `${inputArea.value.scrollHeight}px`;
}
const isDialogVisible = ref(false);
const onClickUploadImgBtn = function () {
  dialogComponent.value = UploadImgBoard;
  isDialogVisible.value = true;

}
const articlePreview = ref();
const onClickUploadVideoBtn = function () {

  isDialogVisible.value = true;
}

</script>

<template>
  <header>
    <NavigationBar/>
  </header>
  <div id="markdown-func-choice-container">
    <button class="write-article-function-btn" id="markdown-upload-img-btn" @click="onClickUploadImgBtn"><img
        :src="UploadImg" alt=""></button>
    <button class="write-article-function-btn" id="markdown-upload-video-btn" @click="onClickUploadVideoBtn"><img
        :src="UploadVideo" alt=""></button>
  </div>
  <div id="write-article-container">
    <div id="markdown-write-container">
      <input id="article-header-input" type="text" placeholder="文章标题">
      <textarea @input="autoResize" ref="inputArea" v-model="inputText" id="article-content-input"
                placeholder="文章内容"></textarea>
    </div>
    <div id="article-preview-container">
      <div ref="articlePreview" v-html="md.render(inputText)"></div>
    </div>
  </div>
  <div style="margin-bottom: 100px"></div>
  <div ref="choiceContainer" id="write-choice-container">
    <div id="write-choice-wrap">
      <el-select :popper-append-to-body="false" v-model="categoryChoice" placeholder="文章所属板块">
        <el-option
            v-for="item in categoryOptions"
            :value="item.value"
            :key="item.value"
            :label="item.label"
        ></el-option>
      </el-select>
      <span id="char-count-show">当前字数为:{{ inputText.length }}</span>
      <button id="tmp-store-btn">暂存</button>
      <button id="publish-btn">发布</button>
      <div id="write-choice-wrap-decorate-line"></div>
    </div>

  </div>
  <UploadDialog v-model:visible="isDialogVisible"/>
</template>

<style scoped lang="less">
#article-preview-container {

  background-color: white;
  border: 1px solid #e4e7ed;
  border-radius: 10px;
  padding: 20px;
  display: flex;
  justify-content: center;

  & > div {
    overflow-y: hidden;
    padding-left: 10px;
    width: 98%;
    max-width: 98%;
    border-left: 2px solid black;
    white-space: pre-wrap;
    word-break: break-all;
    word-wrap: break-word
  }
}

.el-select {
  position: absolute;
  left: 8%;
}

#write-choice-wrap {
  min-width: 800px;
  position: relative;
  display: flex;
  align-items: center;

  & #write-choice-wrap-decorate-line {
    position: absolute;
    border: 2px solid black;
    width: 80%;
    left: 90%;
  }
}


#article-content-input {
  position: relative;
  background-color: transparent;
  border: none;
  resize: none;
  width: 98%;
  font-size: 19px;
  padding: 10px;
  min-height: 400px;
  height: auto;
  outline: none;
}

#markdown-func-choice-container {
  border: 2px solid #e4e7ed;
  background-color: white;
  border-radius: 10px;
  height: 50px;
  margin-bottom: 14px;
  box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
  display: flex;
  align-items: center;
  padding-left: 10px;
  position: relative;
  width: 1000px;
  left: 250px;

  .write-article-function-btn {
    margin: 4px;
    padding: 4px 6px;
    border: none;
    background-color: transparent;
    border-radius: 4px;
    transition: 0.1s;
    display: flex;
    cursor: pointer;

    & img {
      width: 28px;
      color: black;
    }
  }

  .write-article-function-btn:hover {
    background-color: rgb(90, 150, 222);
  }

}

#write-article-container {
  position: relative;
  width: 1500px;
  display: flex;

  & > div {
    min-height: 200px;
    width: 47%;
    margin: 10px;
    border: 1px solid #e4e7ed;
    box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
  }
}

#markdown-write-container {
  height: auto;
  border-radius: 10px;
  background-color: white;

  & #article-header-input {
    outline: none;
    margin-left: 10px;
    width: 93%;
    font-size: 44px;
    background-color: transparent;
    border: none;
    border-bottom: 2px solid black;
    box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
    padding: 10px 10px 10px 20px;
  }
}

#write-choice-container {
  position: fixed;
  bottom: 0;
  height: 60px;
  border: 2px solid #e4e7ed;
  box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
  background-color: white;
  z-index: 10;
  display: flex;
  align-items: center;
  width: 100%;

  & button {
    cursor: pointer;
  }

  & > div:nth-child(2) {
    width: 40%;
    border: 2px solid black;
  }

  & #tmp-store-btn {
    position: absolute;
    font-size: 18px;
    padding: 6px 12px;
    border-radius: 4px;
    width: 80px;
    display: block;
    left: 60%;
    transition: 0.1s;
    background-color: #ffffff;

    &:hover {
      background-color: rgba(227, 227, 227, 1);
    }
  }

  & #char-count-show {
    position: absolute;
    left: 40%;
    margin: 20px;
    user-select: none;
  }

  & #publish-btn {
    position: absolute;
    font-size: 18px;
    padding: 6px 12px;
    border-radius: 4px;
    left: 72%;
    transition: 0.1s;
    background-color: rgb(56, 141, 229);
    color: white;
    width: 80px;

    &:hover {
      background-color: rgba(64, 158, 255, 78);
    }
  }

}

#markdown-write-container {
  margin-bottom: 14px;
}

.hljs {
  border-radius: 10px;
}
</style>