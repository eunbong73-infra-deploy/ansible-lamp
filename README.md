# lamp on centos 8

## install ansible
sudo yum install ansible -y

## execute
ansible-playbook -i inventory.txt playbook_lamp.yaml


## reference 1
https://github.com/kodekloudhub/learning-app-ecommerce

## reference 2
https://medium.com/splunkuserdeveloperadministrator/creating-mysql-databases-with-ansible-925ab28598ab

## db confirm
- mysql -u root -h localhost -p
- mysql> use ecomdb;
- mysql> show tables;
- mysql> select * from products;


## web confirm
http://localhost


## python관련 설치..
- python 3.10 이상 install
- fastapi install  :  /usr/local/bin/python3.10 -m pip install "fastapi[all]"
- tailer install   :  /usr/local/bin/python3.10 -m pip install tailer
- fasitapi github  : https://github.com/tiangolo/fastapi
- tailer github    : https://github.com/six8/pytailer


## 소스 수정
- main.py 디렉토리로 이동
- playbook이 설치된 Directory로 소스 수정 (main.py)
   ans_base_dir="/home/osboxes/ansible-demos-exercises/"
   job_base_dir= ans_base_dir + "lamp_handson/"

## 실행
- uvicorn main:app --reload


## 테스트 방법
- 실행트리거       : curl localhost:8000/create
- 설치과정로그     : curl localhost:8000/createLog
- 특정위치이후로그 : curl localhost:8000/createLog?startLine=10
