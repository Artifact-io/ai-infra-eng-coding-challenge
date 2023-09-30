# Artifact AI Infrastructure Challenge


## Part 1: Finetuning a model

### 1.1. Finetuning a model

In [part_1/1.1_finetune](part_1/1.1_finetune) you will find a script called `train.py`. You should modify the script so that it will finetune the `tiiuae/falcon-rw-1b` on the `b-mc2/sql-create-context` dataset.

Requirements:
* Detect and use GPUs if they are available.
* Produce training metrics to evaluate the model.
* Save the model upon completion.

Bonus:
* Allow the user to specify training parameters via command line arguments (e.g. `--batch_size`, `--learning_rate`, etc.).
* Allow the user to distribute training across multiple nodes using a framework of your choice. Extra credit for using a non-proprietary / OSS framework.

### 1.2. Multi-GPU training

In [part_1/1.2_multi_gpu](part_1/1.2_multi_gpu) you should modify your training script so that it will perform data parallel training on multiple GPUs.

Requirements:
* Your script should detect and use all available GPUs for training.


## Part 2: Deploying the model

### 2.1. Containerizing the model

In [part_2/2.1_containerize](part_2/2.1_containerize) you will need to create a `main.py` script that will load your model and serve it over HTTP. You will also need to create a `Dockerfile` and a `build.sh` script that will build a container image for your model.

You may use any framework(s) you like to serve the model.


Requirements:
* Your container image should be able to detect and use GPUs if they are available.
* Your service should should receive a JSON payload with the following format:
	```json
	{
		"instances": [{
			"question": "The question to create a SQL query for.",
			"context": "The context to create a SQL query for."
		}]
	}
	```
* Your service should return a JSON payload with the following format:
	```json
	{
		"predictions": [{
			"The SQL query that was generated."
		}]
	}
	```

### 2.2. Deploying the model

In [part_2/2.2_deploy](part_2/2.2_deploy) you will need to create kubernetes manifests to deploy your model to a kubernetes cluster.

You may use any framework(s) you like to deploy the model including but not limited to:
* Kubernetes Deployments / Services
* Knative
* KServe

Requirements:
* Your service should be able to scale horizontally.
* Your service should be able to scale to zero when there is no traffic.

## Part 3: Monitoring the model

### 3.1. Metrics

In [part_3/3.1_metrics](part_3/3.1_metrics) you will need ensure that your service is emitting metrics that can be scraped by Prometheus.

Metrics:
* Request latency
* Request throughput
* Request success rate
* Request error rate

