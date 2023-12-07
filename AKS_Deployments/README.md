# AKS

## Table of Contents

- [Getting Started](#getting_started)
- [Usage](#usage)

## Getting Started <a name = "getting_started"></a>


### Prerequisites

Make sure you have RBAC permissions to the cluster and kubelogin installed.
link:  https://azure.github.io/kubelogin/install.html

### Installing

Connect to the cluster

powershell
```
import-AzAksCredential -ResourceGroupName <resourceGroup_Name> -Name <Cluster_name>
Press y
```

Deploy to the cluster nginx ingress controller

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.3.0/deploy/static/provider/cloud/deploy.yaml
```

Check if you see an external ip for the ingress controller

```
kubectl get service ingress-nginx-controller --namespace=ingress-nginx
```

Apply the two servers and their services

```
kubectl apply -f ServiceA.yaml --namespace ingress-nginx
kubectl apply -f ServiceB.yaml --namespace ingress-nginx
```

Check to see if all the pods are running correctly

```
kubectl get pods --namespace ingress-nginx
```

Apply the load balancer

```
kubectl apply -f IngressController.yaml --namespace ingress-nginx
```



## Usage <a name = "usage"></a>

now that you are done, you can run Get command with the ip and path, for example
```
invoke-restmethod -method GET -uri https://X.X.X.X/serviceA
```
