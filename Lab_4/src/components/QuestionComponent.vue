<template>
  <div class="question">
    <div class="question__title">
      <span> 1. </span> <span> How many legs has a spider?</span>
    </div>
    <el-form-item>
      <el-radio-group  class="answers" v-model="value">
        <el-radio  label="1" >Option AAOption AOption AOption AOption AOption AOption AOption A</el-radio>
        <el-radio  label="2" >Option B</el-radio>
        <el-radio  label="2" >Option B</el-radio>
        <el-radio  label="2" >Option B</el-radio>
        <el-radio  label="2" >Option B</el-radio>
        <el-radio  label="2" >Option B</el-radio>
        <el-radio  label="2" >Option B</el-radio>
        <el-radio  label="2" >Option B</el-radio>
        <el-radio  label="2" >Option B</el-radio>
        <el-radio  label="2" >Option B</el-radio>
        <el-radio  label="2" >Option B</el-radio>
        <el-radio  label="2" >Option B</el-radio>
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
  .answers {
    margin-top: 1rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
  }
}
</style>