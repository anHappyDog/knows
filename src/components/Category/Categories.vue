<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import CategoryCard from "./CategoryCard.vue";
import alertStore from "../../alertStore";
const methods = alertStore.methods;
const router = useRouter();
const admin =  ref(false);
const categories = ref(null);
const fetchCategories = async function () {
  try {
    const res = await axios.get(axios.defaults.baseURL + "/api/categories");
    categories.value = res.data["data"];
  } catch (err) {
    methods.addAlert({
      type: "error",
      message: err.toString(),
      timeout: 3000
    });
  }
};

const onClickNewCategoryBtn = function () {
  router.push("/main/newCategory");
};

const fetchAdmin = async function () {
  try {
    const res = await axios.get(axios.defaults.baseURL + "/api/admin");
    if (res.data.status == 0) {
      admin.value = res.data["data"];
      console.log(admin.value);
    } else {
      console.log(res.data.message);
    }
  } catch (err) {
    console.log(err.toString());
  }
};

onMounted(() => {
  fetchAdmin();
  fetchCategories();
});
</script>

<template>
  <Transition>
    <div v-if="categories">
      <v-container v-if="admin" class="border boder-2 mt-4 mb-4 rounded-sm elevation-2">
        <v-btn variant="outlined" @click="onClickNewCategoryBtn">新建板块</v-btn>
      </v-container>
      <v-container class="border boder-2 mt-4 mb-4 rounded-sm elevation-2">
        <v-container>
          <v-row>
            <v-col cols="12" sm="12" md="6" lg="4" v-for="category in categories" :key="category.id">
              <CategoryCard :admin="admin" :category="category" />
            </v-col>
          </v-row>
        </v-container>
      </v-container>

    </div>
  </Transition>
</template>
<style scoped></style>
