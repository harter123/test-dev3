<template>
    <div class="home">
        <div class="left-menu">
            <el-menu
                    style="height: 100%;"
                    :default-active="activeIndex"
                    class="el-menu-vertical-demo"
                    background-color="#304156"
                    active-text-color="#409eff"
                    @select="handleSelect"
                    text-color="#fff">

                <el-menu-item index="service" style="text-align: left">
                    <i class="el-icon-menu"></i>
                    <span slot="title">服务</span>
                </el-menu-item>
                <el-menu-item index="interface" style="text-align: left">
                    <i class="el-icon-star-on"></i>
                    <span slot="title">接口</span>
                </el-menu-item>
                <el-menu-item index="task" style="text-align: left">
                    <i class="el-icon-setting"></i>
                    <span slot="title">任务</span>
                </el-menu-item>
                <el-menu-item index="logout" style="text-align: left">
                    <i class="el-icon-user"></i>
                    <span slot="title">退出登录</span>
                </el-menu-item>
            </el-menu>
        </div>

        <div class="right-context">
            <router-view/>
        </div>
    </div>
</template>

<script>
    // @ is an alias to /src
    import {logout} from "../request/user";

    export default {
        name: 'home',
        props: {
            menu: String
        },
        components: {},
        data() {
            return {
                activeIndex: "service",
            }
        },
        methods: {
            logoutUser() {
                logout().then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.$router.push('/login')
                    } else {
                        this.$notify.error({
                            title: '错误',
                            message: '请求失败'
                        });
                    }
                });
            },
            handleSelect(index, keyPath) {
                this.activeIndex = index;
                switch (index) {
                    case "logout":
                        this.logoutUser();
                        break;
                    case "service":
                        this.$router.push('/service');
                        break;
                    case "interface":
                        this.$router.push('/interface');
                        break;
                    case "task":
                        this.$router.push('/task');
                        break;
                }
            },
            // initMenu() {
            //     //indexOf 代表查找这个字符串是否包含，如果包含，则返回字符串的位置，如果不包含，就返回-1
            //     if (String(this.$route.path).indexOf('task') > -1) {
            //         this.activeIndex = 'task';
            //     }
            //     if (String(this.$route.path).indexOf('service') > -1) {
            //         this.activeIndex = 'service';
            //     }
            // }
        },
        created() {
            // this.initMenu();
            this.activeIndex = this.menu;
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