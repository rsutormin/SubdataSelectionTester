# -*- coding: utf-8 -*-
import unittest
import os
import json
import time
import requests

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint

from biokbase.workspace.client import Workspace as workspaceService
from SubdataSelectionTester.SubdataSelectionTesterImpl import SubdataSelectionTester
from SubdataSelectionTester.SubdataSelectionTesterServer import MethodContext


class SubdataSelectionTesterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        user_id = requests.post(
            'https://kbase.us/services/authorization/Sessions/Login',
            data='token={}&fields=user_id'.format(token)).json()['user_id']
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'SubdataSelectionTester',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('SubdataSelectionTester'):
            cls.cfg[nameval[0]] = nameval[1]
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL, token=token)
        cls.serviceImpl = SubdataSelectionTester(cls.cfg)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_SubdataSelectionTester_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    # NOTE: According to Python unittest naming rules test method names should start from 'test'.
    def test_get_object_subset(self):
        ws_name = self.getWsName()
        obj_name = 'test.1'
        obj_data = {'a1': {'b1': 'v1', 'b2': 'v2'}, 'a2': 123}
        self.getWsClient().save_objects({'workspace': self.getWsName(), 'objects': 
                [{'name': obj_name, 'type': 'Empty.AType-0.1', 'data': obj_data}]})
        ret = self.getImpl().get_object_subset(self.getContext(), 
                [{'ref': ws_name + '/' + obj_name, 'included': ['/a1/b1']}])[0]
        ret_obj = ret[0]['data']
        self.assertEqual(ret_obj['a1']['b1'], 'v1')

    def test_hello_world(self):
        message = self.getImpl().hello_world(self.getContext(), 'Roman')[0]
        self.assertEqual(message, 'Hello, Roman!')