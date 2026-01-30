contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print(f"Alice's Number :{contacts["Alice"]}")
contacts["Diana"] ="555-4321"
print(f"Contacts after adding Diana: {contacts}")
contacts["Bob"] ="555-0000"
print(f"Contacts after updating Bob: {contacts}")
del contacts["Charlie"]
print(f"Contacts after delteling Chaelie: {contacts}")
print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))
