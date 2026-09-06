import pytest
from backend.agent import agent

def test_create_ticket():
    # Simulate a student reporting a Wi-Fi issue
    result = agent("Wi-Fi issue in Hostel A")
    assert "Ticket created" in str(result)

def test_check_ticket_status():
    # Simulate checking the status of a ticket
    status = agent.tools['check_ticket_status']("CF1027")
    assert "IN PROGRESS" in str(status)

def test_notify_student():
    # Simulate notifying a student
    message = agent.tools['notify_student']("Your ticket has been resolved.")
    assert "Student notification" in str(message)