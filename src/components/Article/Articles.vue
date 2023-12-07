<script setup>
import { computed, ref, onMounted,inject,watch } from "vue";
import axios from "axios";
import router from "../../router";
import ArticleCard from "../Article/ArticleCard.vue";
const articles = ref(null);
const page = ref(1);
const keyword = inject('keyword');
const sizePerPage = 24;
const pages = computed(()=>{ return  Math.ceil(articles.value.length / sizePerPage);});

const getArticles = async function () {
  try {
    const res = await axios.get(axios.defaults.baseURL + "/api/articles");
    articles.value = res.data["data"];
  } catch (err) {
    console.log(err.toString());
  }
};





const fetchArticles = async function() {
  if (!keyword||keyword.value === "") {
    getArticles();
  }
  page.value = 1;
  axios.get(axios.defaults.baseURL + "/api/articles/search/" + keyword.value).then(res=>{
    if (res.data.status !== 0) {
      console.log(res.data.message);
      return;
    } else {
      articles.value = res.data.data;
    }
  }).catch(err=>{
    console.log(err.toString());
  })
}

watch (keyword,()=>{
  fetchArticles();
});

onMounted(() => {
  fetchArticles();
});
const slicedArticles = computed(() => {
  return articles.value ? articles.value.slice((page.value - 1) * sizePerPage, page.value * sizePerPage) : [];
});
</script>

<template>
  <Transition>
    <v-container v-if="articles">
      <v-row>
        <v-col cols="12" sm="6" md="4" lg="3" v-for="article in slicedArticles" :key="article.id">
          <ArticleCard :article="article" />
        </v-col>
      </v-row>
      <v-pagination :length="pages" v-model="page" />
    </v-container>

  </Transition>
</template>

<style scoped></style>
