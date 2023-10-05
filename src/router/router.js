import {createRouter, createWebHistory} from 'vue-router'
import SignIn from "@/components/LoginBoard/subComponent/SignIn.vue";
import SignUp from "@/components/LoginBoard/subComponent/SignUp.vue";
import Test2 from "@/components/LoginBoard/LoginBoard.vue";
import MainPage from "@/components/MainPage/MainPage.vue";
import LoginBoard from "@/components/LoginBoard/LoginBoard.vue";
import UserProfile from "@/components/UserProfile/UserProfile.vue";
import ArticleRank from "@/components/ArticleRank/ArticleRank.vue";
import WriteArticle from "@/components/WriteArticle/WriteArticle.vue";
import Category from "@/components/Category/Category.vue";
import TaskBoard from "@/components/TaskBoard/TaskBoard.vue";
import ArticleListCard from "@/components/ArticleList/ArticleList.vue";
import Test from "@/components/Test.vue";
import ArticleList from "@/components/ArticleList/ArticleList.vue";
import TestSignIn from "@/components/TestSignIn.vue";
import TestSignUp from "@/components/TestSignUp.vue";

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
    {
        path: "/test",
        component: Test,
        children: [
            {
                path: "signIn",
                component: TestSignIn
            },
            {
                path: "signUp",
                component: TestSignUp
            }

        ]
    },
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