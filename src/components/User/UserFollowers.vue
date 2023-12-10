<script setup>
import axios from 'axios';
import { useRoute,useRouter } from 'vue-router';
import { ref, computed, onMounted,watch } from 'vue';
import alertStore from '../../alertStore';
const methods = alertStore.methods; 
const followers = ref(null);
const route = useRoute();
const router = useRouter();
const user_id = ref(route.params.user_id);
const props = defineProps({
    user_id: {
        required: true
    }
});
const fetchFollowers = async function () {
    try {
        const res = await axios.get(
            axios.defaults.baseURL + "/api/user/" + user_id.value + "/followers"
        );
        if (res.data.status == 0) {
            followers.value = res.data["data"];
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
    user_id.value = route.params.user_id;
    if (route.params.user_id) {
        fetchFollowers();
    }
});

const onClickFollowBtn = async function (id) {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/follow", {
      user_id: id,
    });
    if (res.data.status == 0) {
      methods.addAlert({
        type: "success",
        message:"关注成功",
        timeout:3000
      })
      fetchFollowers();
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
};
const goToUserProfile = function(id) {
    router.push("/main/user/" + id);
}
const onClickUnFollowBtn = async function (id) {
    try {
        const res = await axios.post(axios.defaults.baseURL + "/api/unfollow", {
            user_id: id,
        });
        if (res.data.status == 0) {
            methods.addAlert(
                {
                    type: "success",
                    message: "取消关注成功",
                    timeout: 3000
                }
            );
            fetchFollowers();
        } else {
            console.log(res.data.message);
        }
    } catch (err) {
        console.log(err.toString());
    }
};
</script>

<template>
    <v-container v-if="followers">
        <v-row>
            <v-col cols="12" sm="6" md="4" lg="3" v-for="follower in slicedFollowers" :key="follower.id">
                <v-card>
                    <v-card-title @click="goToUserProfile(follower.id)" class="cursor-pointer">{{ follower.username }}</v-card-title>
                    <v-card-subtitle>{{ follower.email }}</v-card-subtitle>
                    <v-card-actions>
                        <v-btn v-if="follower.is_followed === false" @click="onClickFollowBtn(follower.id)">关注</v-btn>
                        <v-btn v-if="follower.is_followed"  @click="onClickUnFollowBtn(follower.id)">取消关注</v-btn>
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