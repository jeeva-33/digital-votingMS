from backend.db_connections import get_connection


# 1️⃣ Add a new candidate
def add_candidate(name, party):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Candidate (name, party) VALUES (%s, %s)"
    cursor.execute(query, (name, party))
    conn.commit()
    conn.close()
    print(f"✅ Candidate '{name}' from party '{party}' added successfully!")

# 2️⃣ View all candidates
def view_candidates():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Candidate"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

# 3️⃣ View voting results
def view_results():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT c.candidate_id, c.name, c.party, COUNT(v.vote_id) AS votes
    FROM Candidate c
    LEFT JOIN Vote v ON c.candidate_id = v.candidate_id
    GROUP BY c.candidate_id, c.name, c.party
    ORDER BY votes DESC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows
