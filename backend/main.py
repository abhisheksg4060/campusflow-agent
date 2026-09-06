from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent   # import the CampusFlow agent

app = FastAPI(title="CampusFlow API")

# Define the request model
class Request(BaseModel):
    message: str

# Health check endpoint
@app.get("/")
def home():
    return {"status": "CampusFlow running"}

# Main agent endpoint
@app.post("/agent")
def run_agent(request: Request):
    result = agent(request.message)
    return {"response": str(result)}

# Optional: direct ticket creation endpoint
@app.post("/ticket")
def create_ticket(request: Request):
    return {"ticket": str(agent.tools['create_ticket'](
        title="Issue",
        description=request.message,
        category="general",
        location="unknown",
        priority="Medium"
    ))}

# Optional: check ticket status endpoint
@app.get("/status/{ticket_id}")
def check_status(ticket_id: str):
    return {"status": str(agent.tools['check_ticket_status'](ticket_id))}