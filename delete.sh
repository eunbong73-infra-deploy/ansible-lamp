#!/bin/bash
#ansible-playbook -i /home/osboxes/ansible-demos-exercises/lamp_handson ./playbook_lamp.yaml
cd /home/osboxes/ansible-demos-exercises/lamp_handson
ansible-playbook -i ./inventory.txt ./x_clean.yaml
