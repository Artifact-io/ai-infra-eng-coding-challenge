# Artifact AI Infrastructure Engineer Coding Challenge

## Part 1: Deploying a pre-trained model

### 1.1. Containerizing the model

In [part_1/1.1_containerize](part_1/1.1_containerize) you will need to implement an inference service in `main.py` serve the `Artifact-io/toy-sql-28M` pre-trained model over HTTP. You will also need to implement the `Dockerfile` to containerize the model and service.

You may use any framework(s) you like to serve the model such as:
* Flask
* FastAPI
* Kserve InferenceService


Requirements:
* Your container image should be able to detect and use GPUs if they are available.
* Your service should expose a `POST /predict` endpoint that will receive a JSON payload with the following format:
	```json
	{
		"instances": [{
			"question": "The question to create a SQL query for.",
			"context": "The context to create a SQL query for."
		}]
	}
	```
* `POST /predict`  should return a JSON payload with the following format:
	```json
	{
		"predictions": [
			"The SQL query that was generated."
		]
	}
	```

### 1.2. Deploying the model

In [part_1/1.2_deploy](part_1/1.2_deploy) you will need to create kubernetes manifests to deploy your model to a kubernetes cluster.

You may use any framework(s) you like to deploy the model including but not limited to:
* Kubernetes Deployments / Services
* Knative
* KServe

Requirements:
* Your service should be able to scale horizontally.
* Your service should be able to scale to zero when there is no traffic.

## Part 2: Monitoring the model

### 2.1. Metrics

In [part_2/2.1_metrics](part_2/2.1_metrics) you will need ensure that your service is emitting metrics that can be scraped by Prometheus.

Metrics:
* Request latency
* Request throughput
* Request success rate
* Request error rate

