import { createApp,ref} from 'vue';
import '@mdi/font/css/materialdesignicons.min.css';
import './style.css';
import router from './router'
import App from './App.vue';
import axios from 'axios';
import VueCookies from 'vue3-cookies';

//! for Vuetify
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
//!

//! this is used for the markdown editor
import createVideoPlugin from './md_plugins/video_plugin.js';
// highlightjs
import hljs from 'highlight.js';
import VMdPreview from '@kangc/v-md-editor/lib/preview';
import VMdEditor from '@kangc/v-md-editor/lib/codemirror-editor';
import '@kangc/v-md-editor/lib/style/codemirror-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
// codemirror 编辑器的相关资源
import Codemirror from 'codemirror';
// mode
import 'codemirror/mode/markdown/markdown';
import 'codemirror/mode/javascript/javascript';
import 'codemirror/mode/css/css';
import 'codemirror/mode/htmlmixed/htmlmixed';
import 'codemirror/mode/vue/vue';
// edit
import 'codemirror/addon/edit/closebrackets';
import 'codemirror/addon/edit/closetag';
import 'codemirror/addon/edit/matchbrackets';
// placeholder
import 'codemirror/addon/display/placeholder';
// active-line
import 'codemirror/addon/selection/active-line';
// scrollbar
import 'codemirror/addon/scroll/simplescrollbars';
import 'codemirror/addon/scroll/simplescrollbars.css';
// style
import 'codemirror/lib/codemirror.css';
//!

const vuetify = createVuetify({
  components,
  directives,
});

axios.defaults.baseURL = 'https://database.api.lonelywatch.com';
axios.defaults.withCredentials = true;
VMdEditor.Codemirror = Codemirror;

VMdEditor.use(githubTheme,{
  Hljs: hljs,
}).use(createVideoPlugin());

VMdPreview.use(githubTheme,{
  Hljs: hljs,
}).use(createVideoPlugin());


const loading = ref(false);
const app = createApp(App);

app.provide('loading',loading);
router.setLoading = function (value) {
  loading.value = value;
};
app.use(VueCookies).use(router).use(VMdPreview)
.use(VMdEditor).use(vuetify).mount('#app');
