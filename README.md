# AKS-BItcoin

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

An Azure Kubernetes Service (AKS) cluster is configured to run two API services, both dedicated to providing real-time information on the current value of Bitcoin.

### Service A:

Service A, one of the API services within the AKS cluster, is designed with the following features:

#### Real-time Bitcoin Value:

Service A continuously fetches and displays the current value of Bitcoin.

#### Timely Print:

The service incorporates a timely print mechanism, ensuring regular updates on the Bitcoin value at specified intervals.

#### Average Calculation:

Service A calculates and displays the average value of Bitcoin over the last 10 minutes. This provides a snapshot of the recent trend in Bitcoin prices.
By combining real-time updates with a periodic average, Service A offers a comprehensive view of Bitcoin's value, making it a valuable resource for users seeking both instantaneous and historical insights.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your cloud environment

### Prerequisites

```
1. Azure Account
2. Kubelogin: https://azure.github.io/kubelogin/install.html
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Inside of the directory AKS_Terraform run apply the terraform file

```
cd AKS_Terraform
terraform apply --auto-approve
```
continue with the steps inside of the AKS_Deployments directory


