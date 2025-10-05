import tkinter as tk
from tkinter import messagebox
from backend.voter_operations import voter_login
import frontend.voter_dashboard as voter_dashboard

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Admin login
    if username == "admin" and password == "admin123":
        messagebox.showinfo("Login Success", "Welcome Admin!")
        import frontend.admin_dashboard
        return

    # Voter login
    voter = voter_login(username, password)
    if voter:
        voter_id, has_voted = voter
        messagebox.showinfo("Login Success", f"Welcome Voter! Voted: {has_voted}")
        root.withdraw()  # hide login window
        voter_dashboard.open_dashboard(voter_id)  # ✅ opens new window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Voting Management System - Login")
root.geometry("400x250")

tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()


