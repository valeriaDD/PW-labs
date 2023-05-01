import Vue from "vue";
import VueRouter from "vue-router";
import DashboardPage from "@/components/DashboardPage.vue";
import QuizzesPage from "@/components/QuizzesPage.vue";
import QuizPage from "@/components/QuizPage.vue";
import ErrorPage from "@/components/ErrorPage.vue";
import store from "@/store";

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

router.beforeEach(async (to, from, next) => {
    if (!store.getters['profile/getUser'] && to.name !== 'Dashboard') {
        return next({ name: 'Dashboard' })
    }

    if (store.getters['profile/getUser'] && to.name === 'Dashboard') {
        return next({ name: 'Quizzes' })
    }

    return next()
})

export default router;
