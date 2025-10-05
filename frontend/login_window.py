import tkinter as tk
from tkinter import messagebox
from backend.admin_operations import view_candidates, view_results
from backend.voter_operations import voter_login, register_voter



# ------------------ Functions ------------------ #

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check admin login
    if username == "admin" and password == "admin123":
        messagebox.showinfo("Login Success", "Welcome Admin!")
        # TODO: Open admin dashboard
        return

    # Check voter login
    voter = voter_login(username, password)
    if voter:
        voter_id, has_voted = voter
        messagebox.showinfo("Login Success", f"Welcome Voter! Voted: {has_voted}")
        # TODO: Open voter dashboard
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# ------------------ GUI ------------------ #

root = tk.Tk()
root.title("Voting Management System - Login")
root.geometry("400x250")

# Labels
tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Login Button
tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()
