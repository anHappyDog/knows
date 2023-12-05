<script setup>
import axios from "axios";
import { ref } from "vue";
import {useRouter}  from 'vue-router';
const image = ref(null);
const name = ref("");
const description = ref("");
const router = useRouter();
const onClickCreateBtn = async function () {
    try {
        if (name === "" || description === "") {
            console.log("板块名称或者板块描述不能为空");
            return;
        }
        const formData = new FormData();
        formData.append('image',image.value);
        formData.append('name',name.value);
        formData.append('description',description.value);
        const res = await axios.post(axios.defaults.baseURL + "/api/newCategory",formData);
        if (res.data.status == 0) {
            router.push('/main/categories');
            console.log("创建板块成功");
        } else {
            console.log(res.data.message);
        }
    } catch(err) {
        console.log(err.toString());
    }
};
const onClickBackBtn = async function () {
    router.go(-1);
};
const setImage = function (e) {
  image.value = e.target.files[0];
};
</script>

<template>
  <h1>New Categoty</h1>
  <input type="file" @change="setImage" />
  <label for="name">Name</label>
  <input type="text" placeholder="name" v-model="name" />
  <label for="description">Description</label>
  <input type="text" placeholder="description" v-model="description" />
  <button @click="onClickCreateBtn">Create</button>
  <button @click="onClickBackBtn">Back</button>
</template>

<style scoped></style>
