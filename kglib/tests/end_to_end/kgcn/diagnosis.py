#
#  Copyright (C) 2022 Vaticle
#
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.
#
import sys
import unittest

from kglib.kgcn_tensorflow.examples.diagnosis.diagnosis import diagnosis_example
from kglib.utils.typedb.test.base import TypeDBServer


class TestDiagnosisExample(unittest.TestCase):
    def setUp(self):
        self._tdb = TypeDBServer(sys.argv.pop())
        self._tdb.start()
        self._typedb_binary_location = self._tdb.typedb_binary_location
        self._data_file_location = sys.argv.pop()
        self._schema_file_location = sys.argv.pop()

    def tearDown(self):
        self._tdb.stop()

    def test_learning_is_done(self):
        solveds_tr, solveds_ge = diagnosis_example(self._typedb_binary_location,
                                                   schema_file_path=self._schema_file_location,
                                                   seed_data_file_path=self._data_file_location)
        self.assertGreaterEqual(solveds_tr[-1], 0.7)
        self.assertLessEqual(solveds_tr[-1], 0.99)
        self.assertGreaterEqual(solveds_ge[-1], 0.7)
        self.assertLessEqual(solveds_ge[-1], 0.99)


if __name__ == "__main__":
    # This handles the fact that additional arguments that are supplied by our py_test definition
    # https://stackoverflow.com/a/38012249
    unittest.main(argv=['ignored-arg'])
