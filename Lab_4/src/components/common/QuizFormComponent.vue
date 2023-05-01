<template>
    <div class="quiz__questions">
        <el-form>
            <question-component
                v-for="(question, index) in questions"
                :key="question.id"
                :question="question"
                :number="index + 1"/>
        </el-form>
    </div>
</template>

<script>
import QuestionComponent from "@/components/common/QuestionComponent.vue";

export default {
    name: "QuizFormComponent",
    components: {QuestionComponent},
    computed: {
        quiz() {
            return this.$store.getters["quiz/getQuiz"];
        },
        questions() {
            return this.quiz.questions;
        }
    },
}
</script>

<style scoped>

</style>