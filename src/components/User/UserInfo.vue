<script setup>
import { ref, onBeforeMount, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import UserFollowers from './UserFollowers.vue';
import UserFollowees from './UserFollowees.vue';
import UserArticles from './UserArticles.vue';
const route = useRoute();
const id = ref(route.params.user_id);
const userInfo = ref(null);
const avatar = ref(null);
const cover = ref(null);
const tab = ref(null);
const router = useRouter();
const avatarInput = ref(null);
const coverInput = ref(null);
const dialog = ref(false);
const changedEmail= ref('');
const changedIntroduction = ref('');
const changeForm = ref(null);

watch(() => route.params.user_id, (newUserId) => {
  id.value = newUserId;
});
const onClickFollowBtn = async function () {
  try {
    const res = await axios.post(axios.defaults.baseURL + "/api/follow", {
      user_id: id.value,
    });
    if (res.data.status == 0) {
      console.log("关注成功");
      fetchUserInfo();
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
  if (cover.value) {
    uploadCover();
  }
};

const selectAvatar = function (e) {
  avatar.value = e.target.files[0];
  if (avatar.value) {
    uploadAvatar();
  }
};


watch(id, () => {
  fetchUserInfo();
})


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

const openChangeUser = function() {
  dialog = true;
  changedEmail = userInfo.email;
  changedIntroduction = userInfo.introduction;
}

const changedEmailRules = [
  v => !!v || "电子邮箱不能为空",
  v => /.+@.+\..+/.test(v) || "请输入正确的电子邮箱",
];
const changedIntroductionRules = [
  v => !!v || "个人描述不能为空",
  v => v.length <= 200 || '个人介绍不能超过200字符'
];

const onClickChangeUserBtn = async function() {
  const isValid = await changeForm.value.validate();
  if (!isValid.valid) {
    return;
  }
  try{
    const res = await axios.post(axios.defaults.baseURL + '/api/changeUserInfo',{
      email:changedEmail.value,
      introduction: changedIntroduction.value
    });
    if (res.data.status === 0) {
      fetchUserInfo();
      dialog.value = false;
    } else {
      console.log(res.data.message);
    }
  } catch(err) {
    console.log(err.toString());
  };
}

const onClickBackUserBtn = function() {
  dialog = false;
}

onBeforeMount(() => {
  //   id.value = route.params.user_id;
  fetchUserInfo();

});

</script>

<template>
  <transition>
    <div v-if="userInfo">
      <v-container class="position-relative rounded-sm elevation-2 mt-6 pa-0 rounded-sm">
        <v-btn class="upload-cover-btn" @click="coverInput.click()">上传封面</v-btn>
        <v-img height="120" cover :src="axios.defaults.baseURL + userInfo.cover" />
        <v-container class="user-baseinfo-container">
          <v-container class="user-btns">
            <v-btn v-if="!userInfo.isSelf && !userInfo.is_followed" @click="onClickFollowBtn">关注</v-btn>
            <v-btn v-else-if="!userInfo.isSelf && userInfo.is_followed" @click="onClickUnFollowBtn">取消关注</v-btn>
            <v-btn v-if="userInfo.isSelf" class="ml-3" @click="signOut">退出登录</v-btn>
            <v-btn v-if="userInfo.isSelf" class="ml-3" @click="dialog = true">修改资料</v-btn>
          </v-container>
          <v-avatar size="120px" class="usr-profile-avatar" @click="avatarInput.click()">
            <v-img :src="axios.defaults.baseURL + userInfo.avatar" />
          </v-avatar>
          <input type="file" hidden ref="avatarInput" accept="image/*" @change="selectAvatar" />
          <input type="file" hidden ref="coverInput" accept="image/*" @change="selectCover" />
          <p class="profile-username">{{ userInfo.username }}</p>
        </v-container>
      </v-container>
      <v-container class="border border-2 rounded-sm elevation-2 mt-6 pa-0 rounded-sm">
        <v-container>
          <p>电子邮箱:{{ userInfo.email }}</p>
        </v-container>
        <v-container>
          <p>个人介绍:{{ userInfo.introduction }}</p>
        </v-container>
        <v-divider />
        <v-tabs v-model="tab" align-tabs="center">
          <v-tab>我的文章</v-tab>
          <v-tab>我的关注</v-tab>
          <v-tab>我的粉丝</v-tab>
        </v-tabs>
        <v-window v-model="tab">
          <v-window-item>
            <UserArticles :user_id="userInfo.user_id" :key="userInfo.user_id" />
          </v-window-item>
          <v-window-item>
            <UserFollowees :user_id="userInfo.user_id" :key="userInfo.user_id" />
          </v-window-item>
          <v-window-item>
            <UserFollowers :user_id="userInfo.user_id" :key="userInfo.user_id" />
          </v-window-item>
        </v-window>
      </v-container>
      <v-dialog v-model="dialog" width="50%">
        <v-card>
          <v-container>
            <v-form ref="changeForm" @submit.prevent="onClickChangeUserBtn">
              <v-text-field label="电子邮箱"  :placeholder="userInfo.email" :rules="changedEmailRules" v-model="changedEmail" />
              <v-textarea label="个人介绍" :placeholder="userInfo.introduction" :rules="changedIntroductionRules" v-model="changedIntroduction" />
              <v-btn class="mr-2" type="submit">确认修改</v-btn>
              <v-btn variant="plain" @click="dialog = false">返回</v-btn>
            </v-form>
          </v-container>

        </v-card>
      </v-dialog>
    </div>
  </transition>
</template>

<style scoped>
@keyframes rotate {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}

.user-btns {
  position: absolute;
  z-index: 10;
  width: fit-content;
  right: 5%;
}

.upload-cover-btn {
  position: absolute;
  z-index: 10;
  background-color: transparent;
  right: 5%;
  top: 10%;
  border-width: 1px;
}

.user-baseinfo-container {
  min-height: 100px;
}

.profile-username {
  margin-left: 150px;
  font-size: 24px;
  padding: 0;
}

.usr-profile-avatar {
  position: absolute;
  top: 70px;
  border: 1px solid #a59c9c;

  & :hover {
    animation: rotate 1s ease-in-out;
  }
}
</style>
