import tkinter as tk
from tkinter import messagebox
from backend.voter_operations import cast_vote
from backend.admin_operations import view_candidates


# ---------------- Functions ---------------- #

def show_candidates():
    candidates = view_candidates()
    text_area.delete("1.0", tk.END)
    for c in candidates:
        text_area.insert(tk.END, f"ID: {c[0]}, Name: {c[1]}, Party: {c[2]}\n")

def vote():
    try:
        candidate_id = int(entry_candidate.get())
        voter_id = int(label_voter_id["text"])
        cast_vote(voter_id, candidate_id)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Voter Dashboard")
root.geometry("500x500")

# Voter ID label (set this from login)
label_voter_id = tk.Label(root, text="0")  # This will be updated after login
label_voter_id.pack()

tk.Label(root, text="Candidate ID to vote").pack()
entry_candidate = tk.Entry(root)
entry_candidate.pack()

tk.Button(root, text="Vote", command=vote).pack(pady=10)
tk.Button(root, text="View Candidates", command=show_candidates).pack(pady=10)

# Text area to show candidates
text_area = tk.Text(root, height=15, width=60)
text_area.pack(pady=10)

root.mainloop()
