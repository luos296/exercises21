#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wework_api import WeWorkAPI
from jsonpath import jsonpath


class TestWeWork:
    def setup_class(self):
        self.work_api = WeWorkAPI()
        self.work_api.get_token()
        self.row_data = self.work_api.get_corp_tag_list()
        with open('row_data.json', mode='w') as f:
            f.write(self.row_data.text)

    def test_get_corp_tag_list(self):
        # 查询所有标签
        # todo:对返回json格式进行schema校验(暂时不会)
        r = self.work_api.get_corp_tag_list()
        assert r.status_code == 200
        # print(r.json())
        assert r.json()['errcode'] == 0

    def test_get_corp_tag_list_tag_id(self):
        # 测试用tag_id查询标签
        tag_id = self.row_data.json()['tag_group'][0]['tag'][0]['id']
        tag_name = self.row_data.json()['tag_group'][0]['tag'][0]['name']
        r = self.work_api.get_corp_tag_list(tag_id=tag_id)
        assert r.status_code == 200
        # print(r.json())
        assert r.json()['errcode'] == 0
        assert jsonpath(r.json(), '$..name')[0] == tag_name

    def test_add_corp_tag(self):
        group_name = '测试组1'
        tag_name = '标签名1'
        r = self.work_api.add_corp_tag(group_name=group_name, tag_name=tag_name)
        assert r.status_code == 200
        # print(r.json())
        assert r.json()['errcode'] == 0
        assert jsonpath(r.json(), '$..name')[0] == tag_name

    def test_edit_corp_tag(self):
        group_id = self.row_data.json()['tag_group'][0]['group_id']
        new_name = '新名称'
        r = self.work_api.edit_corp_tag(id=group_id, new_name=new_name)
        assert r.status_code == 200
        # print(r.json())
        assert r.json()['errcode'] == 0
        get_tag_list = self.work_api.get_corp_tag_list(group_id=group_id)
        # print(get_tag_list.json())
        assert jsonpath(get_tag_list.json(), '$..group_name')[0] == new_name

    def test_del_corp_tag(self):
        tag_id = self.row_data.json()['tag_group'][0]['tag'][0]['id']
        tag_name = self.row_data.json()['tag_group'][0]['tag'][0]['name']
        r = self.work_api.del_corp_tag(tag_id=tag_id)
        assert r.status_code == 200
        # print(r.json())
        assert r.json()['errcode'] == 0
        get_tag_list = self.work_api.get_corp_tag_list()
        # 确保该标签名已删除
        assert get_tag_list.json()['tag_group'][0]['tag'][0]['id'] != tag_id
        assert get_tag_list.json()['tag_group'][0]['tag'][0]['name'] != tag_name

    def teardown_class(self):
        # 清空现有数据
        get_tag_list = self.work_api.get_corp_tag_list().json()
        group_id_list = jsonpath(get_tag_list, '$..group_id')
        self.work_api.del_corp_tag(group_id=group_id_list)
        # 恢复原始数据
        for i in self.row_data.json()['tag_group']:
            for j in i['tag']:
                self.work_api.add_corp_tag(group_name=i['group_name'], tag_name=j['name'])
        # print(self.work_api.get_corp_tag_list().json())
