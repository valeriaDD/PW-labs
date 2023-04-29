import Vue from "vue";
import VueRouter from "vue-router";
import DashboardPage from "@/components/DashboardPage.vue";
import QuizzesPage from "@/components/QuizzesPage.vue";
import QuizPage from "@/components/QuizPage.vue";
import ErrorPage from "@/components/ErrorPage.vue";

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Dashboard',
        component: DashboardPage
    },
    {
        path: '/quizzes',
        name: 'Quizzes',
        component: QuizzesPage,
        children: [
            {
                path: '/quizzes/:id',
                name: 'Quiz',
                component: QuizPage,
                beforeEnter: (to, from, next) => isNaN(to.params.id) ? next(ErrorPage) : next(),
            },
        ]
    },
    {
        path: "*",
        name: "ErrorPage",
        component: ErrorPage
    }
];

const router = new VueRouter({
    routes,
    mode: 'history'
})

export default router;
