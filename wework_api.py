#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from urllib import parse


class WeWorkAPI:
    host = 'https://qyapi.weixin.qq.com/'
    access_token: str = None

    def get_token(self):
        url = parse.urljoin(self.host, 'cgi-bin/gettoken')
        params = {
            'corpid': 'ww819451014bb7ead0',
            'corpsecret': 'IvwMVGMQpe-JYMFa4NNDetCC8v4onmoW3lNXTSyg8wo'
        }
        r = requests.get(url=url, params=params)
        self.access_token = r.json()['access_token']

    def get_corp_tag_list(self, tag_id=None, group_id=None):
        url = parse.urljoin(self.host, 'cgi-bin/externalcontact/get_corp_tag_list')
        params = {
            'access_token': self.access_token
        }
        data = {
            'tag_id': tag_id,
            'group_id': group_id
        }
        r = requests.post(url=url, params=params, json=data)
        return r

    def add_corp_tag(self, group_name, tag_name):
        url = parse.urljoin(self.host, 'cgi-bin/externalcontact/add_corp_tag')
        params = {
            'access_token': self.access_token
        }
        data = {
            'group_name': group_name,
            'tag': [
                {
                    "name": tag_name
                }
            ]
        }

        r = requests.post(url=url, params=params, json=data)
        return r

    def edit_corp_tag(self, id, new_name):
        url = parse.urljoin(self.host, 'cgi-bin/externalcontact/edit_corp_tag')
        params = {
            'access_token': self.access_token
        }
        data = {
            'id': id,
            'name': new_name
        }
        r = requests.post(url=url, params=params, json=data)
        return r

    def del_corp_tag(self, tag_id=None, group_id=None):
        url = parse.urljoin(self.host, 'cgi-bin/externalcontact/del_corp_tag')
        params = {
            'access_token': self.access_token
        }
        data = {
            'tag_id': tag_id,
            'group_id': group_id
        }
        r = requests.post(url=url, params=params, json=data)
        return r
