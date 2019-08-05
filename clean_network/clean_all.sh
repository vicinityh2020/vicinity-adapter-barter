ssh machine1 sudo 'docker stop $(sudo docker ps -aq)'
ssh machine1 sudo 'docker rm $(sudo docker ps -aq)'
ssh machine1 << EOF
  cd /home/device-Machine1-barter; 
  sudo ./start.sh 
EOF

ssh machine1 << EOF
  cd /home/device-Machine1-barter/hyperledger-explorer; 
  sudo ./start.sh 
EOF

ssh machine2 sudo 'docker stop $(sudo docker ps -aq)'
ssh machine2 sudo 'docker rm $(sudo docker ps -aq)'
ssh machine2 << EOF
  cd /home/device-Machine2-barter; 
  sudo ./start.sh 
EOF

ssh machine3 sudo 'docker stop $(sudo docker ps -aq)'
ssh machine3 sudo 'docker rm $(sudo docker ps -aq)'
ssh machine3 << EOF
  cd /home/device-Machine3-barter; 
  sudo ./start.sh 
EOF

ssh machine4 sudo 'docker stop $(sudo docker ps -aq)'
ssh machine4 sudo 'docker rm $(sudo docker ps -aq)'
ssh machine4 << EOF
  cd /home/device-Machine4-barter; 
  sudo ./start.sh 
EOF

ssh machine5 sudo 'docker stop $(sudo docker ps -aq)'
ssh machine5 sudo 'docker rm $(sudo docker ps -aq)'
ssh machine5 << EOF
  cd /home/device-Machine5-barter; 
  sudo ./start.sh 
EOF


