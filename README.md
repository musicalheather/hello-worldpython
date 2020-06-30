# hello-python
Very simple hello world python Flask application.

Source
https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/

Useful Commands

#List Images

docker images

#Build new version

docker build -f docker/Dockerfile -t hello-python:v10 .

#Tell Kubernetes to deploy new version to pods

kubectl set image deployment hello-python hello-python=hello-python:v10

#List out Kubernetes pods

kubectl get pods

#SSH into specified pod

kubectl exec -it podname -- /bin/bash

#Create kubernetes deployment

kubectl apply -f kubernetes/deployment.yaml

#Delete kubernetes deployment

kubectl delete -f kubernetes/deployment.yaml

