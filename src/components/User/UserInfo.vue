<script setup>
import { ref, onBeforeMount } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
const route = useRoute();
const id = ref(route.params.user_id);
const userInfo = ref(null);
const avatar = ref(null);
const cover = ref(null);
const router = useRouter();

const articles = ref([]);
const followers = ref([]);
const followees = ref([]);
const fetchFollowers = async function () {
  try {
    const res = await axios.get(
      axios.defaults.baseURL + "/api/user/" + id.value + "/followers"
    );
    if (res.data.status == 0) {
      followers.value = res.data["data"];
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const fetchFollowees = async function () {
  try {
    const res = await axios.get(
      axios.defaults.baseURL + "/api/user/" + id.value + "/followees"
    );
    if (res.data.status == 0) {
      followees.value = res.data["data"];
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const onClickFollowBtn = async function () {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/follow", {
      user_id: id.value,
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

const onClickUnFollowBtn = async function () {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/unfollow", {
      user_id: id.value,
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

const fetchUserInfo = async function () {
  try {
    const res = await axios.get(
      axios.defaults.baseURL + "/api/user/" + id.value
    );
    if (res.data.status == 0) {
      userInfo.value = res.data["data"];
    } else {
      console.log(res.data.message);
    }
    console.log(res.data);
  } catch (err) {
    console.log(err.toString());
  }
};

const signOut = async function () {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/signOut");
    if (res.data.status == 0) {
      localStorage.removeItem("token");
      router.push("/signIn");
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const selectCover = function (e) {
  cover.value = e.target.files[0];
};

const selectAvatar = function (e) {
  avatar.value = e.target.files[0];
};

const fetchArticles = async function () {
  try {
    const res = await axios.get(
      axios.defaults.baseURL + "/api/user/" + id.value + "/articles"
    );
    articles.value = res.data["data"];
  } catch (e) {
    console.log(er.toString());
  }
};

const uploadCover = async function () {
  try {
    if (cover.value == null) {
      return;
    }
    const formData = new FormData();
    formData.append("cover", cover.value);
    const res = await axios.post(
      axios.defaults.baseURL + "/api/uploadCover",
      formData
    );
    if (res.data.status == 0) {
      fetchUserInfo();
      console.log("成功上传封面");
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

const uploadAvatar = async function () {
  try {
    if (avatar.value == null) {
      return;
    }
    const formData = new FormData();
    formData.append("avatar", avatar.value);
    const res = await axios.post(
      axios.defaults.baseURL + "/api/uploadAvatar",
      formData
    );
    if (res.data.status == 0) {
      fetchUserInfo();
      console.log("成功上传头像");
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

onBeforeMount(() => {
  //   id.value = route.params.user_id;
  fetchUserInfo();
  fetchArticles();
  fetchFollowers();
  fetchFollowees();
});
</script>

<template>
  <div v-if="userInfo !== null">
    <h1>User Id: {{ id }}</h1>
    <input type="file" @change="selectCover" />
    <button @click="uploadCover">上传封面</button>
    <input type="file" @change="selectAvatar" />
    <button @click="uploadAvatar">上传头像</button>
    <button @click="signOut">退出登录</button>

    <p>{{ userInfo.username }}</p>
    <p>{{ userInfo.email }}</p>
    <p>{{ userInfo.introduction }}</p>
    <p>{{ userInfo.avatar }}</p>
    <p>{{ userInfo.cover }}</p>
    <div v-if="!userInfo.isSelf">
      <button v-if="userInfo.is_followed === true" @click="onClickUnFollowBtn">
        取消关注
      </button>
      <button v-else @click="onClickFollowBtn">关注</button>
    </div>
    <h2>My articles</h2>
    <div v-for="article in articles" :key="article.id">
      <router-link :to="'/main/article/' + article.id">
        <h2>{{ article.title }}</h2>
      </router-link>
    </div>
    <h2>My followers</h2>
    <div v-for="follower in followers" :key="follower.id">
      <router-link :to="'/main/user/' + follower.id">
        <h2>{{ follower.username }}</h2>
      </router-link>
    </div>
    <h2>My followings</h2>
    <div v-for="followee in followees" :key="followee.id">
      <router-link :to="'/main/user/' + followee.id">
        <h2>{{ followee.username }}</h2>
      </router-link>
    </div>
  </div>
  <div v-else>
    <h1>User Id: {{ id }}</h1>
    <p>暂无该用户</p>
  </div>
</template>

<style scoped></style>
