<script setup>
import {ref, defineEmits, computed} from 'vue';
import UploadImgBoard from "@/components/WriteArticle/UploadImgBoard.vue";

const props = defineProps({
  visible: {
    type: Boolean,
    required: true,
  }
});

const emit = defineEmits(['update:visible']);

const isVisible = computed({
  get: () =>
      props.visible,
  set: (val) => {
    console.log(val);
    emit('update:visible', val);
  }
})


</script>

<template>
  <el-dialog
      @close="isVisible = false;"
      v-model="isVisible"
      width="700px"
      align-center>
    <UploadImgBoard/>
  </el-dialog>
</template>

<style scoped lang="less">
</style>