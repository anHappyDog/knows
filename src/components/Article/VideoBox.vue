<script setup>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute();
const videos = ref(null);
const page = ref(1);
const video = ref(null);
const copyLink = async function (text) {
    try {
        await navigator.clipboard.writeText(text);
    } catch (err) {
        console.log(err.toString());
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
        } else {
            console.log(res.data.message);
        }
    } catch (err) {
        console.log(err.toString());
    }
}
const onvideoselected = function (e) {
    video.value = e.target.files[0];
    console.log(video);
    uploadvideo();
};
const uploadvideo = async function () {
    try {
        console.log(video.value);
        const formData = new FormData();
        formData.append('video', video.value);
        const res = await axios.post(axios.defaults.baseURL + '/api/uploadUserVideo', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        if (res.data.status === 0) {
            console.log('上传成功');
            fetchUserVideos();
        } else {
            console.log(res.data.message);
        }
    } catch (err) {
        console.log(err.toString());
    }
}
onMounted(() => {
    fetchUserVideos();
});

</script>

<template>
    <v-container v-if="videos">
        <p class="text-grey">点击视频复制视频链接哦</p>
        <v-file-input     prepend-icon="mdi-paperclip" class="pa-0" @change="onvideoselected"  label="上传视频"></v-file-input>
        <p>{{ videos }}</p>
        <v-container class="user-video-container">
            <v-row>
                <v-col cols="12" sm="6" md="4" lg="3" v-for="item in slicedvideos">

                    <v-img @click="copyLink(axios.defaults.baseURL + item.preview)"
                        :src="axios.defaults.baseURL + item.video" />
                </v-col>
            </v-row>
            <v-pagination :length="pages" v-model="page" />
        </v-container>

    </v-container>
</template>

<style scoped>

</style>