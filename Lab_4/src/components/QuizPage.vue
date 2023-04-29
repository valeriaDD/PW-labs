<template>
  <el-dialog
      :visible.sync="isVisible"
      @close="handleDialogClose"
      :title="'The of the quiz will be here!'"
      class="dialog">
    <quiz-score-component/>

    <span slot="footer" class="dialog-footer">
    <el-button type="primary" @click="handleDialogClose">Submit</el-button>
  </span>
  </el-dialog>
</template>

<script>

import QuizScoreComponent from "@/components/common/QuizScoreComponent.vue";

export default {
  name: "QuizPage",
  components: {QuizScoreComponent},
  data() {
    return {
      isVisible: true,
    };
  },
  methods: {
    handleDialogClose() {
      this.$router.push({name: "Quizzes"})
    }
  }
}
</script>

<style scoped lang="scss">
</style>