<template>
    <el-dialog
            :visible.sync="isVisible"
            :before-close="handleDialogClose"
            top="2rem"
            :title="quiz.title"
            class="dialog">

        <quiz-score-component v-if="completedQuiz" :score="score"/>
        <quiz-form-component v-else/>

        <span slot="footer" class="dialog-footer" v-if="!completedQuiz">
          <el-button type="primary" @click="submitAnswers">Submit</el-button>
        </span>
    </el-dialog>
</template>

<script>

import QuizScoreComponent from "@/components/common/QuizScoreComponent.vue";
import QuizFormComponent from "@/components/common/QuizFormComponent.vue";

export default {
    name: "QuizPage",
    components: {QuizFormComponent, QuizScoreComponent},
    data() {
        return {
            isVisible: true,
            quizId: this.$route.params.id,
        };
    },
    computed: {
        quiz() {
          return this.$store.getters['quiz/getQuiz'];
        },
        completedQuizzes() {
            return this.$store.getters['profile/getCompletedQuizzes']
        },
        completedQuiz() {
            return this.completedQuizzes.find(quiz => parseInt(quiz.id) === parseInt(this.quizId));
        },
        score() {
            return this.completedQuiz.score;
        },
    },
    methods: {
        handleDialogClose() {
            this.$confirm('Are you sure to close this dialog?')
                .then(() => {
                    this.$router.push({name: "Quizzes"})
                })
                .catch(() => {})
        },
        submitAnswers() {
            this.$store.dispatch('quiz/submitAnswers', {id: this.quizId})
        }
    },
    mounted() {
        this.$store.dispatch('quiz/loadQuiz', this.quizId);
    }
}
</script>

<style scoped lang="scss">
</style>