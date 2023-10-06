<script setup>
import NavigationBar from "@/components/NavigationBar/NavigationBar.vue";
import {reactive} from "vue";
import TaskCard from "@/components/TaskBoard/TaskCard.vue";

const taskData = reactive([{
  taskId: 1,
  taskName: "登录",
  isFinished: false,
  exp: "15",
  taskDescription: "This is a description of the task"
},
  {taskId: 2, taskName: "登录", isFinished: false, exp: "15", taskDescription: "This is a description of the task"},
{taskId: 3, taskName: "登录", isFinished: false, exp: "15", taskDescription: "This is a description of the task"},
{taskId: 4, taskName: "登录", isFinished: false, exp: "15", taskDescription: "This is a description of the task"},
{taskId: 5, taskName: "登录", isFinished: false, exp: "15", taskDescription: "This is a description of the task"}]);


</script>

<template>
  <header>
    <NavigationBar/>
  </header>
  <div id="task-container">
    <p id="everyday-task-description">每日任务:</p>
    <div id="task-card-container">
      <TaskCard v-for="(task,index) in taskData" :task-description="task.taskDescription" :exp="task.exp"
                :task-name="task.taskName" :key="task.taskId" :count="index" :isFinished="true"></TaskCard>
    </div>
  </div>
</template>

<style scoped>

#task-card-container {
  position: relative;
  left: 10%;
  height: auto;
  width: 80%;
}

#task-container {
  position: absolute;
  left: 250px;
  width: 1000px;
  margin: 10px;
  border: 2px solid #e4e7ed;
  border-top: 4px solid black;
  box-shadow: 0 1px 3px hsla(0, 0%, 7%, .1);

  height: auto;
  background-color: white;

  & #everyday-task-description {
    font-size: 18px;
    width: 25%;
    margin-top: 40px;
    margin-left: 40px;
    border-bottom: 2px solid black;
  }
}


</style>