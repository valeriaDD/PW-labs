import {getQuiz, submitQuiz} from "@/services/restAPIs";

const state = {
    quiz: {},
    questionsCount: 0,
    correctAnswersCount: 0,
    score: undefined,
    request: {
        started: false,
    }
};

const getters = {
    getQuiz(state) {
        return state.quiz;
    },
    getScore(state) {
        return state.score;
    }
};

const actions = {
    async loadQuiz({commit}, id) {
        commit("SET_REQUEST_START");
        try {
            const response = await getQuiz(id);
            commit("SET_QUIZ", response);
            commit("SET_REQUEST_END");
        } catch (e) {
            commit("SET_REQUEST_END");
        }
    },
    async submitAnswers({commit, rootGetters, state}, {id}) {
        commit("SET_REQUEST_START");
        try {
            const userId = await rootGetters['profile/getUser']

            for (const question of state.quiz.questions) {
                let response = await submitQuiz(id, {
                    user_id: userId,
                    question_id: question.id,
                    answer: question.userChoice ?? '',
                });

                commit("ADD_ANSWER_RESULTS", {questionId: question.id, response: response})
            }

            commit("COUNT_CORRECT_ANSWERS")
            commit("SET_REQUEST_END");
        } catch (e) {
            commit("SET_REQUEST_END");
        }
    },
    addAnswer({commit}, {question, answer}) {
        commit("ADD_ANSWER", {question: question, answer: answer});
    },
    reset({commit}) {
        commit("RESET_QUIZ_DATA");
    },
};

const mutations = {
    SET_QUIZ(state, quiz) {
        state.quiz = quiz;
        state.questionsCount = quiz.questions?.length
    },
    SET_REQUEST_START(state) {
        state.request.started = true;
    },
    SET_REQUEST_END(state) {
        state.request.started = false;
    },
    ADD_ANSWER(state, {question, answer}) {
        const result = state.quiz.questions.find(item => parseInt(item.id) === parseInt(question))

        if (result) {
            result.userChoice = answer;
        }
    },
    ADD_ANSWER_RESULTS(state, {questionId, response}) {
        let quizAnswer = state.quiz.questions.find((item) => parseInt(item.id) === parseInt(questionId))

        if (quizAnswer) {
            quizAnswer.correct = response.correct;
            quizAnswer.correct_answer = response.correct_answer;
        }

        state.quiz = {...state.quiz}
    },
    COUNT_CORRECT_ANSWERS(state) {
        state.correctAnswersCount = state.quiz.questions.filter(answer => answer.correct).length;
        state.score = `${state.correctAnswersCount}/${state.questionsCount}`;
    },
    RESET_QUIZ_DATA(state) {
        state.quiz = {};
        state.questionsCount = 0;
        state.score = undefined;
        state.correctAnswersCount = 0;
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}