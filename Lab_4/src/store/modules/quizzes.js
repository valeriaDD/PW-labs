import {getQuizzes} from "@/services/restAPIs";

const state = {
    quizzes: [],
    request: {
        started: false,
    }
};

const getters = {
    getQuizzes(state) {
        return state.quizzes;
    }
};

const actions = {
    async loadQuizzes({commit}) {
        commit("SET_REQUEST_START");
        try {
            const response = await getQuizzes();
            commit("SET_QUIZZES", response);
            commit("SET_REQUEST_END");
        } catch (e) {
            commit("SET_REQUEST_END");
        }
    },
};

const mutations = {
    SET_QUIZZES(state, quizzes) {
        state.quizzes = quizzes;
    },
    SET_REQUEST_START(state) {
        state.request.started = true;
    },
    SET_REQUEST_END(state) {
        state.request.started = false;
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}