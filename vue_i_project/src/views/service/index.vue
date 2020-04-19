<template>
    <div class="service-main">
        <el-button @click="openAddModal">创建服务</el-button>

        <div class="service-list">
            <el-card class="service-card" v-for="item in serviceList" :key="item.id">
                <div slot="header" class="service-card-header">

                    <div @click="goToInterface(item.id)">
                        <a href="javascript:void(0)">{{item.name}}</a>
                    </div>
                    <div>
                        <el-button style="padding: 3px 0;" type="text" @click="openEditModal(item)">编辑
                        </el-button>
                        <el-button style="padding: 3px 0;margin-left: 5px;" type="text"
                                   @click="deleteServiceFun(item.id)">删除
                        </el-button>
                    </div>

                </div>
                <div>
                    {{item.description}}
                </div>
            </el-card>

        </div>

        <el-dialog title="创建服务" :visible.sync="dialogAddVisible">
            <el-form :model="addForm" :rules="addRules" ref="addFormRef" label-width="50px" class="demo-ruleForm">
                <el-form-item label="名称" prop="name">
                    <el-input v-model="addForm.name"></el-input>
                </el-form-item>

                <el-form-item label="描述" prop="description">
                    <el-input type="textarea" v-model="addForm.description"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogAddVisible = false">取 消</el-button>
                <el-button type="primary" @click="addServiceFun">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="编辑服务" :visible.sync="dialogEditVisible">
            <el-form :model="editForm" :rules="editRules" ref="editFormRef" label-width="50px" class="demo-ruleForm">
                <el-form-item label="名称" prop="name">
                    <el-input v-model="editForm.name"></el-input>
                </el-form-item>

                <el-form-item label="描述" prop="description">
                    <el-input type="textarea" v-model="editForm.description"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogEditVisible = false">取 消</el-button>
                <el-button type="primary" @click="editServiceFun">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import {addService, deleteService, getAllServices, updateService} from "../../request/service";

    export default {
        name: "index",
        data() {
            return {
                dialogAddVisible: false,
                dialogEditVisible: false,
                addForm: {
                    name: "",
                    description: "",
                },
                addRules: {
                    name: [
                        {required: true, message: '请输入名称', trigger: 'blur'},
                    ],
                    description: [
                        {required: true, message: '请填写描述', trigger: 'blur'}
                    ]
                },
                editForm: {
                    id: 0,
                    name: "",
                    description: "",
                },
                editRules: {
                    name: [
                        {required: true, message: '请输入名称', trigger: 'blur'},
                    ],
                    description: [
                        {required: true, message: '请填写描述', trigger: 'blur'}
                    ]
                },
                serviceList: [],
            }
        },
        created() {
            this.getAllServicesFun()
        },
        methods: {
            goToInterface(serviceId){
                this.$router.push(`/interface/?serviceId=${serviceId}`)
            },
            deleteServiceFun(serviceId) {
                this.$confirm('此操作将永久删除该服务, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    //点击确定
                    deleteService(serviceId).then(data => {
                        let success = data.data.success;
                        if (success) {
                            this.getAllServicesFun();
                        } else {
                            this.$notify.error({
                                title: '错误',
                                message: '请求失败'
                            });
                        }
                    })
                }).catch(() => {
                    //点击取消
                });
            },
            getAllServicesFun() {
                getAllServices().then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.serviceList = data.data.data;
                    } else {
                        this.$notify.error({
                            title: '错误',
                            message: '请求失败'
                        });
                    }
                })
            },
            openAddModal() { //这是打开创建窗口
                this.dialogAddVisible = true
            },
            addServiceFun() { //这是请求创建服务
                this.$refs.addFormRef.validate((valid) => {
                    if (valid) {
                        //表单检验通过
                        addService(this.addForm).then(data => {
                            let success = data.data.success;
                            if (success) {
                                this.dialogAddVisible = false
                                this.getAllServicesFun();
                            } else {
                                this.$notify.error({
                                    title: '错误',
                                    message: '请求失败'
                                });
                            }
                        })
                    } else {
                        return false;
                    }
                });
            },
            openEditModal(data) { //这是打开编辑窗口
                this.dialogEditVisible = true;
                this.editForm.id = data.id;
                this.editForm.name = data.name;
                this.editForm.description = data.description;
            },
            editServiceFun() { //这是请求编辑服务
                this.$refs.editFormRef.validate((valid) => {
                    if (valid) {
                        //表单检验通过
                        updateService(this.editForm.id, this.editForm).then(data => {
                            let success = data.data.success;
                            if (success) {
                                this.dialogEditVisible = false
                                this.getAllServicesFun();
                            } else {
                                this.$notify.error({
                                    title: '错误',
                                    message: '请求失败'
                                });
                            }
                        })
                    } else {
                        return false;
                    }
                });
            }
        }
    }
</script>

<!--这里是重写element的css， 不能有scoped属性，所以这里是全局的-->
<style>
    .el-card__header {
        padding: 10px 20px;
        border-bottom: 1px solid #EBEEF5;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
    }
</style>

<style scoped>
    .service-main {
        text-align: left;
        padding: 5px 5px;
    }

    .service-card {
        width: 250px;
        margin-top: 5px;
        margin-right: 10px;
    }

    .service-list {
        display: flex;
        flex-wrap: wrap;
    }

    .service-card-header {
        display: flex;
        justify-content: space-between;
    }
</style>