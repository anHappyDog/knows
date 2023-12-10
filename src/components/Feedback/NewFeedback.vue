<script setup>
import axios from "axios";
import { useRouter } from "vue-router";
import { ref } from "vue";
import alertStore from "../../alertStore";
const methods = alertStore.methods;
const title = ref("");
const content = ref("");
const form = ref(null);
const router = useRouter();
const onClickReleaseBtn = async function () {
    const isValid = await form.value.validate();
    if (!isValid.valid) {
        methods.addAlert({
            type: "error",
            message: "请先检查您的输入",
            timeout: 3000
        });
        return;
    }
    try {
        const res = await axios.post(axios.defaults.baseURL + "/api/feedback", {
            title: title.value,
            content: content.value,
        });
        if (res.data.status == 0) {
            methods.addAlert({
                type: "success",
                message: "发布反馈成功",
                timeout: 3000
            });
            router.push("/main/feedbacks");
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