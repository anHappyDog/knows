<script setup>
import { ref, onBeforeMount } from "vue";
import axios from "axios";
const content = ref("");
const cover = ref(null);
const categories = ref([]);
const category_id = ref(null);
const title = ref("");
const fetchCategories = async function () {
  try {
    const res = await axios.get(axios.defaults.baseURL + "/api/categories");
    categories.value = res.data["data"];
  } catch (err) {
    console.log(err.toString());
  }
};
const onClickUploadCoverBtn = async function () {
  try {
    if (cover.value === null) {
      return;
    }
    const formData = new FormData();
    formData.append("cover", cover.value);
    const res = await axios.post(
      axios.defaults.baseURL + "/api/uploadArticleCover",
      formData
    );
    if (res.data.status === 0) {
      console.log("成功上传封面");
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const onClickBackBtn = async function () {
  try {
  } catch (err) {
    console.log(err.toString());
  }
};

const onClickReleseBtn = async function () {
  try {
    if (content.value === "" ) {
        console.log("内容不能为空");
        return;
    } else if (title.value === "") {
        console.log("标题不能为空");
        return;
    } else if (category_id.value === null) {
        console.log("分类不能为空");
        return;
    } else {
        const formData = new FormData();
        if (cover.value !== null) {
            formData.append("cover", cover.value);
        }
        formData.append("content", content.value);
        formData.append("title", title.value);
        formData.append("category_id", category_id.value);
        const res = await axios.post(axios.defaults.baseURL + "/api/newArticle", formData);
        if (res.data.status === 0) {
            console.log("成功发布文章");
        } else {
            console.log(res.data.message);
        }
    }
  } catch (err) {
    console.log(err.toString());
  }
};
const setCover = function (e) {
  cover.value = e.target.files[0];
};

onBeforeMount(() => {
  fetchCategories();
});
</script>

<template>
  <h1>New Article</h1>
  <input type="text" placeholder="title" v-model="title" />
  <input type="file" @change="setCover" />
  <button @click="onClickUploadCoverBtn">上传封面</button>
  <select v-model="category_id">
    <option
      v-for="category in categories"
      :key="category.id"
      :value="category.id"
    >
      {{ category.name }}
    </option>
  </select>
  <button @click="onClickReleseBtn">发布</button>
  <button @click="onClickBackBtn">返回</button>
  <v-md-editor v-model="content" height="400px"></v-md-editor>
</template>

<style scoped></style>
