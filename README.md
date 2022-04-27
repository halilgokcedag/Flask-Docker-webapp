# Flask-Docker-webapp

### About The Project

This small project deploys a Flask web app microservice on a Kubernetes environment using Docker. Web server returns a JSON response including specific information such as host IP address, visitor IP address, engine version and current date. Response will be in the following format:
```
{
  "timestamp": "<current date and time>",
  "hostname": "<Name of the host (IP also accepted)>",
  "engine": "<Name and/or version of the engine running>",
  "visitor ip": "<the IP address of the visitor>"
}
```

Project has a Dockerfile and two folders with a python file, a YAML file and a text file. App folder includes a python file and reqiurements.txt file for required python modules. Docker image has been already created and pushed to the Docker Hub. If needed, image can be re-created by using the Dockerfile in the repository. Deployment folder includes a YAML file to deploy the web app and the service for access to the web app via NodePort. Nodeport for this service will be 30300

## Built With

* Python
* Flask
* Docker
* Kubernetes (Minikube)

## Getting Started

### Prerequisites

This webapp can be deployed to any Kubernetes environment but only Minikube instructions will be provided in this page. Minikube and kubectl are required to deploy this app. If these tools are not already installed on your system, follow below steps. 

kubectl is required to communicate with Kubernetes cluster. Go to [Kubernetes website](https://kubernetes.io/docs/tasks/tools/) to install the kubectl.

To install a Minikube cluster, go to the [Minikube website](https://minikube.sigs.k8s.io/docs/start/)

If you are willing build image yourself, you need to install Docker. To install Docker, go to the [Docker Website](https://docs.docker.com/get-docker/)

Start your cluster as explained in the Minikube website. Once you can access to the cluster via kubectl, go to Deployment step.

### Deployment

1. Clone the repo and go to the deployment directory.

```
git clone https://github.com/halilgokcedag/Flask-Docker-webapp.git
```

If you want to build a new image and push to your Docker Hub repository, run the following commands by replacing the user value with your Docker Hub account. Remove the << and >> characters.

```
cd Flask-Docker-webapp/
docker build -t server-flask .
docker tag server-flask <<your_dockerhub_user>>/server-flask
docker login
docker push <<your_dockerhub_user>>/server-flask:latest
cd ../
```

2. Run the following commands to create the deployment and the service.

Note: If you created your image, replace the image value in the deploy.yaml file with the image name from your Docker hub.

```
cd Flask-Docker-webapp/deployment/
kubectl create -f deploy.yaml
```

3. Run the following command and copy the URL.

```
minikube service my-flask-app --url
```

4. Run the following command using the URL from step 3 or use a browser to access to the server.

```
curl <<url-from-step-3>>
```


### Cleanup
1. If the deployment is not needed anymore, run the following command to delete the deployment and the service.

```
kubectl delete -f deploy.yaml
```

