<template>
    <div class="login-container">
        <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" auto-complete="on"
                 label-position="left">

            <div class="title-container">
                <h3 class="title">登录页面</h3>
            </div>

            <el-form-item prop="username">
        <span class="svg-container">
          <i class="el-icon-s-custom"></i>
        </span>
                <el-input
                        ref="username"
                        v-model="loginForm.username"
                        placeholder="Username"
                        name="username"
                        type="text"
                        tabindex="1"
                        auto-complete="on"
                />
            </el-form-item>

            <el-form-item prop="password">
        <span class="svg-container">
          <i class="el-icon-lock"></i>
        </span>
                <el-input
                        :key="passwordType"
                        ref="password"
                        v-model="loginForm.password"
                        :type="passwordType"
                        placeholder="Password"
                        name="password"
                        tabindex="2"
                        auto-complete="on"
                        @keyup.enter.native="handleLogin"
                />
            </el-form-item>
            <div>
                <el-button :loading="loading" type="primary" style="width:100%;margin-bottom:10px;"
                           @click="handleLogin">登录
                </el-button>
            </div>
            <div>
                <el-button style="width:100%;margin-bottom:30px;" @click="handleRegister">注册</el-button>
            </div>
        </el-form>
    </div>
</template>

<script>
    import {login, register} from "../../request/user";

    export default {
        name: 'Login',
        data() {
            return {
                loginForm: {
                    username: 'admin',
                    password: '111111'
                },
                loginRules: {
                    username: [{required: true, trigger: 'blur'}],
                    password: [{required: true, trigger: 'blur'}]
                },
                loading: false,
                passwordType: 'password',
            }
        },
        methods: {
            handleLogin() {
                this.$refs.loginForm.validate(valid => {
                    if (valid) {
                        // this.loading = true
                        login(this.loginForm.username, this.loginForm.password).then(data => {
                            let success = data.data.success;
                            if (success) {
                                this.$router.push('/')
                            } else {
                                this.$notify.error({
                                    title: '错误',
                                    message: '登录失败'
                                });
                            }

                        })
                    } else {
                        console.log('error submit!!')
                        return false
                    }
                })
            },
            handleRegister() {
                this.$refs.loginForm.validate(valid => {
                    if (valid) {
                        // this.loading = true
                        register(this.loginForm.username, this.loginForm.password).then(data => {
                            let success = data.data.success;
                            if (success) {
                                this.$router.push('/')
                            } else {
                                this.$notify.error({
                                    title: '错误',
                                    message: '注册失败'
                                });
                            }
                        }).catch(data => {

                        })
                    } else {
                        console.log('error submit!!')
                        return false
                    }
                })
            }
        }
    }
</script>

<style lang="scss">
    /* 修复input 背景不协调 和光标变色 */
    /* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

    $bg: #283443;
    $light_gray: #fff;
    $cursor: #fff;

    @supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
        .login-container .el-input input {
            color: $cursor;
        }
    }

    /* reset element-ui css */
    .login-container {
        .el-input {
            display: inline-block;
            height: 47px;
            width: 85%;

            input {
                background: transparent;
                border: 0px;
                -webkit-appearance: none;
                border-radius: 0px;
                padding: 12px 5px 12px 15px;
                color: $light_gray;
                height: 47px;
                caret-color: $cursor;

                &:-webkit-autofill {
                    box-shadow: 0 0 0px 1000px $bg inset !important;
                    -webkit-text-fill-color: $cursor !important;
                }
            }
        }

        .el-form-item {
            border: 1px solid rgba(255, 255, 255, 0.1);
            background: rgba(0, 0, 0, 0.1);
            border-radius: 5px;
            color: #454545;
        }
    }
</style>

<style lang="scss" scoped>
    $bg: #2d3a4b;
    $dark_gray: #889aa4;
    $light_gray: #eee;

    .login-container {
        min-height: 100%;
        width: 100%;
        background-color: $bg;
        overflow: hidden;

        .login-form {
            position: relative;
            width: 520px;
            max-width: 100%;
            padding: 160px 35px 0;
            margin: 0 auto;
            overflow: hidden;
        }

        .tips {
            font-size: 14px;
            color: #fff;
            margin-bottom: 10px;

            span {
                &:first-of-type {
                    margin-right: 16px;
                }
            }
        }

        .svg-container {
            padding: 6px 5px 6px 5px;
            color: $dark_gray;
            vertical-align: middle;
            display: inline-block;
            margin-left: -20px;
        }

        .title-container {
            position: relative;

            .title {
                font-size: 26px;
                color: $light_gray;

                text-align: center;
                font-weight: bold;
            }
        }

        .show-pwd {
            position: absolute;
            right: 10px;
            top: 7px;
            font-size: 16px;
            color: $dark_gray;
            cursor: pointer;
            user-select: none;
        }
    }

    .flex-space {
        display: flex;
        justify-content: space-between;
    }
</style>
