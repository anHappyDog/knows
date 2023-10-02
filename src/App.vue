<script>

import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
</script>

<template>
  <router-view></router-view>
</template>

<style scoped>
header {
  line-height: 1.5;
}


@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }
  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
