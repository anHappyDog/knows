<script setup>
import axios from 'axios';
import { useRoute,useRouter } from 'vue-router';
import { ref, computed, onMounted,watch } from 'vue';
const followers = ref(null);
const route = useRoute();
const router = useRouter();
const props = defineProps({
    user_id: {
        required: true
    }
});
const fetchFollowers = async function () {
    try {
        const res = await axios.get(
            axios.defaults.baseURL + "/api/user/" + route.params.user_id + "/followers"
        );
        if (res.data.status == 0) {
            followers.value = res.data["data"];
            console.log(followers.value);
        } else {
            console.log(res.data.message);
        }
    } catch (err) {
        console.log(err.toString());
    }
};
const sizePerPage = 12;
const pages = computed(() => {
    return followers.value ? Math.ceil(followers.value.length / sizePerPage) : 1;
});
const page = ref(1);
const slicedFollowers = computed(() => {

    return followers.value ? followers.value.slice((page.value - 1) * sizePerPage, page.value * sizePerPage) : [];
});
onMounted(() => {
    fetchFollowers();
})
watch (()=>route.params.user_id,()=>{
    fetchFollowers();
});

const onClickFollowBtn = async function (id) {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/follow", {
      user_id: id,
    });
    if (res.data.status == 0) {
      console.log("关注成功");
      fetchUserInfo();
      fetchFollowees();
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};
const goToUserProfile = function(id) {
    console.log(id);
    router.push("/main/user/" + id);
}

</script>

<template>
    <v-container v-if="followers">
        <v-row>
            <v-col cols="12" sm="6" md="4" lg="3" v-for="follower in slicedFollowers" :key="follower.id">
                <v-card>
                    <v-card-title @click="goToUserProfile(follower.id)" class="cursor-pointer">{{ follower.username }}</v-card-title>
                    <v-card-subtitle>{{ follower.email }}</v-card-subtitle>
                    <v-card-actions>
                        <v-btn @click="onClickFollowBtn(follower.id)">关注</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-container v-if="followers.length === 0" class="d-flex align-center justify-center">
                <p>暂无粉丝</p>
            </v-container>
        </v-row>
        <v-pagination :length="pages" v-model="page" />

    </v-container>
</template>

<style scoped></style>