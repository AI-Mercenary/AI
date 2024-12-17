# Simple Reflex Agent for Room Cleaning
def simple_reflex_agent():
    # Initial state: All rooms are dirty
    state = {'A': 'dirty', 'B': 'dirty', 'C': 'dirty', 'D': 'dirty'}
    print("Initial State:", state)

    # Iterate through the rooms
    for room in state:
        if state[room] == 'dirty':  # Check if the room is dirty
            print(f"Cleaning room {room}")
            state[room] = 'clean'  # Clean the room
            print("Updated State:", state)

    print("\nAll rooms are clean! Final State:", state)


# Run the Simple Reflex Agent
if __name__ == "__main__":
    print("=== Simple Reflex Agent ===\n")
    simple_reflex_agent()
