"""
You must have an AWS account to use this Python code.
© 2024, Amazon Web Services, Inc. or its affiliates. All rights reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

#####################################################################
# file: aws-lambda-python-layer-app.py
# author: bishrt@amazon.com
# date: 07-25-2024
# AWS CLI reference: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker
# AWS Boto3 SDK reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html
# Lambda Best Practices reference: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
# Lambda Developer reference: https://aws.amazon.com/blogs/architecture/best-practices-for-developing-on-aws-lambda/
# Lambda Python reference: https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html
#####################################################################

#####################################################################
# IMPORTS
# base imports part of Lambda Python runtime
import json
import os
import logging
import time
import sys
import math
# the following imports are EXTENSIONS and MUST REQUIRE a Lambda layer
import packaging
import requests

#####################################################################
# LOGGING
#####################################################################
logger = logging.getLogger()
# logger.handler == console
csh = logging.StreamHandler()
logger.addHandler(csh)
# logger.level
logger.setLevel(logging.INFO)

logger.info("Initializing Lambda function...")

#####################################################################
# LAMBDA.MAIN()
#####################################################################

def lambda_handler(event, context):
    logger.info('Executing Lambda function...')

    logger.info("Hello World!")

    return {
        "statusCode": 200,
        'body' : json.dumps('Hello World!')
    }

# NO PROGRAM.MAIN()