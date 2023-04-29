<template>
  <div class="question">
    <div class="question__title">
      <span> 1. </span> <span> How many legs does a spider have?</span>
    </div>
    <el-form-item :error="'Correct answer is miaw'">
      <el-radio-group class="answers" v-model="value">
        <el-radio label="1" class="radio-button">Option AAOption AOption AOptioOption AAOption AOption AOption AOption
          AOption AOption AOption A
        </el-radio>
        <el-radio label="2" class="radio-button">Option B</el-radio>
        <el-radio label="2" class="radio-button">Option B Option B Option B Option B </el-radio>
        <el-radio label="2" class="radio-button">Option B</el-radio>
        <el-radio label="2" class="radio-button">Option B</el-radio>
        <el-radio label="2" class="radio-button">Option B</el-radio>
        <el-radio label="2" class="radio-button">Option B</el-radio>
        <el-radio label="2" class="radio-button">Option B</el-radio>
        <el-radio label="2" class="radio-button">Option B</el-radio>
        <el-radio label="2" class="radio-button">Option B</el-radio>
        <el-radio label="2" class="radio-button">Option B Option BOption B Option BOption B Option B</el-radio>
        <el-radio label="2" class="radio-button">Option B</el-radio>
      </el-radio-group>
    </el-form-item>
  </div>
</template>

<script>
export default {
  name: "QuestionComponent",
  data() {
    return {
      value: '',
    };
  }
}
</script>

<style scoped lang="scss">
.question {
  .question__title {
    font-weight: bolder;
    font-size: 1rem;
  }

  .answers {
    margin-top: 1rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
  }
}
</style>