<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from 'vue-router';
import alertStore from "../../alertStore";
const methods = alertStore.methods;
const image = ref(null);
const name = ref("");
const description = ref("");
const router = useRouter();
const form = ref(null);
const onClickCreateBtn = async function () {
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
        const formData = new FormData();
        formData.append('image', image.value);
        formData.append('name', name.value);
        formData.append('description', description.value);
        const res = await axios.post(axios.defaults.baseURL + "/api/newCategory", formData);
        if (res.data.status == 0) {
            router.push('/main/categories');
            methods.addAlert({
                type: "success",
                message: "创建板块成功",
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
};
const onClickBackBtn = async function () {
    router.go(-1);
};
const setImage = function (e) {
    image.value = e.target.files[0];
};

const avatarRules = [
    (v) => !!v || "头像不能为空"
];
const nameRules = [
    (v) => !!v || "板块不能为空",
    (v) => v.length <= 20 || "板块名长度不能超过20",
];
const descriptionRules = [
    (v) => !!v || "板块描述不能为空",
    (v) => v.length <= 200 || "板块描述长度不能超过200",
];


</script>

<template>
    <Transition>
        <v-container class="d-flex align-center flex-column
         rounded-sm border border1 new-category-container elevation-2">
            <h2 class="color-primary ">创建板块</h2>
            <v-sheet width="300" class="mt-10 ">
                <v-form ref="form" @submit.prevent="onClickCreateBtn">
                    <v-file-input prepend-icon="mdi-paperclip" accept="image/*" label="板块头像" @change="setImage"
                        :rules="avatarRules" />
                    <v-text-field label="板块名称" v-model="name" :rules="nameRules" />
                    <v-textarea label="板块描述" v-model="description" :rules="descriptionRules" />
                    <v-container class="d-flex flex-row align-center justify-center">
                        <v-btn type="submit" class="mr-4 for-new-category-btn">创建</v-btn>
                        <v-btn variant="plain" @click="onClickBackBtn" class="for-new-category-btn">返回</v-btn>
                    </v-container>
                </v-form>

            </v-sheet>
        </v-container>

    </Transition>
</template>

<style scoped>
.new-category-container {
    margin-top: 10%;
    width: 50%;
}

.for-new-category-btn {
    width: 40%;
}
</style>
