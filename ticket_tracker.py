'''
2. Python Programming Challenges for Customer Service Data Handling
Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
'''

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Open a new service ticket
def open_ticket(ticket_id, Customer, Issue):
    print("Open a new service ticket with the given details.")
    if ticket_id in service_tickets:
        print("Ticket ID already exists. Please choose a different ID.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": Issue, "Status": "open"}
print("Ticket {ticket_id} opened successfully.")
                              
# Update the status of an existing ticket
def update_ticket(ticket_id, status):
    print("Update the status of an existing ticket.")
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Ticket {ticket_id} status updated to {status}")
    else: 
        print("Ticket ID does not exist.")
# Display all tickets or filter by status
def display_ticket(status=None):
    print("Display all tickets or filter by status.")
    if status:
        filtered_tickets = {ticket_id: ticket for ticket_id, ticket in service_tickets() if ticket["Status"]== status}
        print(f"Tickets with status '{status}':")
        for ticket_id, ticket in filtered_tickets.items():
            print(f"Ticket ID: {ticket_id}")
            print(f"Customer: {ticket['Customer']}")
            print(f"Issue: {ticket['Issue']}")
            print(f"Status: {ticket['Status']}")
# Initialize with some sample tickets and include functionality for additional ticket entry
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

while True:
    print("Customer Service Ticket Tracker")
    print("-------------------------------")
    print("1. Open a new service ticket")
    print("2. Update the status of an existing ticket")
    print("3. Display all tickets")
    print("4. Display tickets by status")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        ticket_id = input("Enter ticket ID: ")
        customer = input("Enter customer name: ")
        issue = input("Enter issue description: ")
        open_ticket(ticket_id, customer, issue)
    elif choice == "2":
        ticket_id = input("Enter ticket ID: ")
        status = input("Enter new status (open/closed): ")
        update_ticket(ticket_id, status)
    elif choice == "3":
        display_ticket()
    elif choice == "4":
        status = input("Enter status to filter by (open/closed): ")
        display_ticket(status)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
