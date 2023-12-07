<script setup>
import { ref, inject } from 'vue';
const loading = inject('loading');
</script>

<template>
    <v-app>
        <v-progress-linear :active="loading" color="primary" :indeterminate="true" absolute top />
        <router-view v-slot="{ Component }">
            <transition name="fade" mode="out-in">
                <component :is="Component" />
            </transition>
        </router-view>

    </v-app>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.1s;
}

.fade-enter,
.fade-leave-to

/* .fade-leave-active in <2.1.8 */
    {
    opacity: 0;
}
</style>
