import mysql.connector

# ----------------- Database Connection ----------------- #
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # replace with your MySQL password
        database="voting_db"
    )

# ----------------- Create Tables ----------------- #
def create_tables(cursor):
    # Admin table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Admin (
        admin_id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) UNIQUE,
        password VARCHAR(50)
    )
    """)

    # Voter table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Voter (
        voter_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100),
        age INT,
        username VARCHAR(50) UNIQUE,
        password VARCHAR(50),
        has_voted BOOLEAN DEFAULT FALSE
    )
    """)

    # Candidate table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Candidate (
        candidate_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100),
        party VARCHAR(50)
    )
    """)

    # Vote table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vote (
        vote_id INT PRIMARY KEY AUTO_INCREMENT,
        voter_id INT,
        candidate_id INT,
        FOREIGN KEY (voter_id) REFERENCES Voter(voter_id),
        FOREIGN KEY (candidate_id) REFERENCES Candidate(candidate_id)
    )
    """)

# ----------------- Create Basic Triggers ----------------- #
def create_triggers(cursor):
    # Basic trigger to log underage voter
    try:
        cursor.execute("""
        CREATE TRIGGER trg_voter_age_check
        BEFORE INSERT ON Voter
        FOR EACH ROW
        BEGIN
            IF NEW.age < 18 THEN
                SELECT CONCAT('Warning: Voter ', NEW.name, ' is under 18.');
            ELSE
                SELECT CONCAT('Voter ', NEW.name, ' registered successfully.');
            END IF;
        END
        """)
        print("Trigger trg_voter_age_check created.")
    except Exception as e:
        print(f"Trigger creation skipped or already exists: {e}")

    # Basic trigger to log vote insertion
    try:
        cursor.execute("""
        CREATE TRIGGER trg_vote_insert
        AFTER INSERT ON Vote
        FOR EACH ROW
        BEGIN
            SELECT CONCAT('Vote recorded! Voter ID=', NEW.voter_id, ', Candidate ID=', NEW.candidate_id);
        END
        """)
        print("Trigger trg_vote_insert created.")
    except Exception as e:
        print(f"Trigger creation skipped or already exists: {e}")

# ----------------- Main ----------------- #
def main():
    conn = create_connection()
    cursor = conn.cursor()

    # Create tables
    create_tables(cursor)
    print("Tables created successfully.")

    # Create triggers
    create_triggers(cursor)

    conn.commit()
    cursor.close()
    conn.close()
    print("Database setup complete!")

if __name__ == "__main__":
    main()
