import {deleteRequest, getRequest, postRequest} from "./common";

export const getTaskInterfaces = function (taskId) { //获取任务下的接口
    return getRequest(`task_interfaces/?task_id=${taskId}`)
};

export const addTaskInterfaces = function (data_list) { //创建任务和接口关联
    return postRequest('task_interfaces/', data_list)
};

export const deleteTaskInterface = function (taskInterfaceId) {//删除任务下的接口
    return deleteRequest(`task_interface/${taskInterfaceId}/`);
};
