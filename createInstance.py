
import boto3

ec2 = boto3.resource('ec2')

user_data = '''#!/bin/bash
cd ~
sudo apt update -y 

curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install -y nodejs

curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update -y
sudo apt install -y yarn

npm install -g @aws-amplify/cli

wget -P /home/ubuntu/ "https://github.com/hjfarah/scrips_varios/archive/master.tar.gz"
tar -xvzf master.tar.gz
rm master.tar.gz
'''

user_data =""

instance = ec2.create_instances(ImageId='ami-06397100adf427136',
                                MinCount=1, MaxCount=1,
                                KeyName='tempnorth', SecurityGroupIds=['sg-0454cf8c78d306c84'],
                                UserData=user_data, InstanceType='t3.nano',
                                TagSpecifications=[{'Tags': [{'Key': 'vpnwest1','Value': 'vp1 borrable'}],
                                                    'ResourceType':'instance'}])

print(instance[0])


#sudo yum install docker -y
#sudo service docker start
#sudo usermod -a -G docker ec2-user

#images
#linux aws ami-0fcdcdb074d2bac5f

  #ubuntu
    #18 ami-06397100adf427136 (us-west)
    #16.04 ami-069339bea0125f50d

#security group
#us-west-1 sg-0454cf8c78d306c84
#us-east-1 sg-00037f6ce5028772a