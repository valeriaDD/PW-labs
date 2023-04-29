<template>
  <div class="quiz__questions">
    <el-form>
      <question-component/>
      <question-component/>
    </el-form>
  </div>
</template>

<script>
import QuestionComponent from "@/components/common/QuestionComponent.vue";

export default {
  name: "QuizFormComponent",
  components: {QuestionComponent}
}
</script>

<style scoped>

</style>