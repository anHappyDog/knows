<script setup>
import ArticleCard from '../Article/ArticleCard.vue';
import axios from 'axios';
import { ref, computed, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import alertStore from '../../alertStore';
const methods = alertStore.methods;
const route = useRoute();
const user_id = ref(route.params.user_id);
const props = defineProps({
    user_id: {
        required: true
    }
});
watch(() => route.params.user_id, () => {
    user_id.value = route.params.user_id;
    if (user_id.value) {
        fetchArticles();
    }
});
const articles = ref(null);
const page = ref(1);
const sizePerPage = 12;
const pages = computed(() => { return articles.value ? Math.ceil(articles.value.length / 8) : 1; });
onMounted(() => {
    fetchArticles();

})

const fetchArticles = async function () {
    try {
        const res = await axios.get(
            axios.defaults.baseURL + "/api/user/" + user_id.value + "/articles"
        );
        articles.value = res.data["data"];
    } catch (e) {
        methods.addAlert({
            type: "error",
            message: e.toString(),
            timeout: 3000
        });
    }
};
const slicedArticles = computed(() => {
    return articles.value ? articles.value.slice((page.value - 1) * sizePerPage, page.value * sizePerPage) : [];
});
</script>

<template>
    <Transition>
        <v-container v-if="articles">
            <v-row>
                <v-col cols="12" sm="6" md="4" lg="3" v-for="article in slicedArticles" :key="article.id">
                    <ArticleCard :article="article" />
                </v-col>
            </v-row>
            <v-pagination :length="pages" v-model="page"></v-pagination>
        </v-container>

    </Transition>
</template>

<style scoped></style>