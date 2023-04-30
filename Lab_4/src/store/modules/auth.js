const state = {
    token: "5d98f8bafbecc2328fbc24bc63fe400257844e2bd0c1a5340305ac04ef4b284f",
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