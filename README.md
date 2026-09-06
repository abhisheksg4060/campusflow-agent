# CampusFlow

> An autonomous AI agent that handles repetitive campus coordination tasks using Strands Agents SDK.

---

## 🚨 Problem
Students spend significant time on repetitive coordination tasks:
- Reporting maintenance problems
- Finding the right department or staff member
- Checking request status
- Following up on unresolved issues
- Escalating when delays occur

The problem isn’t complexity — it’s repetition. Someone has to keep chasing these tasks.

---

## 💡 Solution
CampusFlow is an **autonomous AI agent** built with Strands Agents SDK and Amazon Bedrock.  
Instead of being “just another chatbot,” CampusFlow executes tasks in the background:

- Understands student requests  
- Classifies and routes to the correct department  
- Creates tickets  
- Monitors progress  
- Sends follow‑ups automatically  
- Escalates unresolved issues  
- Notifies students only when necessary  

---

## ✨ Features
- Natural‑language issue reporting  
- Automatic classification and routing  
- Ticket creation and tracking  
- Status monitoring  
- Automated follow‑ups  
- Escalation logic  
- Human‑in‑the‑loop approval for high‑impact actions  
- Background mode for continuous monitoring  

---

## 🏗️ Architecture

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python + FastAPI  
- **Agent**: Strands Agents SDK  
- **Model**: Amazon Bedrock  
- **Database**: SQLite (MVP), DynamoDB (scalable)  
- **Deployment**: AWS Lambda / AgentCore  

---

## 🏗️ CampusFlow Architecture

### Mermaid Diagram
```mermaid
flowchart LR
    A[Frontend (HTML/CSS/JS)] --> B[Backend (FastAPI)]
    B --> C[CampusFlow Agent (Strands SDK)]
    C --> D[Database (SQLite/DynamoDB)]
    B --> E[Deployment (AWS Lambda / AgentCore)]

___

## 📚 Tech Stack
- Strands Agents SDK  
- Amazon Bedrock  
- Python + FastAPI  
- SQLite / DynamoDB  
- AWS Lambda / AgentCore  

---

## ⚙️ Installation
```bash
git clone https://github.com/yourusername/campusflow-agent
cd campusflow-agent
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
pip install -r requirements.txt




