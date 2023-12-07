import { createRouter, createWebHistory } from "vue-router";
import {inject} from "vue";
import SignIn from "./components/Login/SignIn.vue";
import SignUp from "./components/Login/SignUp.vue";
import MainPage from "./components/MainPage.vue";
import Articles from "./components/Article/Articles.vue";
import Article from "./components/Article/Article.vue";
import NewArticle from "./components/Article/NewArticle.vue";
import UserInfo from "./components/User/UserInfo.vue";
import Categories from "./components/Category/Categories.vue";
import NewCategory from "./components/Category/NewCategory.vue";
import Category from "./components/Category/Category.vue";
import ArticleSearch from "./components/Article/ArticleSearch.vue";
const routes = [
  { path: "/", component: SignIn, name: "SignIn" },
  { path: "/SignUp", component: SignUp, name: "SignUp" },
  {
    path: "/SignIn",
    component: SignIn,
    name: "SignIn",
  },
  {
    path: "/main",
    component: MainPage,
    name: "main",
    children: [
      {
        path: "articles",
        component: Articles,
        name: "articles",
      },
      {
        path: "article/:id",
        component: Article,
        name: "articleDetail",

      },
      {
        path: "newArticle",
        component: NewArticle,
        name: "newArticle",
      },
      { path: "/", redirect: { name: "articles" } },
      {
        path: "user/:user_id",
        component: UserInfo,
        name: "userInfo",
        
      },
      {
        path: "categories",
        component: Categories,
        name: "categories",
      },
      {
        path: "newCategory",
        component: NewCategory,
        name: "newCategory",
      },
      {
        path: "category/:category_id",
        component: Category,
        name: "category",
      },
      {
        path: "feedbacks",
        component: () => import("./components/Feedback/Feedbacks.vue"),
        name: "feedbacks",
      },
      {
        path: "feedback/:feedback_id",
        component: () => import("./components/Feedback/Feedback.vue"),
        name: "feedback",
      },
      {
        path: "newFeedback",
        component: () => import("./components/Feedback/NewFeedback.vue"),
        name: "newFeedback",
      }
    ],
  },
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
router.beforeEach((to, from) => {
  console.log("your god");
  router.setLoading(true);
  if (to.name === "SignIn" || to.name === "SignUp") {
    if (localStorage.getItem("token")) {
      return { name: "main" };
    }
    return true;
  } else {
    if (localStorage.getItem("token")) {
      return true;
    } else {
      return { name: "SignIn" };
    }
  }
});
router.afterEach(() => {
  console.log("my love");
  router.setLoading(false);
});
export default router;
