from backend.db_connections import get_connection

# 1️⃣ Register a new voter
def register_voter(name, age, gender, username, password):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO Voter (name, age, gender, username, password)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, age, gender, username, password))
    conn.commit()
    conn.close()
    print(f"✅ Voter '{name}' registered successfully!")

# 2️⃣ Voter login
def voter_login(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT voter_id, has_voted FROM Voter WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    voter = cursor.fetchone()
    conn.close()
    return voter  # Returns (voter_id, has_voted) or None if login fails

# 3️⃣ Cast a vote
def cast_vote(voter_id, candidate_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Check if voter already voted
    cursor.execute("SELECT has_voted FROM Voter WHERE voter_id=%s", (voter_id,))
    has_voted = cursor.fetchone()[0]
    
    if has_voted:
        print("❌ Voter has already voted!")
        conn.close()
        return
    
    # Record vote
    query = "INSERT INTO Vote (voter_id, candidate_id) VALUES (%s, %s)"
    cursor.execute(query, (voter_id, candidate_id))
    
    # Update voter status
    cursor.execute("UPDATE Voter SET has_voted=1 WHERE voter_id=%s", (voter_id,))
    
    conn.commit()
    conn.close()
    print("✅ Vote cast successfully!")
