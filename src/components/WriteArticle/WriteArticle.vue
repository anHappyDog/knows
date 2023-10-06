<script setup>
import {ref,reactive,onMounted} from 'vue'
import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
const inputText = ref('');
onMounted(()=>{
})

</script>

<template>
  <header>
    <NavigationBar />
  </header>
    <v-md-editor :value="inputText"></v-md-editor>
</template>

<style scoped>

</style>