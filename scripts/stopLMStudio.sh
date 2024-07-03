# free up resources in codespace
ps -aux | grep -i studio | cut -d' ' -f6 | xargs -L1 kill -9 
docker ps -a | grep vnc | cut -d' ' -f1 | xargs -L1 docker rm -f