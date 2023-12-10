<template>
    <div class="main-alert-container">
        <transition-group class="main-alert-group" name="alert" tag="div">
            <v-alert v-for="alert in alerts" :key="alert.id" :type="alert.type" dense dismissible
                @dismiss="removeAlert(alert.id)" class="main-alert-msg m-2">
                {{ alert.message }}
            </v-alert>
        </transition-group>
    </div>
</template>  
<script setup>
import alertStore from '../alertStore';

const { state, methods } = alertStore;
const alerts = state.alerts;
const removeAlert = methods.removeAlert;

</script>
  
<style>

.main-alert-group {
    position: flex;
    flex-direction: column;
    align-items: flex-end;
    width:300px;
    max-width: 300px;
    
    z-index: 9999999 !important;
}

.main-alert-msg {
    margin-top: 10px;
    margin-bottom: 10px;
    z-index: 99999999 !important;
    width: 300px;
    right: 100px;
}

.main-alert-container {
    position: fixed;
    padding: 16px;
    right: 0;
    width: 300px;
    max-width: 300px;
    z-index: 9999999 !important;
}

.alert-enter-active,
.alert-leave-active {
    transition: opacity 0.5s;
}

.alert-enter,
.alert-leave-to {
    opacity: 0;
}
</style>