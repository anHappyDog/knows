<script setup>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import alertStore from "../../alertStore";
const methods = alertStore.methods;
const route = useRoute();
const videos = ref(null);
const page = ref(1);
const video = ref(null);
const copyLink = async function (text) {
    try {
        await navigator.clipboard.writeText(text);
        methods.addAlert({
            type:"success",
            message:"复制成功",
            timeout:3000
        });
    } catch (err) {
        methods.addAlert({
            type: "error",
            message: err.toString(),
            timeout: 3000
        });
    }
}

const pages = computed(() => {
    return videos.value ? Math.ceil(videos.value.length / sizePerPage) : 1;
});
const sizePerPage = 8;
const slicedvideos = computed(() => {
    return videos.value ? videos.value.slice((page.value - 1) * sizePerPage, page.value * sizePerPage) : [];
});

const fetchUserVideos = async function () {
    try {
        const res = await axios.get(axios.defaults.baseURL + '/api/user/videos');
        if (res.data.status === 0) {
            videos.value = res.data.data;
            
            return;
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
const onvideoselected = function (e) {
    video.value = e.target.files[0];
    uploadvideo();
};
const uploadvideo = async function () {
    try {
        const formData = new FormData();
        formData.append('video', video.value);
                
        methods.addAlert({
            type:"warning",
            message:"请等待视频上传",
            timeout:3000
        });
        const res = await axios.post(axios.defaults.baseURL + '/api/uploadUserVideo', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });

        if (res.data.status === 0) {
            methods.addAlert({
                type: "success",
                message: "上传成功",
                timeout: 3000
            });
            videos.value = res.data.data;
        } else {
            methods.addAlert({
                type: "error",
                message: res.data.message,
                timeout: 3000
            });
        }
    } catch (err) {
        methods.addAlert({
                type: "success",
                message: err.toString(),
                timeout: 3000
            });
    }
}
onMounted(() => {
    fetchUserVideos();
});

</script>

<template>
    <v-container v-if="videos">
        <p class="text-grey">点击视频复制视频链接哦</p>
        <v-file-input prepend-icon="mdi-paperclip" class="pa-0" @change="onvideoselected" label="上传视频"></v-file-input>
        <v-container class="user-video-container">
            <v-row>
                <v-col cols="12" sm="6" md="4" lg="3" v-for="item in slicedvideos">

                    <v-img @click="copyLink(axios.defaults.baseURL + item.video)"
                        :src="axios.defaults.baseURL + item.preview" />
                </v-col>
            </v-row>
            <v-pagination :length="pages" v-model="page" />
        </v-container>

    </v-container>
</template>

<style scoped></style>