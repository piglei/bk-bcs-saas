# -*- coding: utf-8 -*-
#
# Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
# Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
import json

import pytest
from django.conf import settings

from backend.resources.workloads.daemonset.formatter import DaemonSetFormatter


@pytest.fixture(scope="module", autouse=True)
def daemonset_configs():
    with open(settings.BASE_DIR + '/backend/tests/resources/formatter/workloads/contents/daemonset.json') as fr:
        configs = json.load(fr)
    return configs


class TestDaemonsetFormatter:
    def test_format_dict(self, daemonset_configs):
        """ 测试 format_dict 方法 """
        result = DaemonSetFormatter().format_dict(daemonset_configs['normal'])
        assert set(result.keys()) == {'images', 'age', 'createTime', 'updateTime'}
        assert result['images'] == ['k8s.gcr.io/kube-proxy:v1.20.2']
