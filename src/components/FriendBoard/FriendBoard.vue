<script setup>
import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import {ref, reactive} from 'vue';
import FriendList from "@/components/FriendBoard/FriendCard.vue";
import FriendCard from "@/components/FriendBoard/FriendCard.vue";

const friendData = reactive([{userId: 1, username: "sad1"},
  {userId: 1, username: "sad1"},
  {userId: 1, username: "sad1"},
  {userId: 1, username: "sad1"},
  {userId: 1, username: "sad1"},
  {userId: 1, username: "sad1"},
  {userId: 1, username: "sad1"},
  {userId: 1, username: "sad1"},
  {userId: 1, username: "sad1"},
  {userId: 1, username: "sad1"},
  {userId: 1, username: "sad1"},
  {userId: 1, username: "sad1"},

]);


</script>

<template>
  <header>
    <NavigationBar/>
  </header>
  <div id="friend-board-container">
    <div id="friend-list-container">
      <FriendCard v-for="(card,index) in friendData" :count="index" :user-id="card.userId"
                  :username="card.username"></FriendCard>
    </div>
    <div id="friend-chat-container">
      <FriendChat :username="friendData[0].username"></FriendChat>
    </div>
  </div>

</template>

<style scoped>
#friend-board-container {
  position: relative;
  display: flex;
  width: 1000px;
  height: 550px;
  margin-top: 25px;
  left: 250px;
  border : 2px solid #e4e7ed;
  border-left: 2px solid black;
  box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
  border-radius: 10px;
  background-color: white;
}

#friend-list-container {
  height: 100%;
  width: 25%;
  border-right: 4px solid #e4e7ed;
  overflow-y: scroll;
  overflow-x: hidden;
}

#friend-chat-container {
  height: 100%;
  width: 75%;
}


</style>