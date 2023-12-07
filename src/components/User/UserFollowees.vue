<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
const route = useRoute();
const props = defineProps({
    user_id: {
        required: true
    }
})
const followees = ref(null);
const page = ref(1);
const sizePerPage = 12;
const pages = computed(() => { return followees.value ? Math.ceil(followees.value.length / sizePerPage) : 1; });
const fetchFollowees = async function () {
    try {
        const res = await axios.get(
            axios.defaults.baseURL + "/api/user/" + route.params.user_id + "/followees"
        );
        if (res.data.status == 0) {
            followees.value = res.data["data"];

            console.log(followees.value.length);
        } else {
            console.log(res.data.message);
        }
    } catch (err) {
        console.log(err.toString());
    }
};
onMounted(() => {
    fetchFollowees();
});
const onClickUnFollowBtn = async function (id) {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/unfollow", {
      user_id: id,
    });
    if (res.data.status == 0) {
      console.log("取消关注成功");
      fetchUserInfo();
      fetchFollowees();
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};
const slicedFollowees = computed(() => {
    return followees.value != null ? followees.value.slice((page.value - 1) * sizePerPage, page.value * sizePerPage) : [];
});

</script>

<template>
    <v-container v-if="followees">
        <v-row>
            <v-col cols="12" sm="6" md="4" lg="3" v-for="followee in slicedFollowees" :key="followee.id">
                <v-card>
                    <v-card-title>{{ followee.username }}</v-card-title>
                    <v-card-subtitle>{{ followee.email }}</v-card-subtitle>
                    <v-card-actions>
                        <v-btn @click="onClickUnFollowBtn(followee.id)">取消关注</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
        <v-container v-if="followees.length === 0" class="d-flex align-center justify-center">
            <p>暂无关注</p>
        </v-container>
        <v-pagination :length="pages" v-model="page" />
    </v-container>
</template>

<style scoped></style>