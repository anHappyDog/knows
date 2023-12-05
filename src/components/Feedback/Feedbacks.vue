<script setup>
import axios from "axios";
import { ref, onBeforeMount } from "vue";
import { useRouter } from "vue-router";
const feedbacks = ref([]);
const router = useRouter();
const fetchFeedbacks = async function () {
    try {
        const res = await axios.get(axios.defaults.baseURL + "/api/feedbacks");
        feedbacks.value = res.data.data;
    } catch (err) {
        console.log(err.toString());
    }

};
const newFeedback = function() {
    router.push('/main/newFeedback');
}
onBeforeMount(() => {
    fetchFeedbacks();
});


</script>

<template>
    <button @click="newFeedback">New Feedbacks</button>
    <div v-for="feedback in feedbacks" :key="feedback.id">
        <router-link :to="`/main/feedback/${feedback.id}`">{{ feedback.title }}</router-link>
        <p>{{ feedback.content }}</p>
    </div>
</template>

<style scoped></style>