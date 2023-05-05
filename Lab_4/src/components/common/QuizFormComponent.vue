<template>
    <div class="quiz__questions">
        <quiz-score-component v-if="score" :score="score" :imgHeight="100"/>
        <el-form>
            <question-component
                v-for="(question, index) in questions"
                :key="question.id"
                :question="question"
                :correct = question.correct
                :number="index + 1"/>
        </el-form>
    </div>
</template>

<script>
import QuestionComponent from "@/components/common/QuestionComponent.vue";
import QuizScoreComponent from "@/components/common/QuizScoreComponent.vue";

export default {
    name: "QuizFormComponent",
    components: {QuizScoreComponent, QuestionComponent},
    data() {
        return {
            value: {},
        }
    },
    computed: {
        quiz() {
            return this.$store.getters["quiz/getQuiz"];
        },
        questions() {
            return this.quiz.questions;
        },
        score() {
            return this.$store.getters["quiz/getScore"];
        },
    },
    methods: {
        validateAnswers(rule, value, callback) {
            const unansweredQuestions = this.questions.filter(q => !q.answered);
            if (unansweredQuestions.length > 0) {
                callback(new Error(`Please answer question ${unansweredQuestions[0].id}`));
            } else {
                callback();
            }
        }
    }
}
</script>

<style scoped>

</style>