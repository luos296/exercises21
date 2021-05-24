#!/usr/bin/env python
# -*- coding:utf-8 -*-
from api.wework_api import WeWorkAPI


class Tag(WeWorkAPI):
    def get_corp_tag_list(self, tag_ids: list = None, group_ids: list = None, **kwargs):
        if group_ids:
            json_data = {"group_id": group_ids}
        elif tag_ids:
            json_data = {"tag_id": tag_ids}
        else:
            json_data = kwargs
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            'method': 'post',
            'params': {'access_token': self.access_token},
            'json': json_data
        }
        return self.request(data)

    def add_corp_tag(self, group_name: str = None, tag_list: list = None, **kwargs):
        if tag_list:
            json_data = {
                'group_name': group_name,
                'tag': tag_list
            }
        else:
            json_data = kwargs
        data = {
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            'method': 'post',
            'params': {'access_token': self.access_token},
            'json': json_data
        }
        return self.request(data)

    def edit_corp_tag(self, id: str, new_name: str):
        data = {
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            'method': 'post',
            'params': {'access_token': self.access_token},
            'json': {"id": id, "name": new_name}
        }
        return self.request(data)

    def del_corp_tag(self, tag_ids: list = None, group_ids: list = None):

        data = {
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            'method': 'post',
            'params': {'access_token': self.access_token},
            'json': {
                'tag_id': tag_ids,
                'group_id': group_ids
            }
        }
        print()
        return self.request(data)
