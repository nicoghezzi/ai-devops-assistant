# AI DevOps Assistant

An end-to-end AI-powered DevOps application built with FastAPI, Docker, Kubernetes, GitHub Actions, and Prometheus monitoring.

This project demonstrates modern cloud-native engineering practices, including API development, AI integration, containerization, Kubernetes deployments, CI/CD automation, and observability.

---

## Architecture

```text
                +----------------+
                |     User       |
                +--------+-------+
                         |
                         v
                +----------------+
                |   FastAPI API  |
                +--------+-------+
                         |
                         v
                +----------------+
                |   OpenAI API   |
                +--------+-------+
                         |
                         v
                +----------------+
                |    Response    |
                +----------------+

CI/CD Flow

GitHub
   |
   v
GitHub Actions
   |
   v
Docker Build

Deployment Flow

Docker Image
   |
   v
Kubernetes (kind)

Monitoring

Application
   |
   v
Prometheus Metrics (/metrics)
```

---

## Features

* FastAPI REST API
* AI-powered DevOps assistant endpoint
* Dockerized application
* Kubernetes deployment using kind
* GitHub Actions CI pipeline
* Prometheus-compatible monitoring endpoint
* Health check endpoint
* Environment variable-based secret management

---

## Tech Stack

| Category         | Technology     |
| ---------------- | -------------- |
| Language         | Python         |
| API Framework    | FastAPI        |
| AI               | OpenAI API     |
| Containerization | Docker         |
| Orchestration    | Kubernetes     |
| Local Cluster    | kind           |
| CI/CD            | GitHub Actions |
| Monitoring       | Prometheus     |
| Version Control  | Git            |

---

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── main.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

## API Endpoints

### Health Check

**GET /**

Response:

```json
{
  "status": "running"
}
```

---

### Ask AI

**POST /ask**

Request:

```json
{
  "prompt": "How do I troubleshoot a Kubernetes pod?"
}
```

Response:

```json
{
  "answer": "..."
}
```

---

### Metrics

**GET /metrics**

Returns Prometheus-compatible metrics.

Example:

```text
# HELP http_requests_total Total HTTP Requests
# TYPE http_requests_total counter
http_requests_total 5
```

---

## Local Development

### Clone Repository

```bash
git clone https://github.com/nicoghezzi/ai-devops-assistant.git
cd ai-devops-assistant
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

### Run Application

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://localhost:8000/docs
```

---

## Docker

### Build Image

```bash
docker build -t ai-devops-assistant .
```

### Run Container

```bash
docker run -p 8000:8000 --env-file .env ai-devops-assistant
```

---

## Kubernetes Deployment

### Create Cluster

```bash
kind create cluster --name ai-cluster
```

### Load Docker Image

```bash
kind load docker-image ai-devops-assistant --name ai-cluster
```

### Deploy Application

```bash
kubectl apply -f k8s/
```

### Verify Pods

```bash
kubectl get pods
```

### Port Forward

```bash
kubectl port-forward svc/ai-devops-service 8080:80
```

Application:

```text
http://localhost:8080
```

Swagger:

```text
http://localhost:8080/docs
```

Metrics:

```text
http://localhost:8080/metrics
```

---

## Monitoring

The application exposes Prometheus-compatible metrics through:

```text
/metrics
```

Current custom metrics:

```text
http_requests_total
```

Default Python process metrics include:

* CPU usage
* Memory usage
* Garbage collection statistics
* Process uptime

---

## CI/CD Pipeline

GitHub Actions automatically:

* Checks out source code
* Installs dependencies
* Builds Docker image
* Validates application build

Pipeline runs automatically on push to the repository.

---

## Security

* API keys stored in environment variables
* `.env` excluded from source control
* GitHub Secret Scanning enabled
* No hardcoded credentials
* Secrets managed outside application code

---

## Future Enhancements

* Grafana dashboards
* Prometheus server deployment
* Helm charts
* ArgoCD GitOps deployment
* Terraform infrastructure provisioning
* AWS EKS deployment
* Horizontal Pod Autoscaler (HPA)
* Structured logging
* Distributed tracing

---

## Skills Demonstrated

* Python Development
* FastAPI
* AI Integration
* Docker
* Kubernetes
* CI/CD
* GitHub Actions
* Prometheus Monitoring
* DevSecOps Fundamentals
* Cloud-Native Application Development

---

## Author

**Nico Ghezzi**
