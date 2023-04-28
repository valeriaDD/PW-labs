<template>
<div class="container gradient--purple">
  <el-col class="quiz" :lg="16" :sm="18" :xs="23">
    <div class="quiz__title"> The title of the quiz will be here!</div>
    <div class="quiz__questions">
      <el-form>
      <question-component/>
      <question-component/>
      </el-form>
    </div>
  </el-col>
</div>
</template>

<script>
import QuestionComponent from "@/components/QuestionComponent.vue";

export default {
  name: "QuizPage",
  components: {QuestionComponent}
}
</script>

<style scoped lang="scss">
.container {
  padding: 5rem;
  min-height: calc(100vh - 10rem);
  display: flex;
  justify-content: center;

  .quiz {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    padding: 2rem;
    border-radius: 0.5rem;
    background: rgba(255, 255, 255, 0.7);

    &__title {
      text-align: center;
      font-size: 1.5rem;
      font-weight: bold;
    }

    &__questions {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
  }
}
</style>