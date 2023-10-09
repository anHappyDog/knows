import {createRouter, createWebHashHistory} from 'vue-router'
import SignIn from "@/components/LoginBoard/SignIn.vue";
import SignUp from "@/components/LoginBoard/SignUp.vue";
import MainPage from "@/components/MainPage/MainPage.vue";
import LoginBoard from "@/components/LoginBoard/LoginBoard.vue";
import UserProfile from "@/components/UserProfile/UserProfile.vue";
import ArticleRank from "@/components/ArticleRank/ArticleRank.vue";
import WriteArticle from "@/components/WriteArticle/WriteArticle.vue";
import Category from "@/components/Category/Category.vue";
import TaskBoard from "@/components/TaskBoard/TaskBoard.vue";
import ArticleList from "@/components/ArticleList/ArticleList.vue";
import FriendBoard from "@/components/FriendBoard/FriendBoard.vue";
import ArticleShow from "@/components/ArticleShow.vue";
import SearchResult from "@/components/SearchResult/SearchResult.vue";
import axios from "axios";
import {useCookies} from 'vue3-cookies';
import UploadImgBoard from "@/components/WriteArticle/UploadImgBoard.vue";


const cookies = useCookies();

const routes = [
    {
        path: "/",
        redirect: "/loginBoard/signIn"
    },
    {
        path: "/loginBoard",
        component: LoginBoard,
        children: [
            {
                path: "",
                redirect: "/loginBoard/signIn"
            },
            {
                path: "signIn",
                component: SignIn,
                name: "signIn"
            },
            {
                path: "signUp",
                component: SignUp,
                name: "signUp"
            }
        ]
    },
    {
        path: "/mainPage",
        component: MainPage
    },
    {
        path: "/userProfile",
        component: UserProfile
    },
    {
        path: "/taskBoard",
        component: TaskBoard
    },
    {
        path: "/category",
        component: Category
    },
    {
        path: "/writeArticle",
        component: WriteArticle
    },
    {
        path: "/articleRank",
        component: ArticleRank
    },
    {
        path: "/friendBoard",
        component: FriendBoard,
    },
    {
        path: "/article/:articleId",
        component: ArticleShow
    },
    {
        path: "/searchResult",
        component: SearchResult
    },
    {
        path: "/articleList",
        component: ArticleList
    },
    {
        path: "/uploadTest",
        component: UploadImgBoard
    },


]

const router = createRouter({
    history: createWebHashHistory(),
    routes
});

const isValidSessionId = async function () {
    try {
        const result = await axios.get(axios.defaults.baseURL + "/api/validSessionToken");
        return result.data;
    } catch (err) {
        console.log(err);
    }
}



//应该要在失败后做出一些提示
router.beforeEach((to, from, next) => {
    if (to.path === "/loginBoard/signIn") {
        next();
    } else {
        isValidSessionId().then(
            result => {
                if (result["status"] === 0) {
                    next();
                } else {
                    next("/loginBoard/signIn");
                }
            }
        ).catch(err => {
            console.log(err);
        })
    }
});

export default router;