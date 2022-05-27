#!/bin/bash
cd /home/osboxes/ansible-demos-exercises/lamp_handson
#ansible-playbook -i ./inventory.txt  ./playbook_lamp.yaml > test.log &
ansible-playbook -i ./inventory.txt  ./playbook_lamp.yaml
