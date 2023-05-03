const state = {
    token: "176687918888c30addfa5b2e7e21dd6627221005dfedb44f7d17d3c7e2254e8a",
};

const getters = {
    getToken(state) {
        return state.token;
    }
};

export default {
    namespaced: true,
    state,
    getters,
}