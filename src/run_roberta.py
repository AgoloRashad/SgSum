#   Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
sys.path.append("/content/drive/MyDrive/EMNLP2021-SgSum/src")

# import argparse
from utils.args import print_arguments
from utils.logging import init_logger
from utils.check import check_gpu

from networks.roberta_multigraphextsum.run_graphsum import main as run_multigraphsum
from run_args import parser as run_parser
from data_preprocess.preprocess_graphextsum_data import do_format_to_json, do_format_to_paddle

if __name__ == "__main__":
    args = run_parser.parse_args()
    print_arguments(args)
    init_logger(args.log_file)
    check_gpu(args.use_cuda)

    if args.do_preprocessing:
        if not os.path.exists(args.json_path):
          os.mkdir(args.json_path)

        if not os.path.exists(args.data_path):
          os.mkdir(args.data_path)
      
        do_format_to_json(args)
        do_format_to_paddle(args)

        args.test_set = args.data_path

    if args.model_name == 'graphsum':
        run_graphsum(args)
    elif args.model_name == 'multigraphsum':
        run_multigraphsum(args)
    else:
        raise ValueError("Model %s is not supported currently!" % args.model_name)
