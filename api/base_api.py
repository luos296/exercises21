#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import requests


class BaseAPI:
    def request(self, data: dict):
        if 'url' in data:
            return self.http_request(data)

    def http_request(self, data):
        response = requests.request(**data)
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        return response

    def rpc_request(self):
        pass

    def tcp_request(self):
        pass
