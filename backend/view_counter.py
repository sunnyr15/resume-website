import mysql.connector 

# Database connection configuration
config = {
    'user': 'root',
    'password': 'sunny001',  # Replace with your MySQL password
    'host': 'localhost',      # Change to your RDS endpoint if needed
    'database': 'view_counter_db',
}

# Connect to the MySQL database
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Database connection successful.")

    # Check if there is an entry in the view_counter table
    cursor.execute("SELECT count FROM view_counter WHERE id = 1")
    result = cursor.fetchone()
    
    if result:
        # Increment the count if entry exists
        new_count = result[0] + 1
        cursor.execute("UPDATE view_counter SET count = %s WHERE id = 1", (new_count,))
        print(f"Updated view count to {new_count}.")
    else:
        # Create an entry if it doesn't exist
        cursor.execute("INSERT INTO view_counter (id, count) VALUES (1, 1)")
        print("Initialized view count to 1.")

    # Commit the transaction
    conn.commit()

    # Fetch and display the updated count
    cursor.execute("SELECT count FROM view_counter WHERE id = 1")
    updated_count = cursor.fetchone()[0]
    print(f"Current view count: {updated_count}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
