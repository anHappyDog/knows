import {createRouter, createWebHistory} from 'vue-router'
import SignIn from "@/components/LoginBoard/subComponent/SignIn.vue";
import SignUp from "@/components/LoginBoard/subComponent/SignUp.vue";
import Test2 from "@/components/LoginBoard/LoginBoard.vue";
import MainPage from "@/components/MainPage.vue";
import LoginBoard from "@/components/LoginBoard/LoginBoard.vue";
import UserProfile from "@/components/UserProfile/UserProfile.vue";

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
        component: null
    },
    {
        path: "/category",
        component: null
    },
    {
        path: "/writeArticle",
        component: null
    },
    {
        path: "/articleRank",
        component: null
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;