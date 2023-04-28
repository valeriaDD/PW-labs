import Vue from "vue";
import VueRouter from "vue-router";
import DashboardPage from "@/components/DashboardPage.vue";
import QuizzesPage from "@/components/QuizzesPage.vue";
import QuizPage from "@/components/QuizPage.vue";

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
        component: QuizzesPage
    },
    {
        path: '/quizzes/1',
        name: 'Quiz',
        component: QuizPage
    },
];

const router = new VueRouter({
    routes,
    mode: 'history'
})

export default router;
