<template>
    <div class="question">
        <div class="question__title">
            <span> {{number ?? ''}}. </span> <span> {{question.question}}</span>
        </div>
        <el-form-item :error="''">
            <el-radio-group class="answers" v-model="value" @change="addAnswer">
                <el-radio :label="answer" class="radio-button" v-for="(answer, index) in question.answers" :key="index"/>
            </el-radio-group>
        </el-form-item>
    </div>
</template>

<script>
export default {
    name: "QuestionComponent",
    props: {
        question: {
            type: Object,
            required: true,
        },
        number: {
            type: Number,
            default: null,
        }
    },
    data() {
        return {
            value: '',
        };
    },
    methods: {
        addAnswer(value) {
            this.$store.dispatch("quiz/addAnswer", {
                question: this.question?.id,
                answer: value,
            })
        }
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