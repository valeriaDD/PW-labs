import {createUser} from "@/services/restAPIs";

const state = {
    userId: localStorage.getItem('id') ?? undefined,
    completedQuizzes:  localStorage.getItem('completed') ?? [],
    request: {
        started: false,
    },
};

const getters = {
    getUser(state) {
        return state.userId
    },
    getCompletedQuizzes(state) {
        return state.completedQuizzes
    }
};

const actions = {
    async createUser({commit}, {name, surname}) {
        commit("SET_REQUEST_START");
        try {
            const response = await createUser({name: name, surname: surname})
            commit("SET_USER", response);
            commit("SET_REQUEST_END");
        } catch (e) {
            commit("SET_REQUEST_END");
        }
    },
    addFinishedQuiz({commit}, {id, score}) {
        commit("ADD_COMPLETED_QUIZ", id, score)
    },
    logout({ commit }) {
        commit('REMOVE_USER')
    },
};

const mutations = {
    SET_USER(state, user) {
      state.userId = user.id;
      localStorage.setItem('id', user.id);
    },
    REMOVE_USER(state) {
        state.userId = undefined;
        localStorage.removeItem('id');
    },
    ADD_COMPLETED_QUIZ(state, id, score) {
        state.completedQuizzes.push({id: id, score:score})
        localStorage.setItem('completed', state.completedQuizzes);
    },
    SET_REQUEST_START(state) {
        state.request.started = true;
    },
    SET_REQUEST_END(state) {
        state.request.started = false;
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}