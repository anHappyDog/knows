<script setup>
import {ref} from 'vue';
import testAvatar from "@/assets/avatar.jpg";

const props = defineProps({
  userId: {
    type: Number,
    required: true
  },
  username: {
    type: String,
    required: true
  },
  count: {
    type: Number,
    required: true
  }
});
const userAvatar = ref(testAvatar);

</script>

<template>
  <div class="friend-card-container">
    <img :src="userAvatar" alt="" class="user-card-avatar">
    <p class="user-card-name">{{ username }}</p>
  </div>

</template>

<style scoped>
.friend-card-container {
  display: flex;
  border-bottom: 1px solid #e4e7ed;
  justify-items: center;
  align-items: center;
  cursor: pointer;

  & img {
    border-radius: 50%;
    border: 1px solid black;
    height: 48px;
    width: 48px;
    margin: 6px;
    overflow: hidden;
  }

  & p {
    margin-left: 10px;

  }
}


</style>