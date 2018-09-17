# coding: utf-8
"""
a simple example of request_html
__author__ = Leo.Feng
"""
import time
import requests_html


class GetConceptJinSe(object):

    def __init__(self):
        self.concept_url = 'http://api.jinse.com/v5/plate/list?limit=50' \
                           '&page=1&cover=0&version=3.0.0&source=android'

        self.concept_base = 'http://api.jinse.com/v5/plate/coin?id={}&limit=50' \
                            '&page=1&currency=CNY&version=3.0.0&source=android'

    @staticmethod
    def get_response(_url):
        with requests_html.HTMLSession() as r:
            # the response is json, so use the json() method transform to a dictionary
            return r.get(_url).json()

    def get_concept_list(self):
        rsp = self.get_response(self.concept_url)
        print(f'response: {rsp}')
        return rsp['list']

    def get_coin_list(self, _dict):
        name = _dict['name']
        _url = self.concept_base.format(_dict['id'])
        rsp = self.get_response(_url)
        _list = rsp['list']
        data_list = [
            {'code': i['slug']} for i in _list
        ]
        return {
            'conceptName': name,
            'coinList': data_list
        }

    def run(self):
        a = time.time()
        concept_list = self.get_concept_list()
        result = [self.get_coin_list(c) for c in concept_list]
        print(f'result: {result}')
        using_time = time.time() - a
        print(f'using time: {using_time}')


if __name__ == '__main__':
    try:
        jinse_concept = GetConceptJinSe()
        jinse_concept.run()
    except Exception as e:
        print(f'{e}')
