<script setup>
import {ref,onBeforeMount} from 'vue';
import router from '../router';
const userid = ref('');

onBeforeMount(()=>{
  userid.value = localStorage.getItem('token');
})

</script>

<template>
  <div>
    <router-link to="/main/articles">Articles</router-link>
    <router-link to="/main/categories">Categories</router-link>
    <router-link to="/main/newArticle">New Article</router-link>
    <router-link :to="`/main/user/${userid}`">User Info</router-link>
    <router-link to="/main/feedbacks">Feedbacks</router-link>
  </div>
  <router-view> </router-view>
</template>

<style scoped></style>
