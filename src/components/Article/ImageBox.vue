<script setup>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute();
const images = ref(null);
const page = ref(1);
const image = ref(null);
const copyLink = async function (text) {
    try {
        await navigator.clipboard.writeText(text);
    } catch (err) {
        console.log(err.toString());
    }
}

const pages = computed(() => {
    return images.value ? Math.ceil(images.value.length / sizePerPage) : 1;
});
const sizePerPage = 8;
const slicedimages = computed(() => {
    return images.value ? images.value.slice((page.value - 1) * sizePerPage, page.value * sizePerPage) : [];
});

const fetchUserImages = async function () {
    try {
        const res = await axios.get(axios.defaults.baseURL + '/api/user/images');
        if (res.data.status === 0) {

            images.value = res.data.data;
        } else {
            console.log(res.data.message);
        }
    } catch (err) {
        console.log(err.toString());
    }
}
const onImageSelected = function (e) {
    image.value = e.target.files[0];
    uploadImage();
};
const uploadImage = async function () {
    try {
        console.log(image.value);
        const formData = new FormData();
        formData.append('image', image.value);
        const res = await axios.post(axios.defaults.baseURL + '/api/uploadUserImage', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        if (res.data.status === 0) {
            console.log('上传成功');
            fetchUserImages();
        } else {
            console.log(res.data.message);
        }
    } catch (err) {
        console.log(err.toString());
    }
}
onMounted(() => {
    fetchUserImages();
});

</script>

<template>
    <v-container v-if="images">
        <p class="text-grey">点击图片复制图片链接哦</p>
        <v-file-input     prepend-icon="mdi-paperclip" class="pa-0" @change="onImageSelected" accept="image/*" label="上传图片"></v-file-input>

        <v-container class="user-image-container">
            <v-row>
                <v-col cols="12" sm="6" md="4" lg="3" v-for="item in slicedimages">

                    <v-img @click="copyLink(axios.defaults.baseURL + item.image)"
                        :src="axios.defaults.baseURL + item.image" />
                </v-col>
            </v-row>
            <v-pagination :length="pages" v-model="page" />
        </v-container>

    </v-container>
</template>

<style scoped>

</style>