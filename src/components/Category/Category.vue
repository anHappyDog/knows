<script setup>
import { useRoute } from "vue-router";
import { ref, onBeforeMount } from "vue";
import axios from 'axios';
const route = useRoute();
const category_id = ref(route.params.category_id);
const articles = ref([]);
const fetchArticlesFromCategory = async function () {
  try {
    const res = await axios.get(
      axios.defaults.baseURL + "/api/category/" + category_id.value
    );
    if (res.data.status == 0) {
      articles.value = res.data["data"];

      console.log(res.data["data"]);
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

onBeforeMount(() => { 
  console.log(category_id.value);
    fetchArticlesFromCategory();
});
</script>
<template>
    <h1>Category:{{ category_id }}</h1>
    <div>
        <div v-for="article in articles" :key="article.id">
        <router-link :to="`/main/article/${ article.id }`"> <h2>{{ article.title }}</h2></router-link>
        </div>
    </div>
</template>



<style scoped></style>
