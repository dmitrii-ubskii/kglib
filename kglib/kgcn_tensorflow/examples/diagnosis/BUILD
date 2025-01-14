#
# Copyright (C) 2022 Vaticle
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

load("@rules_python//python:defs.bzl", "py_test", "py_library")
load("@vaticle_kglib_pip//:requirements.bzl",
       vaticle_kglib_requirement = "requirement")
load("@vaticle_dependencies//tool/checkstyle:rules.bzl", "checkstyle_test")

py_test(
    name = "diagnosis_test",
    srcs = [
        "diagnosis_test.py"
    ],
    deps = [
        "diagnosis",
        "//kglib/utils/graph/test",
        vaticle_kglib_requirement('numpy'),
        vaticle_kglib_requirement('networkx'),
        vaticle_kglib_requirement('decorator'),
    ]
)

py_library(
    name = "diagnosis",
    srcs = [
        'diagnosis.py'
    ],
    deps = [
        "//kglib/kgcn_tensorflow/pipeline",
        "//kglib/kgcn_tensorflow/learn",
        "//kglib/kgcn_tensorflow/plot",
        "//kglib/kgcn_tensorflow/models",
        "//kglib/utils/typedb/synthetic",
        "//kglib/utils/typedb/type",
        "@vaticle_typedb_client_python//:client_python",
    ],
    visibility=['//visibility:public']
)

checkstyle_test(
    name = "checkstyle",
    include = glob(["*"]),
    license_type = "apache",
)
