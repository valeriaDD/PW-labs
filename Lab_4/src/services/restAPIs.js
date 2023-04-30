import httpClient from "@/services/HttpClient";

export const createUser = ({name, surname}) => httpClient.post('/users', {
    name: name,
    surname: surname,
});

const showQuizzes = () => httpClient.post('/quizzes');

const getQuiz = (id) => httpClient.get(`/quizzes/${id}`);

const submitQuiz = (id) => httpClient.post(`/quizzes/${id}/submit`);

export default {
    createUser,
    showQuizzes,
    getQuiz,
    submitQuiz,
}