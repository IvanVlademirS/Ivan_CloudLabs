# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import boto3

def create_detector(client):
    client.create_detector();

region='us-east-1'

# Create GuardDuty client
gd = boto3.client(
    service_name='guardduty',
    region_name=region
    )

#Get the GuardDuty Detector for the current AWS Region
detector=gd.list_detectors()
if len(detector['DetectorIds']) > 0:
    detector_id = detector['DetectorIds'][0]
    print('Detector exists in Region ' + region + ' Detector Id: ' + detector_id)
else:
    print('GuardDuty Detector does not exist in Region ' + region)
    print('Creating Detector in ' + region + ' ...')
    create_detector(gd)

