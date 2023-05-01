import Vue from 'vue'
import Vuex from 'vuex'
import auth from "@/store/modules/auth.js";
import profile from "@/store/modules/profile.js";
import quizzes from "@/store/modules/quizzes.js";
import quiz from "@/store/modules/quiz";

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        auth,
        profile,
        quizzes,
        quiz,
    }
});
