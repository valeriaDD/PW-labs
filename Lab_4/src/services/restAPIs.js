import httpClient from "@/services/HttpClient";

export const createUser = ({name, surname}) => httpClient.post('/users', {
    name: name,
    surname: surname,
});
export const getQuizzes = () => httpClient.get('/quizzes', {});

export const getQuiz = (id) => httpClient.get(`/quizzes/${id}`, {});

export const submitQuiz = (id, params) => httpClient.post(`/quizzes/${id}/submit`, params);