<template>
    <el-dialog
            :visible.sync="isVisible"
            :before-close="handleDialogClose"
            top="2rem"
            :title="quiz.title"
            class="dialog">

        <quiz-score-component v-if="completedQuiz" :score="completedQuizScore"/>
        <quiz-form-component v-else/>

        <span slot="footer" class="dialog-footer" v-if="!completedQuiz">
          <el-button type="primary" @click="submitAnswers">{{inReview ? 'Ok' : 'Submit' }}</el-button>
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
        completedQuizScore() {
            return this.completedQuiz.score;
        },
        score() {
            return this.$store.getters['quiz/getScore'];
        },
        inReview() {
            return typeof this.score !== 'undefined';
        },
    },
    methods: {
        handleDialogClose() {
            this.$confirm('Are you sure to close this dialog?')
                .then(() => {
                    if (this.inReview) {
                        this.pushToStorage()
                    }
                    this.$router.push({name: "Quizzes"})
                })
                .catch(() => {})
        },
        pushToStorage() {
            this.$store.dispatch('profile/addFinishedQuiz', {
                id: this.quizId,
                score: this.score,
            });
        },
        submitAnswers() {
            if (this.inReview) {
                this.$store.dispatch('profile/addFinishedQuiz', {
                    id: this.quizId,
                    score: this.score,
                });

                this.$router.push({name: "Quizzes"})
            } else {
                this.$store.dispatch('quiz/submitAnswers', {id: this.quizId})
            }
        }
    },
    beforeCreate() {
        this.$store.dispatch('quiz/loadQuiz', this.$route.params.id);
    },
    destroyed() {
        this.$store.dispatch('quiz/reset');
    }
}
</script>

<style scoped lang="scss">
</style>