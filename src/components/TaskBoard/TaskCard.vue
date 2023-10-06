<script setup>
import {onMounted, ref} from 'vue';
import upArrow from "@/assets/upArrow.svg";
import downArrow from "@/assets/downArrow.svg";

const imgSrc = ref(downArrow);
const btnText = ref("展开详细信息");
let descriptionArea;
let height;

onMounted(() => {
  descriptionArea = document.getElementsByClassName("task-description-container")[props.count];
  height = descriptionArea.clientHeight;
  descriptionArea.style.height = "0";

})

const onClickLoadBtn = function () {
  if (isLoaded.value) {
    isLoaded.value = false;
    descriptionArea.style.height = "0";
    btnText.value = "展开详细信息";
    imgSrc.value = downArrow;
  } else {
    isLoaded.value = true;
    imgSrc.value = upArrow;
    btnText.value= "收起详细信息";
    descriptionArea.style.height = `${height}px`;
    console.log(height);
  }
}

const isLoaded = ref(false);

const props = defineProps({
  taskName: {
    type: String,
    required: true
  },
  exp: {
    type: String,
    required: true
  },
  taskDescription: {
    type: String,
    required: true
  },
  count :{
    type:Number,
    required:true
  },
  isFinished :{
    type:Boolean,
    required:true
  }
});

onMounted(() => {
  console.log(props.taskDescription);
})
</script>


<template>
  <div>
     <div class="task-card">
    <div class="task-brief-intro">
      <img class="task-flag-img" src="@/assets/taskFlag.svg" alt="">
      <p class="show-name">{{ props.taskName }}</p>
      <p class="show-exp">经验值:{{ props.exp }}</p>
      <p class="is-finished">已完成</p>
    </div>
    <div class="task-description-container">
      <p class="task-description">{{ props.taskDescription }}</p>
    </div>
    <button  @click="onClickLoadBtn" class="load-btn"><img alt="" :src="imgSrc">{{btnText}}</button>

  </div>
  </div>

</template>

<style scoped>
.task-card {
  border: 2px solid #e4e7ed;
  border-left: 3px solid black;
  margin: 20px;

  & button {
    position: relative;
    border: none;
    cursor: pointer;
    background-color: transparent;
    font-size: 15px;
    left: 40%;
    bottom: 5%;

    & img {
      width: 15px;
    }
  }
}

.task-brief-intro {
  display: flex;

  & .show-exp {
    position: relative;
    left: 20%;
  }

  & .is-finished {
    position: relative;
    left: 40%;
  }

}

.show-name {
  position: relative;

}

.task-flag-img {
  position: relative;
  margin: 10px;
  width: 28px;
}

.task-description-container {
  overflow: hidden;
  transition: height 300ms ease-out 0s;
}

.task-description {
  margin-left: 20px;
  margin-right: 20px;
  padding-top: 10px;
  border-top: 2px solid black;

}

</style>