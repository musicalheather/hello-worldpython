# hello-python
Very simple hello world python Flask application.

Source
https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/


Useful Commands
docker images
docker build -f docker/Dockerfile -t hello-python:v6 .
kubectl set image deployment hello-python hello-python=hello-python:v6
kubectl delete -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl get pods