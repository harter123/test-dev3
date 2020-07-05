<template>
    <div class="task-main">
        <el-button @click="openAddModal">创建任务</el-button>

        <div class="task-list">
            <!--<el-card class="task-card" v-for="item in taskList" :key="item.id">-->
                <!--<div slot="header" class="task-card-header">-->
                    <!--<div>-->
                        <!--<a href="javascript:void(0)" @click="showDrawer(item.id)"> {{item.name}}</a>-->
                    <!--</div>-->
                    <!--<div>-->
                        <!--<el-button style="padding: 3px 0;" type="text" @click="openEditModal(item)">编辑-->
                        <!--</el-button>-->
                        <!--<el-button style="padding: 3px 0;margin-left: 5px;" type="text"-->
                                   <!--@click="deleteTaskFun(item.id)">删除-->
                        <!--</el-button>-->
                    <!--</div>-->

                <!--</div>-->
                <!--<div>-->
                    <!--{{item.description}}-->

                    <!--<div>-->
                        <!--<a href="javascript:void(0)" @click="showReportDrawer(item.id)">查看报告</a>-->
                    <!--</div>-->
                <!--</div>-->
            <!--</el-card>-->

            <el-table
                    :data="taskList"
                    style="width: 100%">
                <el-table-column
                        prop="id"
                        label="ID"
                        width="50">
                </el-table-column>
                <el-table-column
                        prop="name"
                        label="名称"
                        width="250">
                    <template slot-scope="scope">
                        <a @click="showDrawer(scope.row.id)" href="javascript:void(0)">
                            {{scope.row.name}}
                        </a>
                    </template>
                </el-table-column>
                <el-table-column
                        prop="description"
                        label="描述"
                        width="500">
                </el-table-column>
                <el-table-column
                        prop="address"
                        label="操作">
                    <template slot-scope="scope">
                        <el-button
                                @click.native.prevent="openEditModal(scope.row)"
                                type="text"
                                size="small">
                            编辑
                        </el-button>
                        <el-button
                                @click.native.prevent="deleteTaskFun(scope.row.id)"
                                type="text"
                                size="small">
                            删除
                        </el-button>
                        <el-button
                                @click.native.prevent="showReportDrawer(scope.row.id)"
                                type="text"
                                size="small">
                            查看报告
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>

        <div style="text-align:right; margin-top: 10px">
            <el-pagination
                    @size-change="changeSize"
                    @current-change="changePage"
                    :current-page.sync="page"
                    :page-sizes="[10, 20, 50, 100]"
                    :page-size="size"
                    layout="sizes, prev, pager, next"
                    :total="total">
            </el-pagination>
        </div>

        <el-dialog title="创建任务" :visible.sync="dialogAddVisible">
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
                <el-button type="primary" @click="addTaskFun">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="编辑任务" :visible.sync="dialogEditVisible">
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
                <el-button type="primary" @click="editTaskFun">确 定</el-button>
            </div>
        </el-dialog>


        <el-drawer
                :visible.sync="drawerShowFlag"
                direction="rtl"
                size="40%">
            <div slot="title">
                <el-button type="primary" v-loading.fullscreen.lock="fullscreenLoading" plain @click="showAddInterface=true">添加接口</el-button>
            </div>
            <el-table
                    :data="interfaces"
                    stripe
                    style="width: 100%">
                <el-table-column
                        prop="name"
                        label="名称"
                        min-width="40%">
                </el-table-column>
                <el-table-column
                        label="URL"
                        min-width="45%">
                    <template slot-scope="scope">
                        {{scope.row.context.url}}
                    </template>
                </el-table-column>
                <el-table-column label="操作" min-width="15%">
                    <template slot-scope="scope">
                        <el-button
                                @click="deleteTaskInterfaceFun(scope.row)"
                                size="mini"
                                type="danger">删除
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>

        </el-drawer>

        <el-drawer
                :visible.sync="drawerReportShowFlag"
                direction="rtl"
                size="40%">
            <div slot="title">
                <el-button type="primary" plain @click="runTaskFun">执行任务</el-button>
            </div>
            <el-table
                    :data="reports"
                    stripe
                    style="width: 100%">
                <el-table-column label="名称">
                    <template slot-scope="scope">
                        <a href="javascript:void(0)" @click="openReportDetail(scope.row)">{{scope.row}}</a>
                    </template>
                </el-table-column>

            </el-table>
        </el-drawer>

        <el-dialog
                title="添加接口"
                :visible.sync="showAddInterface"
                width="40%">
            <selectInterface ref="selectInterface"></selectInterface>
            <span slot="footer" class="dialog-footer">
                <el-button @click="showAddInterface = false">取 消</el-button>
                <el-button type="primary" @click="addTaskInterfacesFun">确 定</el-button>
              </span>
        </el-dialog>

    </div>
</template>

<script>
    import {addTask, deleteTask, getAllTasks, updateTask} from "../../request/task";
    import {
        addTaskInterfaces,
        deleteTaskInterface,
        getTaskInterfaces,
        getTaskReports, runTask
    } from "../../request/task_interface";
    import selectInterface from "./selectInterface"

    export default {
        name: "index",
        components: {
            selectInterface
        },
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
                taskList: [],
                page:1,
                size:20,
                total:0,

                interfaces: [],
                drawerShowFlag: false,
                showAddInterface: false,
                currentTaskId: 0,

                reports: [],
                drawerReportShowFlag: false,
                fullscreenLoading: false,
            }
        },
        created() {
            this.getAllTasksFun()
        },
        methods: {
            changeSize(value){
                this.size = value;
                this.getAllTasksFun()
            },
            changePage(value){
                this.page = value;
                 this.getAllTasksFun()
            },
            addTaskInterfacesFun() {
                let multipleSelection = this.$refs.selectInterface.multipleSelection;
                let req = [];
                for (let i = 0; i < multipleSelection.length; i++) {
                    req.push({task_id:this.currentTaskId, interface_id: multipleSelection[i].id})
                }
                if(0 === req.length){
                    return
                }
                addTaskInterfaces(req).then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.showAddInterface = false;
                        this.showDrawer(this.currentTaskId);
                    } else {
                        this.$notify.error({
                            title: '错误',
                            message: '请求失败'
                        });
                    }
                });
            },
            showDrawer(taskId) {
                this.currentTaskId = taskId;
                getTaskInterfaces(taskId).then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.interfaces = data.data.data;
                    } else {
                        this.$notify.error({
                            title: '错误',
                            message: '请求失败'
                        });
                    }
                });
                this.drawerShowFlag = true;
            },
            showReportDrawer(taskId) {
                this.currentTaskId = taskId;
                getTaskReports(taskId).then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.reports = data.data.data;
                    } else {
                        this.$notify.error({
                            title: '错误',
                            message: '请求失败'
                        });
                    }
                });
                this.drawerReportShowFlag = true;
            },
            deleteTaskInterfaceFun(taskInterface) {
                deleteTaskInterface(taskInterface.task_interface_id).then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.showDrawer(taskInterface.task_id)
                    } else {
                        this.$notify.error({
                            title: '错误',
                            message: '请求失败'
                        });
                    }
                });
            },
            deleteTaskFun(taskId) {
                this.$confirm('此操作将永久删除该任务, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    //点击确定
                    deleteTask(taskId).then(data => {
                        let success = data.data.success;
                        if (success) {
                            this.getAllTasksFun();
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
            getAllTasksFun() {
                getAllTasks(this.page, this.size).then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.taskList = data.data.data.list;
                        this.total=data.data.data.total;
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
            addTaskFun() { //这是请求创建任务
                this.$refs.addFormRef.validate((valid) => {
                    if (valid) {
                        //表单检验通过
                        addTask(this.addForm).then(data => {
                            let success = data.data.success;
                            if (success) {
                                this.dialogAddVisible = false
                                this.getAllTasksFun();
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
            editTaskFun() { //这是请求编辑任务
                this.$refs.editFormRef.validate((valid) => {
                    if (valid) {
                        //表单检验通过
                        updateTask(this.editForm.id, this.editForm).then(data => {
                            let success = data.data.success;
                            if (success) {
                                this.dialogEditVisible = false
                                this.getAllTasksFun();
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
            openReportDetail(reportName){
                window.open(`/api/task/${this.currentTaskId}/report/${reportName}/`)
            },
            runTaskFun(){
                this.fullscreenLoading = true
                runTask(this.currentTaskId).then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.showReportDrawer(this.currentTaskId)
                    } else {
                        this.$notify.error({
                            title: '错误',
                            message: '请求失败'
                        });
                    }
                    this.fullscreenLoading = false
                })
            },

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
    .task-main {
        text-align: left;
        padding: 5px 5px;
    }

    .task-card {
        width: 250px;
        margin-top: 5px;
        margin-right: 10px;
    }

    .task-list {
        display: flex;
        flex-wrap: wrap;
    }

    .task-card-header {
        display: flex;
        justify-content: space-between;
    }
</style>