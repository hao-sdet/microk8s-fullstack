# MicroK8s Fullstack
Sources: https://microk8s.io/docs

## Requirements
+ A Raspberry Pi running Ubuntu Server 20.04 LTS (*slow)

## Setup
### Installing and configuring the Raspberry Pi
1. Update
```
$ sudo apt update
$ sudo apt upgrade
```
2. Enable SSH
```
$ sudo apt install openssh-server
$ sudo systemctl status ssh
```
3. Set Hostname
```
$ sudo hostnamectl set-hostname my-NewHostName
$ sudo nano /etc/hosts (Replace the existing computer name with your new hostname ex: 127.0.0.1 localhost -> 172.0.0.1 my-NewHostName localhost)
$ sudo reboot
$ ssh ubuntu@my-NewHostName
```
4. Install Node and Npm
```
$ sudo apt-get install nodejs
$ sudo apt-get install npm
```
5. Install Docker
```
$ sudo apt-get install docker.io
$ sudo systemctl enable docker
$ sudo systemctl start docker
```
6. Install microk8s
```
$ sudo snap install microk8s --classic
```

### Build and test Docker images
1. Create and test front-end Docker image
```
$ cd frontend
$ sudo docker build . -t react-nginx-frontend:local
$ sudo docker run --detach --name react-frontend-container -p 81:80 react-nginx-frontend:local
Open a browser and type in http://host-ip:81 (where host-ip is the server ip address)
```
2. Create and test back-end Docker image
```
$ cd backend
$ sudo docker build . -t flask-api-backend:local
$ sudo docker run --detach --name flask-backend-container -p 5001:5000 flask-api-backend:local
Open a browser and type in http://host-ip:5001 (where host-ip is the server ip address)
```

### Deploying on MicroK8s (Kubernetes)
1. Create MicroK8s alias
```
$ sudo snap alias microk8s.kubectl kubectl (To revert back, type: snap unalias kubectl)
```
2. Enable Microk8s add-ons
!Once enabled, registry will be available at localhost:32000
```
$ sudo microk8s enable dns storage registry
```
3. Build Docker images
```
$ sudo docker build . -t localhost:32000/react-nginx-frontend:registry
$ sudo docker build . -t localhost:32000/flask-api-backend:registry
$ docker images
```
4. Push Docker images to MicroK8s registry
```
$ sudo docker push localhost:32000/react-nginx-frontend
$ sudo docker push localhost:32000/flask-api-backend
```
5. Create TLS secret
```
$ chmod +x ./generate.sh
$ ./generate.sh
```
6. Enable ingress with ssl certificate
```
$ microk8s enable ingress:default-ssl-certificate=default/secret/example-com-tls
```
7. Deploy Manually
Database
```
$ kubectl apply -f postgres-configmap.yaml
$ kubectl apply -f postgres-storage.yaml
$ kubectl apply -f postgres-secret.yaml
$ kubectl apply -f postgres-deployment.yaml
```
Backend
```
$ kubectl apply -f flask-secret.yaml
$ kubectl apply -f flask-deployment.yaml
```
Frontend
```
$ kubectl apply -f react-deployment.yaml
```
Ingress
```
$ kubectl apply -f backend-ingress.yaml
$ kubectl apply -f frontend-ingress.yaml
```
8. Verify deployment
```
$ curl -k https://example.com
$ curl -k https://api.example.com
```

### Deploy with Helm
1. Enable helm add-on
!This will enable helm3 (w/o Tiller server)
```
$ sudo microk8s enable helm3
```
2. Verify configuration
! This will show the final configuration blob
```
$ cd helm/
$ sudo microk8s helm3 template .
```
3. Deploy
```
$ microk8s helm3 install .
```
4. Uninstall
```
$ microk8s helm3 delete <name>
```

### Microk8s Useful Commands
1. Deploy
```
$ kubectl apply -f <configuration>.yaml
```
2. Terminate deployment
```
$ kubectl delete -f <configuration>.yaml
```
3. Show clusters event logs
```
$ kubectl get events
```
4. Show all pods
```
$ kubectl get pods -o wide
```
5. Show pods log
```
$ kubectl logs <POD_NAME>
```

