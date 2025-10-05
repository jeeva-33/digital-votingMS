import tkinter as tk
from tkinter import messagebox
from backend.admin_operations import add_candidate, view_candidates, view_results

# ---------------- Functions ---------------- #

def add_new_candidate():
    name = entry_name.get()
    party = entry_party.get()
    if name and party:
        add_candidate(name, party)
        messagebox.showinfo("Success", f"Candidate {name} added!")
    else:
        messagebox.showerror("Error", "Please enter name and party")

def show_candidates():
    candidates = view_candidates()
    text_area.delete("1.0", tk.END)
    for c in candidates:
        text_area.insert(tk.END, f"ID: {c[0]}, Name: {c[1]}, Party: {c[2]}\n")

def show_results():
    results = view_results()
    text_area.delete("1.0", tk.END)
    for r in results:
        text_area.insert(tk.END, f"ID: {r[0]}, Name: {r[1]}, Party: {r[2]}, Votes: {r[3]}\n")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Admin Dashboard")
root.geometry("500x500")

# Add candidate fields
tk.Label(root, text="Candidate Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Party").pack()
entry_party = tk.Entry(root)
entry_party.pack()

tk.Button(root, text="Add Candidate", command=add_new_candidate).pack(pady=10)
tk.Button(root, text="View Candidates", command=show_candidates).pack(pady=10)
tk.Button(root, text="View Results", command=show_results).pack(pady=10)

# Text area to show candidates/results
text_area = tk.Text(root, height=15, width=60)
text_area.pack(pady=10)

root.mainloop()
