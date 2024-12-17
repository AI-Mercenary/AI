# Table-Driven Agent for Room Cleaning
def table_driven_agent():
    # Predefined table mapping states to actions
    table = {
        ('dirty', 'dirty', 'dirty', 'dirty'): ('clean', 'A'),
        ('clean', 'dirty', 'dirty', 'dirty'): ('clean', 'B'),
        ('clean', 'clean', 'dirty', 'dirty'): ('clean', 'C'),
        ('clean', 'clean', 'clean', 'dirty'): ('clean', 'D'),
        ('clean', 'clean', 'clean', 'clean'): ('done', None),
    }
    
    # Mapping room labels to indices
    room_indices = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    
    # Initial state: All rooms are dirty
    state = ['dirty', 'dirty', 'dirty', 'dirty']
    print("Initial State:", state)
    
    # Main loop for agent operation
    while True:
        # Fetch the current action based on the state from the table
        action, room = table[tuple(state)]
        
        # Check if cleaning is complete
        if action == 'done':
            print("\nAll rooms are clean! Final State:", state)
            break
        
        # Perform the cleaning action
        print(f"Action: {action} room {room}")
        state[room_indices[room]] = 'clean'  # Update the state to 'clean'
        print("Updated State:", state)


# Run the Table-Driven Agent
if __name__ == "__main__":
    print("=== Table-Driven Agent ===\n")
    table_driven_agent()
