# 🛒 Mini Shopping App (DevOps Practice)

A simple Python Flask shopping app built for practicing:

- Docker
- Docker Compose
- Jenkins CI/CD
- SonarQube

---

## 🚀 Tech Stack
- Python (Flask)
- SQLite
- Docker & Docker Compose
- Jenkins
- SonarQube

---

## 📂 Project Structure
shopping-app/
├── app/
│ ├── app.py
│ ├── models.py
│ ├── requirements.txt
│ └── templates/
├── tests/
│ └── test_app.py
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── sonar-project.properties

yaml
Copy code

---

## ▶ Run Locally
```bash
pip install -r app/requirements.txt
cd app
python models.py
python app.py
Open: http://localhost:5000

🐳 Docker
bash
Copy code
docker build -t shopping-app .
docker run -p 5000:5000 shopping-app
🐳 Docker Compose
bash
Copy code
docker-compose up --build
🤖 Jenkins
Pipeline includes:

Git checkout

Docker build

Unit tests

SonarQube scan

📊 SonarQube
bash
Copy code
sonar-scanner
✅ Learning Outcome
Containerization

CI/CD pipelines

Code quality analysis

DevOps workflow

yaml
Copy code

---

## 📄 `tests/test_app.py`
👉 Simple **pytest** test (SonarQube friendly)

```python
from app.app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_cart_page():
    client = app.test_client()
    response = client.get("/cart")
    assert response.status_code == 200
Install test dependency:
bash
Copy code
pip install pytest
Run tests:

bash
Copy code
pytest
