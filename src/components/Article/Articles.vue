<script setup>
import { ref, onBeforeMount } from "vue";
import axios from "axios";
import router from "../../router";
const articles = ref([]);

const getArticles = async function () {
  try {
    const res = await axios.get(axios.defaults.baseURL + "/api/articles");
    articles.value = res.data["data"];
  } catch (err) {
    console.log(err.toString());
  }
};
onBeforeMount(getArticles);
</script>

<template>
  <h1>Articles</h1>
  <div>
    <div v-for="article in articles" :key="article.id">
      <router-link :to="'/main/article/' + article.id">
        <h2>{{ article.title }}</h2>
      </router-link>
    </div>
  </div>
</template>

<style scoped></style>
