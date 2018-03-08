#!/usr/local/baize/env/bin/python
#coding:utf-8

# (c) 2016 , Tianbiao Zu <zutianbian@qq.com>
#
# 该文件是白泽自动化管理系统的一部分,是白泽系统APP_web应用的url路由文件


###################################################################################################
from django.conf.urls import patterns, url
import APP.APP_web.views as views

urlpatterns = [
    url(r'^/product_center', views.product_center),
    url(r'^/index', views.index),
    url(r'^/login', views.login),
    # url(r'^/register', views.register),
    url(r'^/logout', views.logout),
    url(r'^/reset', views.reset),
    url(r'^/remote_control/add_command', views.remote_control_add_command),
    url(r'^/remote_control/del_command', views.remote_control_del_command),
    url(r'^/remote_control/do_command', views.remote_control_do_command),
    url(r'^/remote_control/add_script', views.remote_control_add_script),
    url(r'^/remote_control/del_script', views.remote_control_del_script),
    url(r'^/remote_control/do_script', views.remote_control_do_script),
    url(r'^/remote_control/add_copy', views.remote_control_add_copy),
    url(r'^/remote_control/del_copy', views.remote_control_del_copy),
    url(r'^/remote_control/query_copy', views.remote_control_query_copy),
    url(r'^/remote_control/do_copy', views.remote_control_do_copy),
    url(r'^/asset_manage/index', views.asset_manage_index),
    url(r'^/asset_manage/query_property', views.asset_manage_query_property),
    url(r'^/asset_manage/show_detail', views.asset_manage_show_detail),
    url(r'^/asset_manage/tag/add', views.asset_manage_tag_add),
    url(r'^/asset_manage/tag/del', views.asset_manage_tag_del),
    url(r'^/asset_manage/tag/query_asset', views.asset_manage_tag_query_asset),
    url(r'^/asset_manage/tag/query', views.asset_manage_tag_query),
    url(r'^/asset_manage/tag/bind', views.asset_manage_tag_bind),
    url(r'^/asset_manage/tag/unbind', views.asset_manage_tag_unbind),
    url(r'^/asset_manage/tree/bind', views.asset_manage_tree_bind),
    url(r'^/asset_manage/tree/save', views.asset_manage_tree_save),
    url(r'^/asset_manage/tree/query', views.asset_manage_tree_query),
    url(r'^/asset_manage', views.asset_manage),
    url(r'^/network_detect/role/save', views.network_detect_role_save),
    url(r'^/network_detect/role/index', views.network_detect_role_index),
    url(r'^/network_detect/role/delete_multiple', views.network_detect_role_delete_multiple),
    url(r'^/network_detect/task/index', views.network_detect_task_index),
    url(r'^/network_detect/task/add_single', views.network_detect_task_add_single),
    url(r'^/network_detect/task/del_single', views.network_detect_task_del_single),
    url(r'^/network_detect/task/delete_multiple', views.network_detect_task_delete_multiple),
    url(r'^/network_detect/task/query/index', views.network_detect_task_query_index),
    url(r'^/network_detect/task/query/history', views.network_detect_task_query_history),
    url(r'^/network_detect/task/query', views.network_detect_task_query),
    url(r'^/network_detect', views.network_detect),
    url(r'^/configure_manage/work/query_from_asset', views.configure_manage_work_query_from_asset),
    url(r'^/configure_manage/work/save', views.configure_manage_work_save),
    url(r'^/configure_manage/work/test', views.configure_manage_work_test),
    url(r'^/configure_manage/work/query_status_detail', views.configure_manage_work_query_status_detail),
    url(r'^/configure_manage/work/query_status', views.configure_manage_work_query_status),
    url(r'^/configure_manage/work/online', views.configure_manage_work_online),
    url(r'^/configure_manage/work/delete', views.configure_manage_work_delete),
    url(r'^/configure_manage/work/status_refresh', views.configure_manage_work_status_refresh),
    url(r'^/configure_manage/task/save', views.configure_manage_task_save),
    url(r'^/configure_manage/task/test', views.configure_manage_task_test),
    url(r'^/configure_manage/task/query_status_detail', views.configure_manage_task_query_status_detail),
    url(r'^/configure_manage/task/query_status', views.configure_manage_task_query_status),
    url(r'^/configure_manage/task/online', views.configure_manage_task_online),
    url(r'^/configure_manage/task/continue', views.configure_manage_task_continue),
    url(r'^/configure_manage/task/delete', views.configure_manage_task_delete),
    url(r'^/configure_manage', views.configure_manage),
    url(r'^/task_manage/add', views.task_manage_add),
    url(r'^/task_manage/modify', views.task_manage_modify),
    url(r'^/task_manage/status_detail', views.task_manage_status_detail),
    url(r'^/task_manage', views.task_manage),
    url(r'^/work_manage/add', views.work_manage_add),
    url(r'^/work_manage/modify', views.work_manage_modify),
    url(r'^/work_manage/status_detail', views.work_manage_status_detail),
    url(r'^/work_manage', views.work_manage),
    url(r'^/bussiness_manage/bussiness_detail', views.bussiness_manage_bussiness_detail),
    url(r'^/bussiness_manage/add_person', views.bussiness_manage_add_person),
    url(r'^/bussiness_manage/add_btn', views.bussiness_manage_add_btn),
    url(r'^/bussiness_manage/delete', views.bussiness_manage_delete),
    url(r'^/bussiness_manage/save', views.bussiness_manage_save),
    url(r'^/bussiness_manage/add', views.bussiness_manage_add),
    url(r'^/bussiness_manage/index', views.bussiness_manage_index),
    url(r'^/bussiness_manage', views.bussiness_manage),
    url(r'^/alarm_manage/alarm_person/detail', views.alarm_manage_alarm_person_detail),
    url(r'^/alarm_manage/alarm_person/delete', views.alarm_manage_alarm_person_delete),
    url(r'^/alarm_manage/alarm_person/save', views.alarm_manage_alarm_person_save),
    url(r'^/alarm_manage/alarm_person/add', views.alarm_manage_alarm_person_add),
    url(r'^/alarm_manage/alarm_person', views.alarm_manage_alarm_person),
    url(r'^/alarm_manage/alarm/query_alarm_template', views.alarm_manage_alarm_query_alarm_template),
    url(r'^/alarm_manage/alarm/add_alarm_template', views.alarm_manage_alarm_add_alarm_template),
    url(r'^/alarm_manage/alarm/add_alarm_person', views.alarm_manage_alarm_add_alarm_person),
    url(r'^/alarm_manage/alarm/recive_msg', views.alarm_manage_alarm_recive_msg),
    url(r'^/alarm_manage/alarm/change_switch', views.alarm_manage_alarm_change_switch),
    url(r'^/alarm_manage/alarm/detail', views.alarm_manage_alarm_detail),
    url(r'^/alarm_manage/alarm/delete', views.alarm_manage_alarm_delete),
    url(r'^/alarm_manage/alarm/save', views.alarm_manage_alarm_save),
    url(r'^/alarm_manage/alarm/add', views.alarm_manage_alarm_add),
    url(r'^/alarm_manage/alarm', views.alarm_manage_alarm),
    url(r'^/alarm_manage/index', views.alarm_manage_index),
    url(r'^/alarm_manage/api', views.alarm_manage_api),
    url(r'^/alarm_manage/ignore_alarm_msg', views.alarm_manage_ignore_alarm_msg),
    url(r'^/alarm_manage/query_alarm_msg', views.alarm_manage_query_alarm_msg),
    url(r'^/alarm_manage', views.alarm_manage),
    url(r'^/monitor_manage/data_table', views.fun_403),
    url(r'^/monitor_manage/item/bind_work', views.monitor_manage_item_bind_work),
    url(r'^/monitor_manage/item/detail', views.monitor_manage_item_detail),
    url(r'^/monitor_manage/item/delete', views.monitor_manage_item_delete),
    url(r'^/monitor_manage/item/save', views.monitor_manage_item_save),
    url(r'^/monitor_manage/item/add', views.monitor_manage_item_add),
    url(r'^/monitor_manage/item', views.monitor_manage_item),
    url(r'^/monitor_manage/screen/detail', views.monitor_manage_screen_detail),
    url(r'^/monitor_manage/screen/show_chart', views.monitor_manage_screen_show_chart),
    url(r'^/monitor_manage/screen/add_chart', views.monitor_manage_screen_add_chart),
    url(r'^/monitor_manage/screen/delete', views.monitor_manage_screen_delete),
    url(r'^/monitor_manage/screen/add_person', views.monitor_manage_screen_add_person),
    url(r'^/monitor_manage/screen/save', views.monitor_manage_screen_save),
    url(r'^/monitor_manage/screen/add', views.monitor_manage_screen_add),
    url(r'^/monitor_manage/screen', views.monitor_manage_screen),
    url(r'^/monitor_manage', views.monitor_manage),
    url(r'/reciver', views.reciver),
    url(r'^', views.fun_403),
]