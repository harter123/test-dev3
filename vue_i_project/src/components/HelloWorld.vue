<template>
    <div class="hello">
        {{message}}
        {{myProps}}
        <div v-html="htmlMessage"></div>

        <div :id="idMessage" name="hello" :class="classMessage">
qqqqqqq
        </div>


        <div v-if="boolMessage">
            v-if {{boolMessage}}
        </div>
        <div v-else>
            v-else {{boolMessage}}
        </div>

        <div v-show="showMessage">
            v-show {{showMessage}}
        </div>


        <div v-for="item in listMessage" :key="item">
            {{item}}
        </div>

        <el-button onclick="alert(1)">纯js button</el-button>
        <el-button @click="buttonEvent">vue button</el-button>


        <el-input v-model="inputMessage"/>
        <div>
            {{inputMessage}}
        </div>
        <el-button @click="inputEvent">input button</el-button>

    </div>
</template>

<script>
    export default {
        name: 'HelloWorld',
        props: {
            msg: String,
            myProps: String,
        },
        data() {
            return {
                message: "hi 海贼",
                htmlMessage: "<span style='color: crimson'> hi 海贼</span>",
                idMessage: "hiHelloWorld",
                classMessage: 'hiHelloWorld',

                boolMessage: false,
                showMessage: false,

                listMessage: ["a", "b", "c"],

                inputMessage: "input",
            }
        },
        methods: {
            buttonEvent(){
              this.showMessage = !this.showMessage;
            },
            inputEvent(){
                this.inputMessage = "input"
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h3 {
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
    .hiHelloWorld {
        color: aqua;
    }
</style>
