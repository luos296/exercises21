#!/usr/bin/env python
# -*- coding:utf-8 -*-
from api.base_api import BaseAPI


class WeWorkAPI(BaseAPI):
    access_token: str = None

    def get_token(self):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'method': 'get',
            'params': {
                'corpid': 'ww819451014bb7ead0',
                'corpsecret': 'IvwMVGMQpe-JYMFa4NNDetCC8v4onmoW3lNXTSyg8wo'
            }
        }
        r = self.request(data)
        self.access_token = r.json()['access_token']
