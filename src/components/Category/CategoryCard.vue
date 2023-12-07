<script setup>
import axios from 'axios';
import { useRouter } from 'vue-router';
defineProps({
    category: {
        type: Object,
        required: true,
    },
    admin: {
        type: Boolean,
        required: true,
    }
});

const router = useRouter();
const goToCategory = function (id) {
    router.push(`/main/category/${id}`);
}
const onClickDeleteCategoryBtn = async function (id) {
    try {
        const res = await axios.post(axios.defaults.baseURL + "/api/delCategory", {
            category_id: id,
        });
        if (res.data.status == 0) {
            console.log("成功删除分类");
            fetchCategories();
        } else {
            console.log(res.data.message);
        }
    } catch (err) {
        console.log(err.toString());
    }
};
</script>

<template>
    <div v-if="category" class="position-relative">
        <div class="d-flex flex-row align-center mb-2">
            <v-avatar class="cursor-pointer mr-2" @click="goToCategory(category.id)" rounded="0">
                <v-img :src="axios.defaults.baseURL + category.image" alt="板块图片" />
            </v-avatar>
            <v-btn class="ml-0 category-entry-btn" @click="goToCategory(category.id)" variant="plain">
                <span></span>{{ category.name }}
            </v-btn>
        </div>
        <v-divider />
        <v-container class="pa-0 description-container">
            <p class="mt-2">{{ category.description }}</p>
        </v-container>
        <p class="text-grey">{{ category.created_time }}</p>
        <v-btn class="position-absolute del-btn-ctr" @click="onClickDeleteCategoryBtn(category.id)">删除</v-btn>
    </div>
</template>

<style scoped>
.cursor-pointer {
    cursor: pointer;
}
.description-container {
    max-height: 100px;
    overflow: hidden;
}
.del-btn-ctr {
    top: 0;
    right: 10px;
}

.category-entry-btn {
    font-size: large;
    font-style: bold;
}
</style>