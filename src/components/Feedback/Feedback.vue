<script setup>
import { ref, onMounted, watch, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import alertStore from "../../alertStore";
const methods = alertStore.methods;
const route = useRoute();
const router = useRouter();
const feedback_id = ref(route.params.feedback_id);
const feedback = ref(null);
const feedbackPosts = ref(null);
const page = ref(1);
const sizePerPage = 8;
const isAnswer = ref(false);
const answer = ref('');
const form = ref(null);
const pages = computed(() => {
    return feedbackPosts.value ? Math.ceil(feedbackPosts.value.length / sizePerPage) : 1;
});
const slicedPosts = computed(() => {
    return feedbackPosts.value ? feedbackPosts.value.slice((page.value - 1) * sizePerPage, page.value * sizePerPage) : [];
});
const admin = ref(false);
const goToUserProfile = function (id) {
    router.push(`/main/user/${id}`);
}
const fetchFeedback = async function () {
    try {
        const res = await axios.get(axios.defaults.baseURL + '/api/feedback/' + feedback_id.value);
        if (res.data.status == 0) {
            feedback.value = res.data.data;
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

const fetchFeedbackPosts = async function () {
    try {
        const res = await axios.get(axios.defaults.baseURL + `/api/feedback/${feedback_id.value}/posts`);
        if (res.data.status === 0) {
            feedbackPosts.value = res.data.data;
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
}

const onClickSendResponseBtn = async function () {
    isAnswer.value = true;
}

onMounted(() => {
    fetchFeedback();
    fetchFeedbackPosts();
});

const newPost = async function () {
    const isValid = await form.value.validate();
    if (!isValid.valid) {
        return;
    }
    try {
        const res = await axios.post(axios.defaults.baseURL + `/api/feedback/${feedback_id.value}/test`, {
            content: answer.value
        });
        if (res.data.status === 0) {
            isAnswer.value = false;
            fetchFeedbackPosts();
            methods.addAlert({
                type: "success",
                message: "回复成功",
                timeout: 3000
            });
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
}

const answerRules = [
    v => !!v || "回复不能为空",
    v => (v && v.length <= 200) || "回复必须小于200字符",
]

</script>

<template>
    <Transition>
        <div v-if="feedback">
            <v-container class="border border-1 rounded-sm elevation-2 mb-5 mt-2 d-flex flex-row align-center ">
                <h1>反馈详情</h1>
                <v-btn class="ml-auto mr-10" @click="onClickSendResponseBtn" v-if="feedback.can_answer">回复</v-btn>
            </v-container>
            <v-container class="border border-1 rounded-sm elevation-2">
                <v-container class="d-flex flex-row align-center pa-0">
                    <v-avatar class="ml-2 cursor-pointer" @click=""><v-img
                            :src="axios.defaults.baseURL + feedback.user_avatar" /></v-avatar>
                    <v-btn variant="plain" @click="">{{ feedback.user }}</v-btn>
                    <p>({{ feedback.created_time }})</p>
                    <p>: {{ feedback.title }}</p>
                </v-container>
                <v-divider class="mt-2" thickness="3" />
                <v-container>
                    <p>{{ feedback.content }}</p>
                </v-container>
            </v-container>
            <v-container class=" border border-2  mt-2 elevation-2 rounded-sm">

                <v-container v-if="isAnswer">
                    <v-form ref="form" @submit.prevent="newPost">
                        <v-textarea label="回复" v-model="answer" :rules="answerRules" />
                        <v-container>
                            <v-btn class="mr-4" type="submit">回复</v-btn>
                            <v-btn @click="isAnswer = false">返回</v-btn>
                        </v-container>
                    </v-form>
                    <v-divider :thickness="2" />
                </v-container>
                <v-container class="d-flex align-center justify-center">
                    <p class="align-center text-grey" v-if="!feedbackPosts || feedbackPosts.length === 0">暂无回复</p>
                </v-container>
                <v-container class="pa-0" v-if="feedbackPosts && feedbackPosts.length !== 0">
                    <div v-for="post in slicedPosts">
                        <v-container class="d-flex flex-row align-center">
                            <v-avatar class="cursor-pointer" @click="goToUserProfile(post.user_id)">
                                <v-img :src="axios.defaults.baseURL + post.user_avatar" />
                            </v-avatar>
                            <v-btn variant="plain" @click="">{{ post.user }}</v-btn>
                            <p>({{ post.created_time }})</p>
                        </v-container>
                        <v-divider :thickness="2" />
                        <v-container>
                            <p>{{ post.content }}</p>
                        </v-container>
                    </div>
                </v-container>
                <v-divider :thickness="2" />
                <v-pagination :length="pages" v-model="page" />
            </v-container>
            <!--
            <v-container class="sub-container">
                <p>{{ feedback.content }}</p>
            </v-container>
            <v-container class="sub-container">
                <p>{{ feedback.response }}</p>
            </v-container>
            <v-container class="sub-container" v-if="admin && feedback.response === ''">
                <v-form>
                    <v-textarea v-model="response" />
                    <v-btn>发送</v-btn>
                </v-form>

            </v-container> -->
        </div>
    </Transition>
</template>

<style scoped>
.sub-container {
    margin: 10px;
    border: 1px solid #ccc;
    padding: 10px;
}
</style>