<script setup>
import { watch, onMounted, onBeforeUpdate, onBeforeUnmount,computed } from 'vue';
import { useRoute, onBeforeRouteUpdate } from "vue-router";
import ArticleCard from '../Article/ArticleCard.vue';
import { ref } from "vue";
import axios from 'axios';
const route = useRoute();
const category_id = ref(route.params.category_id);
const articles = ref(null);
const categoryInfo = ref(null);
const admin = ref(false);
const page = ref(1);
const sizePerPage = 12;
const pages = computed(()=>{
  return articles.value?Math.ceil(articles.value.length/10):1;
});
const slicedArticles = computed(()=> {
  return articles.value?articles.value.slice((page.value-1)*sizePerPage,page.value*sizePerPage):[];
});
onMounted(() => {
  fetchArticlesFromCategory();
});
const fetchArticlesFromCategory = async function () {
  try {
    const res = await axios.get(
      axios.defaults.baseURL + "/api/category/" + category_id.value
    );
    if (res.data.status == 0) {
      articles.value = res.data["data"];
      categoryInfo.value = res.data['categoryInfo'];
      console.log(res.data["data"]);
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};




</script>
<template>
  <Transition>
    <v-container v-if="categoryInfo">
      <v-container class="border boder-1 elevation-2 rounded-sm">
        <v-container class="d-flex flex-row align-center">
          <v-avatar @click="" class="cursor-pointer mr-2 rounded-0">
            <v-img :src="axios.defaults.baseURL + categoryInfo.image" alt="板块头像" />
          </v-avatar>
          <v-btn variant="plain" @click="">{{ categoryInfo.name }}</v-btn>
          <p>{{ categoryInfo.created_time }}</p>
        </v-container>
        <v-divider :thickness="3" />
        <p class="mt-2 ml-2">{{ categoryInfo.description }}</p>
      </v-container>
      <v-container v-if="articles" class="border boder-1 elevation-2 rounded-sm mt-4">
        <v-row>
          <v-col cols="12" sm="6" md="4" lg="3" v-for="article in slicedArticles" :key="article.id">
            <ArticleCard :article="article" />
          </v-col>
        </v-row>
        <v-pagination v-model="page" :length="pages" />
      </v-container>
    </v-container>
  </Transition>
</template>



<style scoped></style>
