<script setup>
import axios from "axios";
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import alertStore from "../../alertStore";
const methods = alertStore.methods;
const feedbacks = ref(null);
const router = useRouter();
const page = ref(1);
const admin = ref(false);

const pages = computed(() => {
    return feedbacks.value ? Math.ceil(feedbacks.value.length / 10) : 1;
});
const sizePerPage = 8;

const slicedFeedbacks = computed(() =>
    feedbacks.value ? feedbacks.value.slice((page.value - 1) * sizePerPage, page.value * sizePerPage) : []
);
const fetchFeedbacks = async function () {
    try {
        const res = await axios.get(axios.defaults.baseURL + "/api/feedbacks");
        if (res.data.status === 0) {
            feedbacks.value = res.data.data;
            admin.value = res.data.admin;
        } else {
            methods.addAlert({
                type: "error",
                message: res.data.message,
                timeout: 3000
            });
        }
    } catch (err) {
        methods.addAlert({
            type: "error",
            message: err.toString(),
            timeout: 3000
        });
    }

};
const goToFeedback = function (id) {
    router.push("/main/feedback/" + id);
}
const newFeedback = function () {
    router.push('/main/newFeedback');
}
const goToUserProfile = function (id) {
    router.push("/main/user/" + id);
}
onMounted(() => {
    fetchFeedbacks();
});


</script>

<template>
    <Transition>
        <div v-if="feedbacks">
            <v-container id="feedback-head-container" class="border border-1 rounded-sm elevation-2 mb-5 mt-2">
                <h1>反馈列表</h1>
                <v-btn id="new-feedback-btn" variant="outlined" @click="newFeedback">发起反馈</v-btn>
            </v-container>
            <div v-for="feedback in feedbacks" :key="feedback.id">
                <v-container class="border border-1 rounded-sm elevation-2 mb-5 mt-2 d-flex flex-row align-center">
                    <v-avatar class="elevation-1 cursor-pointer" @click="goToUserProfile(feedback.user_id)"><v-img
                            :src="axios.defaults.baseURL + feedback.user_avatar" /></v-avatar>
                    <v-btn variant="plain" @click="goToUserProfile(feedback.user_id)">{{ feedback.user }}</v-btn>
                    <p>({{ feedback.created_time }}) : {{ feedback.title }}</p>
                    <v-btn class="ml-auto" variant="outlined" @click="goToFeedback(feedback.id)">查看</v-btn>



                </v-container>

            </div>
            <v-pagination :length="pages" v-model="page" />
        </div>
    </Transition>
</template>

<style scoped>
.feedback-sinfo {
    top: 0;
    right: 10px;
    width: 50%;
    margin-right: 2%;
    margin-bottom: 2%;
}

#feedback-head-container {
    display: flex;
    flex-direction: row;
    border: 1px solid black;
    margin-top: 10px;
    align-items: center;
    border-radius: 6px;
}

#new-feedback-btn {
    margin-left: 3%;
}

.cursor-pointer {
    cursor: pointer;
}
</style>