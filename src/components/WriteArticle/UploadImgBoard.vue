<script setup>
import {UploadFilled} from '@element-plus/icons-vue'
import axios from 'axios';
import {computed} from "vue";

const beforeUploadImg = function () {

}

const uploadSuccess = function () {

}
const uploadAction = computed(()=>{
  return `${axios.defaults.baseURL}\\api\\uploadImg`
})

</script>

<template>
  <el-upload
      class="upload-demo"
      drag
      :action= "uploadAction"
      :on-success="uploadSuccess"
      :before-upload="beforeUploadImg"
      :with-credentials="true"
  >
    <el-icon class="el-icon--upload">
      <upload-filled/>
    </el-icon>
    <div class="el-upload__text">
      拖拽文件到这或 <em>点击上传</em>
    </div>
    <template #tip>
      <div class="el-upload__tip">
        jpg/png files with a size less than 500kb
      </div>
    </template>
  </el-upload>
</template>

<style scoped>

</style>