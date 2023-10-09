import './assets/main.css';
import router from "@/router/router";
import {createApp} from 'vue';
import App from './App.vue';
import VMdEditor from '@kangc/v-md-editor'
import githubTheme from '@kangc/v-md-editor/lib/theme/github'
import '@kangc/v-md-editor/lib/theme/style/github.css'
import hljs from "highlight.js";
import '@kangc/v-md-editor/lib/style/base-editor.css';
import axios from "axios";
import VueCookies from 'vue3-cookies';
import {useCookies} from "vue3-cookies";

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://127.0.0.1:8000"

axios.interceptors.response.use(response => response, async err => {
    if (err.response.status === 403) {
        await axios.get(axios.defaults.baseURL + "/api/getCsrfToken").then(response => {
            console.log(response);
            useCookies().cookies.set('csrfToken',response.data["csrfToken"]);
        }).catch(err => {
            return Promise.reject(err);
        });
        return axios.request(err.config);
    } else {
        return Promise.reject(err);
    }
});

axios.interceptors.request.use(
    config => {
        const cookies = useCookies();
        if (cookies.cookies) {
            config.headers['csrfToken'] = cookies.cookies.get("csrfToken");
        }
        return config;
    },
    error => {
        return Promise.reject(error);
    }
)

createApp(App).use(VueCookies).use(VMdEditor).use(router).mount('#app');
