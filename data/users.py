from models.user import User
user_data = [
    {"first_name": "Alice", "last_name": "Johnson", "email": "alice@example.com", "password": "password123"},
    {"first_name": "Bob", "last_name": "Smith", "email": "bob@example.com", "password": "securepass456"},
    {"first_name": "Charlie", "last_name": "Brown", "email": "charlie@example.com", "password": "pass789"}
]

# Create a list of User objects
users = [User(user["first_name"],user["last_name"],user["email"],user["password"]) for user in user_data]