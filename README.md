# lamp on centos 8

# execute
ansible-playbook playbook_lamp.yaml


# reference 1
https://github.com/kodekloudhub/learning-app-ecommerce

# reference 2
https://medium.com/splunkuserdeveloperadministrator/creating-mysql-databases-with-ansible-925ab28598ab

# db confirm
mysql -u root -h localhost -p
mysql> use ecomdb;
mysql> show tables;
mysql> select * from products;


# web confirm
http://localhost