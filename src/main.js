import './assets/main.css';
import router from "@/router/router";
import { createApp } from 'vue';
import App from './App.vue';
import VMdEditor from '@kangc/v-md-editor'
import githubTheme from '@kangc/v-md-editor/lib/theme/github'
import '@kangc/v-md-editor/lib/theme/style/github.css'
import hljs from "highlight.js";
import '@kangc/v-md-editor/lib/style/base-editor.css';


VMdEditor.use(githubTheme,{
    Hljs:hljs
});

createApp(App).use(VMdEditor).use(router).mount('#app')
