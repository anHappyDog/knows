<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import ImageBox from "./ImageBox.vue";
import VideoBox from "./VideoBox.vue";
const router = useRouter();
const content = ref("");
const cover = ref(null);
const categories = ref(null);
const category_id = ref(null);
const title = ref("");
const form = ref(null);
const dialog = ref(false);
const tab = ref(null);
const category_names = computed(() => {
  return categories.value.map(category => category.name);
});
const category_name = ref('');
const fetchCategories = async function () {
  try {
    const res = await axios.get(axios.defaults.baseURL + "/api/categories");
    categories.value = res.data["data"];
  } catch (err) {
    console.log(err.toString());
  }
};

const onClickBackBtn = function () {
  try {
    router.back();
  } catch (err) {
    console.log(err.toString());
  }
};
const getCategoryId = function () {
  for (const t in categories.value) {
    if (categories.value[t].name === category_name.value) {
      return categories.value[t].id;
    }
  }
}
const onClickReleseBtn = async function () {
  const isValid = await form.value.validate();
  if (!isValid.valid) {
    return;
  }
  try {
    const formData = new FormData();
    if (cover.value !== null) {
      formData.append("cover", cover.value);
    }
    formData.append("content", content.value);
    formData.append("title", title.value);
    formData.append("category_id", getCategoryId(category_name.value));
    const res = await axios.post(axios.defaults.baseURL + "/api/newArticle", formData);
    if (res.data.status === 0) {
      console.log("成功发布文章");
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};
const setCover = function (e) {
  cover.value = e.target.files[0];
};

const titleRules = [
  v => !!v || "标题不能为空",
  v => v.length <= 20 || "标题不能超过20个字符"
];
const categoryRules = [v => !!v || "分类不能为空"];


onMounted(() => {
  fetchCategories();
});
</script>

<template>
  <Transition>
    <div v-if="categories">
      <v-container class="border border-2 rounded-sm elevation-2  mb-4 mt-6">
        <v-form ref="form" @submit.prevent="onClickReleseBtn">
          <v-text-field label="标题" v-model="title" :rules="titleRules" />
          <v-container class="d-flex flex-row align-center justify-center">
            <v-file-input class="mr-4" @change="setCover" label="封面上传" variant="filled" prepend-icon="mdi-camera" />
            <v-select class="mr-4" label="板块" :items="category_names" v-model="category_name"
              :rules="categoryRules"></v-select>
            <v-btn @click="dialog = true;">管理文件</v-btn>
          </v-container>


          <v-container class="d-flex align-center">
            <v-btn variant="outlined" class="mr-2" type="submit">发布</v-btn>
            <v-btn variant="plain" @click="onClickBackBtn">返回</v-btn>
          </v-container>
        </v-form>

      </v-container>
      <v-container class="border border-2 rounded-sm elevation-2 pa-0">
        <v-md-editor v-model="content" height="400px"></v-md-editor>
      </v-container>
      <v-dialog v-model="dialog" width="auto">
        <v-card min-height="600px" min-width="800px">
          <v-tabs v-model="tab" align-tabs="center">
            <v-tab>
              图片
            </v-tab>
            <v-tab>
              视频
            </v-tab>
          </v-tabs>
          <v-window v-model="tab">
            <v-window-item>
              <ImageBox/>
            </v-window-item>
            <v-window-item>
              <VideoBox />
            </v-window-item>
          </v-window>
          <v-btn class="mt-auto" @click="dialog=false;">关闭</v-btn>
        </v-card>

      </v-dialog>
    </div>
  </Transition>
</template>

<style scoped></style>
