<script setup>
import { useRouter,useRoute } from 'vue-router';
import axios from 'axios';
const route = useRoute();
const router = useRouter();
const props = defineProps({
    article: {
        type: Object,
        required: true
    }
});
const onClickUserAvatar = function (id) {
    router.push('/main/user/' + id);
}
</script>

<template>
    <v-card class="article-card">
        <v-card-title> {{ article.title }}</v-card-title>
        <v-container class="article-author-container">
            <v-avatar color="surface-variant" @click="onClickUserAvatar(article.id)" class="user-avatar">
                <v-img :src="axios.defaults.baseURL + article.author_avatar" />
            </v-avatar>
            <v-btn variant="plain" @click="onClickUserAvatar(article.id)">{{ article.author }}</v-btn>
        </v-container>
        <v-container>
            <p>所属板块:{{ article.category }}</p>
            <p>发布时间:{{ article.date }}</p>
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