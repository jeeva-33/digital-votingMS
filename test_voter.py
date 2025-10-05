from backend.voter_operations import register_voter, voter_login, cast_vote

# Register a new voter
register_voter("Alice", 25, "Female", "alice123", "pass123")

# Login
voter = voter_login("alice123", "pass123")
print("Login info:", voter)

# Cast vote
if voter:
    voter_id, has_voted = voter
    cast_vote(voter_id, 1)  # Voting for candidate_id=1
