<script setup>
import  testAvatar from "@/assets/avatar.jpg";
const props = defineProps({
  username :{
    type :String,
    required: true
  }

});

</script>

<template>
  <div id="friend-interchat-container">
    <div id="friend-chat-content-container">
      <div id="chat-content-header">
        <img :src="testAvatar" alt="用户头像">
        <p>{{username}}</p>
      </div>
    </div>
    <div id="friend-chat-input-container">
      <textarea id="input-textarea"></textarea>
      <button id="chat-send-btn">发送</button>
    </div>
  </div>
</template>

<style scoped>
#friend-interchat-container {
  display: flex;
  height: 100%;
  flex-direction: column;
}
#friend-chat-content-container {
  height: 60%;
}
#friend-chat-input-container {
  height: 40%;
  width: 100%;
  display: flex;
  border-top: 2px solid #e4e7ed;
}

#chat-content-header {
  width: 100%;
  height: 18%;
  border-bottom: 1px solid #c45656;
  display: flex;
  justify-content: center;
  align-items: center;
  & img {
    width: 48px;
    height: 48px;
    margin: 10px;
    border: 2px solid #e4e7ed;
  }
  & p {

  }
}

#input-textarea {
  background-color: transparent;
  border: 2px  solid black;
  resize: none;
  width: 99%;
  height: auto;
}

#chat-send-btn {
  border: 2px solid black;
  padding: 7px 14px;
  cursor: pointer;
}

</style>