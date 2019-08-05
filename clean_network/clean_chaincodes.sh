ssh machine1 sudo 'docker stop $(sudo docker ps -aq --filter="name=dev-peer")'
ssh machine1 sudo 'docker rm $(sudo docker ps -aq --filter="name=dev-peer")'

ssh machine2 sudo 'docker stop $(sudo docker ps -aq --filter="name=dev-peer")'
ssh machine2 sudo 'docker rm $(sudo docker ps -aq --filter="name=dev-peer")'

ssh machine3 sudo 'docker stop $(sudo docker ps -aq --filter="name=dev-peer")'
ssh machine3 sudo 'docker rm $(sudo docker ps -aq --filter="name=dev-peer")'

ssh machine4 sudo 'docker stop $(sudo docker ps -aq --filter="name=dev-peer")'
ssh machine4 sudo 'docker rm $(sudo docker ps -aq --filter="name=dev-peer")'

ssh machine5 sudo 'docker stop $(sudo docker ps -aq --filter="name=dev-peer")'
ssh machine5 sudo 'docker rm $(sudo docker ps -aq --filter="name=dev-peer")'