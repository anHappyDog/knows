<script setup>
import axios from "axios";
import { useRouter } from "vue-router";
import { ref } from "vue";
const title = ref("");
const content = ref("");
const form = ref(null);
const router = useRouter();
const onClickReleaseBtn = async function() {
    const isValid = await form.value.validate();
    if (!isValid.valid) {
        console.log("请先检查您的输入");
        return;
    }
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

const titleRules = [
    (v) => !!v || "标题是必填项",
    (v) => (v && v.length <= 20) || "标题不能超过20个字符",
];
const contentRules = [
    (v) => !!v || "内容是必填项",
    (v) => (v && v.length <= 400) || "内容不能超过200个字符",
];

</script>

<template>
    <v-container id="feedback-container">
        <v-sheet id="feedback-panel">
            <v-form ref="form">
                <v-text-field v-model="title" label="标题" :rules="titleRules"></v-text-field>
                <v-textarea v-model="content" label="内容" :rules="contentRules"></v-textarea>
                <v-btn @click="onClickReleaseBtn">提交</v-btn>
                </v-form>
        </v-sheet>
    </v-container>
</template>

<style scoped>
#feedback-panel {
    padding: 20px;
}
#feedback-container {
    display: flex;
    flex-direction: column;

}
</style>