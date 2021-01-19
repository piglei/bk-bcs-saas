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
import os
import tempfile
import codecs
import contextlib


@contextlib.contextmanager
def save_to_temporary_dir(files):
    """"""
    with tempfile.TemporaryDirectory() as tempdir:
        for filename, content in files.items():
            filename = "%s.yaml" % filename
            fullfilename = os.path.join(tempdir, filename)
            directory = os.path.dirname(fullfilename)
            if not os.path.exists(directory):
                os.makedirs(directory)
            with codecs.open(fullfilename, 'w+', encoding='utf-8') as fp:
                fp.write(content.decode("utf-8"))
        yield tempdir
