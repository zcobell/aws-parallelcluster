# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.
import os
from copy import deepcopy

from pcluster.schemas.cluster_schema import ClusterSchema
from pcluster.utils import load_yaml_dict


def load_cluster_model_from_yaml(config_file_name, test_datadir=None):
    if test_datadir:
        path = test_datadir / config_file_name
    else:
        # If test_datadir is not specified, find configs in example_configs directory
        path = f"{os.path.dirname(__file__)}/example_configs/{config_file_name}"
    input_yaml = load_yaml_dict(path)
    print(input_yaml)
    copy_input_yaml = deepcopy(input_yaml)
    cluster = ClusterSchema(cluster_name="clustername").load(copy_input_yaml)
    print(cluster)
    return input_yaml, cluster
