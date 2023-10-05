<script setup>

import {onMounted, onUnmounted, ref} from "vue";

const backTopFlag = ref(false)//用来判断样式
const backTop = () => {
  let top = document.documentElement.scrollTop//获取点击时页面的滚动条纵坐标位置
  const timeTop = setInterval(() => {
    document.documentElement.scrollTop = top -= 50//一次减50往上滑动
    if (top <= 0) {
      clearInterval(timeTop)
    }
  }, 5)//定时调用函数使其更顺滑
}
const handleScroll = () => {
  backTopFlag.value = document.documentElement.scrollTop > 20;
//往下滑超过20则显示 否则则不显示按钮
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})//监听滚动事件
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <button id="go-top-btn" @click="backTop" :class="backTopFlag ? 'active' : 'inactive'"></button>
</template>

<style scoped>
#go-top-btn {
  position: fixed;
  top: 85%;
  right: 5%;
  cursor: pointer;
  z-index: 10;
  background-image: url("@/assets/rocket.svg");
  background-size: cover;
  width: 70px;
  height: 70px;
  border-radius: 50%;
  border: 1px solid darkgray;
  box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);
}

</style>