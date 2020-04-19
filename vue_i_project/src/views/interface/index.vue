<template>
    <div class="interface-main">
        <el-button @click="openAddModal">创建接口</el-button>
        <el-table
                :data="interfaces"
                stripe
                style="width: 100%">
            <el-table-column
                    prop="name"
                    label="名称"
                    width="180">
            </el-table-column>
            <el-table-column
                    prop="description"
                    label="描述">
            </el-table-column>
            <el-table-column
                    label="URL"
                    width="300">
                <template slot-scope="scope">
                    {{scope.row.context.url}}
                </template>
            </el-table-column>
            <el-table-column label="操作" width="200">
                <template slot-scope="scope">
                    <el-button
                            size="mini">编辑
                    </el-button>
                    <el-button
                            @click="deleteInterfaceFun(scope.row.id)"
                            size="mini"
                            type="danger">删除
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
    import {deleteInterface, getInterfaces} from "../../request/interface";

    export default {
        name: "index",
        data() {
            return {
                serviceId: 0,
                interfaces: [],
            }
        },
        methods: {
            openAddModal() {

            },
            deleteInterfaceFun(interfaceId) {
                this.$confirm('此操作将永久删除该数据, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    deleteInterface(interfaceId).then(data => {
                        let success = data.data.success;
                        if (success) {
                            this.getInterfacesFun()
                        } else {
                            this.$notify.error({
                                title: '错误',
                                message: '请求失败'
                            });
                        }
                    })
                }).catch(() => {
                });

            },
            getServiceId() {
                //获取url里面的参数
                let serviceId = this.$route.query.serviceId;
                if (!serviceId) { //如果是空的
                    this.serviceId = 0;
                    return;
                }
                this.serviceId = Number(serviceId)
            },
            getInterfacesFun() {
                getInterfaces(this.serviceId).then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.interfaces = data.data.data;
                    } else {
                        this.$notify.error({
                            title: '错误',
                            message: '请求失败'
                        });
                    }
                })
            },
        },
        created() {
            this.getServiceId();
            this.getInterfacesFun();
        },
        watch: {
            "$route.query": function () {
                this.getServiceId();
                this.getInterfacesFun();
            }
        }
    }
</script>

<style scoped>
    .interface-main {
        text-align: left;
        padding: 5px;
    }
</style>