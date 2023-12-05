<script setup>
import { ref, onBeforeMount } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();
const categories = ref([]);
const admin = ref(false);
const fetchCategories = async function () {
  try {
    const res = await axios.get(axios.defaults.baseURL + "/api/categories");
    categories.value = res.data["data"];
  } catch (err) {
    console.log(err.toString());
  }
};

const fetchAdmin = async function () {
  try {
    const res = await axios.get(axios.defaults.baseURL + "/api/admin");
    if (res.data.status == 0) {
      admin.value = res.data["data"];
      console.log(admin.value);
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const onClickNewCategoryBtn = function () {
  console.log("点击了新建分类按钮");
  router.push("/main/newCategory");
};

const onClickDeleteCategoryBtn = async function (id) {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/delCategory", {
      category_id: id,
    });
    if (res.data.status == 0) {
      console.log("成功删除分类");
      fetchCategories();
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

onBeforeMount(() => {
  fetchAdmin();
  fetchCategories();
});
</script>

<template>
  <h1>Categories</h1>
  <button v-if="admin" @click="onClickNewCategoryBtn">New Category</button>
  <div v-for="category in categories" :key="category.id">
    <router-link :to="'/main/category/' + category.id">
      <h2>{{ category.name }}</h2></router-link>

    <p>{{ category.description }}</p>
    <p>{{ category.image }}</p>
    <p>{{ category.created_time }}</p>
    <button @click="onClickDeleteCategoryBtn(category.id)">删除</button>
  </div>
</template>
<style scoped></style>
