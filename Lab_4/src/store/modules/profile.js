import {createUser} from "@/services/restAPIs";

const state = {
    user: {},
    request: {
        profile: false,
    },
};

const getters = {
    getUser(state) {
        return state.user
    }
};

const actions = {
    async createUser({commit}, {name, surname}) {
        commit("SET_REQUEST_START");
        try {
            const response = await createUser({name: name, surname: surname})
            console.log(response);
            commit("SET_REQUEST_END");
        } catch (e) {
            commit("SET_REQUEST_END");
        }
    }
};

const mutations = {
    SET_REQUEST_START(state) {
        state.request.profile = true;
    },
    SET_REQUEST_END(state) {
        state.request.profile = false;
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}