<template>
    <div class="home">
        <div class="left-menu">
            <el-menu
                    style="height: 100%;"
                    default-active="2"
                    class="el-menu-vertical-demo"
                    background-color="#304156"
                    active-text-color="#409eff"
                    text-color="#fff">

                        <el-menu-item index="1" style="text-align: left">
                            <i class="el-icon-menu"></i>
                            <span slot="title">服务</span>
                        </el-menu-item>
                        <el-menu-item index="2" style="text-align: left">
                            <i class="el-icon-setting"></i>
                            <span slot="title">任务</span>
                        </el-menu-item>
                        <el-menu-item index="3" style="text-align: left">
                            <i class="el-icon-user"></i>
                            <span slot="title">退出登录</span>
                        </el-menu-item>
            </el-menu>
        </div>

        <div class="right-context"></div>
    </div>
</template>

<script>
    // @ is an alias to /src

    export default {
        name: 'home',
        components: {},
        props: {
            arg: String,
        },
        date() {
            return {
                message: 'message'
            }
        },
        methods: {},
        created() {
        },

    }
</script>

<style scoped>
    .home {
        display: flex;
        height: 100%;
    }
    .left-menu {
        width: 15%;
    }
    .right-context {
        width: 85%;
    }
</style>