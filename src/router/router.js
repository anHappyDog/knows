import {createRouter, createWebHistory} from 'vue-router'
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


const routes = [
    {
        path: "/",
        redirect: "/loginBoard"
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
    // {
    //     path: "/test",
    //     component: Test,
    //     children: [
    //         {
    //             path: "signIn",
    //             name : "signIn",
    //             component: TestSignIn
    //         },
    //         {
    //             path: "signUp",
    //             name:"signUp",
    //             component: TestSignUp
    //         }
    //
    //     ]
    // },
    {
        path: "/articleList",
        component: ArticleList
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;