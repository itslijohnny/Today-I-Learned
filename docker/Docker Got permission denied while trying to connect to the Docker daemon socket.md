# Docker Got permission denied while trying to connect to the Docker daemon socket

  
[Docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock](https://stackoverflow.com/questions/47854463/docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socke)  
  
  
```  
sudo groupadd docker  
sudo usermod -a -G docker $USER  
```  
  
Then restart/ log out and log in