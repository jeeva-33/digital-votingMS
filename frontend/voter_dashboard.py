import tkinter as tk
from tkinter import messagebox
from backend.voter_operations import cast_vote
from backend.admin_operations import view_candidates

def open_dashboard(voter_id):
    voter_root = tk.Toplevel()
    voter_root.title("Voter Dashboard")
    voter_root.geometry("500x500")

    # Header
    tk.Label(voter_root, text=f"Voter Dashboard", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(voter_root, text=f"Voter ID: {voter_id}", font=("Arial", 12)).pack(pady=5)

    # Candidate input
    tk.Label(voter_root, text="Enter Candidate ID to Vote").pack(pady=5)
    entry_candidate = tk.Entry(voter_root)
    entry_candidate.pack(pady=5)

    # Text area
    text_area = tk.Text(voter_root, height=15, width=60)
    text_area.pack(pady=10)

    # Functions
    def show_candidates():
        candidates = view_candidates()
        text_area.delete("1.0", tk.END)
        for c in candidates:
            text_area.insert(tk.END, f"ID: {c[0]}, Name: {c[1]}, Party: {c[2]}\n")

    def vote():
        try:
            candidate_id = int(entry_candidate.get())
            cast_vote(voter_id, candidate_id)
            messagebox.showinfo("Success", "Vote cast successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Buttons
    tk.Button(voter_root, text="View Candidates", command=show_candidates).pack(pady=5)
    tk.Button(voter_root, text="Vote", command=vote).pack(pady=5)

    # Exit button
    tk.Button(voter_root, text="Logout", command=voter_root.destroy).pack(pady=10)

    voter_root.mainloop()
