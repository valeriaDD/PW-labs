import {getQuiz, submitQuiz} from "@/services/restAPIs";

const state = {
    quiz: {},
    questionsCount: 0,
    correctAnswersCount: 0,
    answers: [],
    request: {
        started: false,
    }
};

const getters = {
    getQuiz(state) {
        return state.quiz;
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
    async submitAnswers({commit, rootGetters, state, dispatch}, {id}) {
        commit("SET_REQUEST_START");
        try {
            const userId = await rootGetters['profile/getUser']
            await commit("ADD_USER_ID_TO_ANSWERS", userId)

            for (const answer of state.answers) {
                let response = await submitQuiz(id, answer);
                commit("ADD_ANSWER_RESULTS", {questionId: answer.question_id, response: response})
            }

            dispatch("countCorrectAnswers");
            commit("SET_REQUEST_END");
        } catch (e) {
            console.log(e)
            commit("SET_REQUEST_END");
        }
    },
    countCorrectAnswers({commit, state, dispatch}) {
        commit("COUNT_CORRECT_ANSWERS")
        const score = `${state.correctAnswersCount}/${state.questionsCount}`
        dispatch("profile/addFinishedQuiz", {id: state.quiz.id, score: score}, { root: true });
    },
    addAnswer({commit}, {question, answer}) {
        commit("ADD_ANSWER", {question: question, answer: answer});
    }
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
        const result = state.answers.find(item => parseInt(item.question_id) === parseInt(question))

        if (result) {
            result.answer = answer;
        } else {
            state.answers.push({
                question_id: question,
                answer: answer,
                user_id: undefined,
                correct: undefined,
                correct_answer: undefined,
            })
        }
    },
    ADD_USER_ID_TO_ANSWERS(state, user_id) {
        state.answers.forEach(answer => answer.user_id = user_id)
    },
    ADD_ANSWER_RESULTS(state, {questionId, response}) {
        const result = state.answers.find(item => parseInt(item.question_id) === parseInt(questionId))

        if (result) {
            result.correct = response.correct;
            result.correct_answer = response.correct_answer;
        }
    },
    COUNT_CORRECT_ANSWERS(state) {
        state.correctAnswersCount = state.answers.filter(answer => answer.correct).length;
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}