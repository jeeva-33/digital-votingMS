from backend.admin_operations import add_candidate, view_candidates, view_results

# Add sample candidate
add_candidate("John Doe", "Party A")

# View all candidates
print("Candidates:", view_candidates())

# View results
print("Results:", view_results())
