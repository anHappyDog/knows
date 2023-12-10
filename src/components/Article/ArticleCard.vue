<script setup>
import {watch,ref} from 'vue';

import { useRouter,useRoute } from 'vue-router';
import axios from 'axios';
import alertStore from "../../alertStore";
const methods = alertStore.methods;
const route = useRoute();
const router = useRouter();
const props = defineProps({
    article: {
        type: Object,
        required: true
    }
});
// const article = ref(route.params.article);
// watch(()=>route.params.article,()=>{
//     console.log(route.params.article);
//     article.value = route.params.article;
// });
const onClickUserAvatar = function (id) {
    router.push('/main/user/' + id);
}

const goToCategory = function (category) {
    router.push('/main/category/' + category);
}
</script>

<template>
    <v-card class="article-card">
        <v-card-title> {{ article.title }}</v-card-title>
        <v-container class="article-author-container">
            <v-avatar color="surface-variant" @click="onClickUserAvatar(article.author_id)" class="user-avatar">
                <v-img :src="axios.defaults.baseURL + article.author_avatar" />
            </v-avatar>
            <v-btn variant="plain"  @click="onClickUserAvatar(article.author_id)">{{ article.author }}</v-btn>
        </v-container>
        <v-container>
            <v-btn variant="plain" @click="goToCategory(article.category_id)">{{ article.category }}</v-btn>
            <!-- <p  @click="" class="text-grey cursor-pointer">:{{ article.category }}</p> -->
            <p>{{ article.date }}前</p>
        </v-container>

        <v-card-actions>
            <v-btn text @click="router.push('/main/article/' + article.id)">查看</v-btn>
        </v-card-actions>
    </v-card>
</template>

<style scoped>
.article-author-container {
    padding: 0;
    padding-left: 1em;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
.user-avatar {
 
    &:hover {
        cursor: pointer;
    }
}
</style>