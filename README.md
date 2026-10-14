
# AI DevOps Assistant

An AI-powered DevOps application built with FastAPI, Docker, Kubernetes, and GitHub Actions. Integrates the OpenAI API with automated application delivery and Prometheus-compatible monitoring.

## Architecture

```text
User → FastAPI → OpenAI API → Response

GitHub → GitHub Actions → Docker Image
                              ↓
                         Kubernetes
                              ↓
                     Prometheus Metrics
```

## Tech Stack & Features

- **Language & API:** Python, FastAPI, REST endpoints
- **AI Integration:** OpenAI API for AI-powered DevOps assistance
- **Containers & Orchestration:** Docker, Kubernetes, kind
- **CI/CD:** GitHub Actions for dependency installation and build validation
- **Observability:** Prometheus-compatible metrics, health checks, Python process metrics
- **Security:** Environment-based secrets, `.env` exclusion, GitHub Secret Scanning

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

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Application health check |
| POST | `/ask` | Submit a DevOps question to the AI assistant |
| GET | `/metrics` | Expose Prometheus-compatible metrics |

Example request to `/ask`:

```json
{
  "prompt": "How do I troubleshoot a Kubernetes pod?"
}
```

## Local Development

Clone the repository and install dependencies:

```bash
git clone https://github.com/nicoghezzi/ai-devops-assistant.git
cd ai-devops-assistant

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

Run the application:

```bash
uvicorn main:app --reload
```

Swagger UI: `http://localhost:8000/docs`

## Docker Deployment

Build and run the container:

```bash
docker build -t ai-devops-assistant .
docker run -p 8000:8000 --env-file .env ai-devops-assistant
```

## Kubernetes Deployment (kind)

Create a local cluster and load the Docker image:

```bash
kind create cluster --name ai-cluster
kind load docker-image ai-devops-assistant --name ai-cluster
```

Deploy and verify:

```bash
kubectl apply -f k8s/
kubectl get pods
kubectl port-forward svc/ai-devops-service 8080:80
```

Access the application:

- **API:** `http://localhost:8080`
- **Swagger UI:** `http://localhost:8080/docs`
- **Metrics:** `http://localhost:8080/metrics`

## CI/CD & Monitoring

GitHub Actions automates dependency installation and application build validation on repository pushes. The application exposes request metrics through `/metrics`, including custom HTTP request counters and default Python process metrics.

## Engineering Decisions & Trade-offs

| Decision | Rationale | Trade-off |
|---|---|---|
| **FastAPI for the API layer** | Lightweight framework with automatic API documentation. | Requires explicit handling of input validation, timeouts, and external API errors. |
| **OpenAI API over self-hosted models** | Avoids operating model-serving infrastructure. | Introduces usage costs, external dependency latency, and data privacy considerations. |
| **Docker and Kubernetes** | Provides portable packaging and declarative deployment. | Adds image management and orchestration complexity compared with a standalone container. |
| **kind for local Kubernetes** | Enables local deployment and testing without an AWS cluster. | Does not validate production EKS networking, IAM, or managed infrastructure behavior. |
| **GitHub Actions for CI** | Keeps build validation alongside source code. | The current pipeline validates the build but does not establish automated Kubernetes deployment. |
| **Prometheus-compatible metrics** | Enables application-level visibility and future monitoring integration. | A metrics endpoint alone does not provide a complete monitoring and alerting system. |

## Security

- Load API keys through environment variables.
- Exclude `.env` from source control.
- Use GitHub Secret Scanning to help detect accidental credential exposure.
- Avoid hardcoding credentials in application code or container images.

## Future Enhancements

- Prometheus server and Grafana dashboards
- Helm charts and ArgoCD GitOps deployment
- Terraform-managed AWS EKS infrastructure
- Horizontal Pod Autoscaler (HPA)
- Structured logging and distributed tracing

---

## 🚀 Author
Nicolas Ghezzi LinkedIn: https://www.linkedin.com/in/nghezzi/
