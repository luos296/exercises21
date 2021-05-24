#!/usr/bin/env python
# -*- coding:utf-8 -*-

from api.externalcontact.tag import Tag
from jsonpath import jsonpath
from testcase.base_testcase import BaseTestCase


class TestTag(BaseTestCase):
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()
        group_ids = jsonpath(self.tag.get_corp_tag_list().json(), '$..group_id')
        self.tag.del_corp_tag(group_ids=group_ids)

    def teardown_class(self):
        pass

    def test_get_corp_tag_list(self):
        r = self.tag.get_corp_tag_list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_add_corp_tag(self):
        tag_list = [{'name': 'tag_001'}, {'name': 'tag_002'}]
        group_name = 'tag_group_001'
        r = self.tag.add_corp_tag(group_name=group_name, tag_list=tag_list)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        assert set(jsonpath(r.json(), '$..name')) == {'tag_001', 'tag_002'}

    def test_edit_corp_tag(self):
        tag_list = [{'name': 'tag_001'}, {'name': 'tag_002'}]
        group_name = 'tag_group_002'
        r = self.tag.add_corp_tag(group_name=group_name, tag_list=tag_list)
        group_id = r.json()['tag_group']['group_id']
        new_name = 'tag_group_003'
        r = self.tag.edit_corp_tag(id=group_id, new_name=new_name)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        get_tag_list = self.tag.get_corp_tag_list(group_id=group_id)
        assert jsonpath(get_tag_list.json(), '$..group_name')[0] == new_name

    def test_del_corp_tag(self):
        tag_list = [{'name': 'tag_001'}, {'name': 'tag_002'}]
        group_name = 'tag_group_004'
        r = self.tag.add_corp_tag(group_name=group_name, tag_list=tag_list)
        group_id = r.json()['tag_group']['group_id']
        r = self.tag.del_corp_tag(group_ids=[group_id])
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        get_tag_list = self.tag.get_corp_tag_list()
        assert group_name not in jsonpath(get_tag_list.json(), '$..group_name')
