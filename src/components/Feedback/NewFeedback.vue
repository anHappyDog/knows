<script setup>
import axios from "axios";
import { useRouter } from "vue-router";
import { ref, onBeforeMount } from "vue";
const title = ref("");
const content = ref("");
const router = useRouter();
const onClickReleaseBtn = async function() {
    try {
        const res = await axios.post(axios.defaults.baseURL + "/api/feedback", {
            title: title.value,
            content: content.value,
        });
        if (res.data.status == 0) {
            console.log("反馈成功");
            router.push("/main/feedbacks");
        } else {
            console.log(res.data.message);
        }
    } catch (err) {
        console.log(err.toString());
    }
};


</script>

<template>
<label for="title">标题</label>
<input type="text" v-model="title" />
<label for="content">内容</label>
<textarea v-model="content"></textarea>
<button @click="onClickReleaseBtn">提交</button>
</template>

<style scoped>
</style>