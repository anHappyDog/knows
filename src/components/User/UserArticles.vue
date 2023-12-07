<script setup>
import ArticleCard from '../Article/ArticleCard.vue';
import axios from 'axios';
import { ref, computed,onMounted,watch } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute();
const props = defineProps({
    user_id : {
        required: true
    }
});
watch (()=>route.params.user_id,()=>{
    fetchArticles();
});
const articles = ref(null);
const page = ref(1);
const sizePerPage = 12;
const pages = computed(()=>{return articles.value?Math.ceil(articles.value.length / 8):1; });
onMounted(() => {
    console.log("user article is mounted");
    fetchArticles();

})

const fetchArticles = async function () {
    try {
        const res = await axios.get(
            axios.defaults.baseURL + "/api/user/" + route.params.user_id + "/articles"
        );
        articles.value = res.data["data"];
        console.log(articles.value);
    } catch (e) {
        console.log(e.toString());
    }
};
const slicedArticles = computed(()=>{
    return articles.value?articles.value.slice((page.value - 1) * sizePerPage,page.value * sizePerPage):[];
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