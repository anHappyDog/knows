<script setup>
import {ref,onBeforeMount} from 'vue';
import { useRoute,useRouter } from 'vue-router';
import axios from 'axios';
const route = useRoute();
const feedback_id = ref(route.params.feedback_id);
const feedback = ref(null);
const fetchFeedback = async function() {
    try{
        const res = await axios.get(axios.defaults.baseURL + '/api/feedback/' + feedback_id.value);
        if(res.data.status == 0) {
            feedback.value = res.data.data;
            console.log(res.data.data);
        } else {
            console.log(res.data.message);
        }
    } catch(err) {
        console.log(err.toString());
    }
};

onBeforeMount(()=>{
    fetchFeedback();
});


</script>

<template>
<h1>Feedback:{{ feedback_id }}</h1>
<p>{{ feedback.title }}</p>
<p>{{ feedback.content }}</p>
<p>{{ feedback.response }}</p>
<p>{{ feedback.created_time }}</p>
</template>

<style scoped>
</style>