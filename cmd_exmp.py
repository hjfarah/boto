
import boto3

ec2 = boto3.resource('ec2')

user_data = '''#!/bin/bash
cd ~
sudo yum update -y
sudo yum install nodejs
sudo yum install git
'''

instance = ec2.create_instances(ImageId='ami-035b3c7efe6d061d5',
                                MinCount=1, MaxCount=1,
                                KeyName='newBei', SecurityGroupIds=['sg-00037f6ce5028772a'],
                                UserData=user_data, InstanceType='t3a.nano')

print(instance[0].id)

#113.57.226.168

#056ee704806822732 0b898040803850657 035b3c7efe6d061d5
