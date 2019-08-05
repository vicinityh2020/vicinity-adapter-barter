ssh machine1 sudo 'docker stop $(sudo docker ps -aq)'
ssh machine1 sudo 'docker rm $(sudo docker ps -aq)'
ssh machine1 sudo '/home/device-Machine1-barter/start.sh'
