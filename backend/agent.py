from strands import Agent, tool

@tool
def create_ticket(title: str, description: str, category: str, location: str, priority: str) -> str:
    """
    Create a campus support ticket.
    """
    # MVP: simulate ticket creation
    ticket_id = "CF1027"
    return (
        f"Ticket created successfully.\n"
        f"Ticket ID: {ticket_id}\n"
        f"Category: {category}\n"
        f"Location: {location}\n"
        f"Priority: {priority}"
    )

@tool
def check_ticket_status(ticket_id: str) -> str:
    """
    Check the current status of a campus ticket.
    """
    return f"{ticket_id}: IN PROGRESS"

@tool
def send_followup(ticket_id: str, department: str) -> str:
    """
    Send a follow-up request to the responsible department.
    """
    return f"Follow-up sent to {department} for ticket {ticket_id}."

@tool
def notify_student(message: str) -> str:
    """
    Notify the student about an important update.
    """
    return f"Student notification: {message}"

# Define the agent with available tools
agent = Agent(
    tools=[
        create_ticket,
        check_ticket_status,
        send_followup,
        notify_student
    ]
)