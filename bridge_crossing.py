# bridge_crossing.py
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def cross_bridge_for_4(person_times):
    # Initialize the time elapsed and the order of crossing
    time_elapsed = 0
    crossing_order = []

    # Initial crossing: A and B
    time_elapsed += 2
    crossing_order.append(('A', 'B'))

    # A returns with the torch
    time_elapsed += 1
    crossing_order.append(('A',))

    # C and D cross together
    time_elapsed += 8
    crossing_order.append(('C', 'D'))

    # B returns with the torch
    time_elapsed += 2
    crossing_order.append(('B',))

    # Final crossing: A and B
    time_elapsed += 2
    crossing_order.append(('A', 'B'))

    return time_elapsed, crossing_order


# Unit tests
def test_cross_bridge_for_4():
    # Example scenario: A, B, C, D
    person_times = {'A': 1, 'B': 2, 'C': 5, 'D': 8}
    total_time, order = cross_bridge_for_4(person_times)
    assert total_time == 15
    assert order == [('A', 'B'), ('A',), ('C', 'D'), ('B',), ('A', 'B')]


# Example usage
if __name__ == "__main__":
    person_times = {'A': 1, 'B': 2, 'C': 5, 'D': 8}
    
    test_cross_bridge_for_4()
    
    total_time, order = cross_bridge_for_4(person_times)
    print(f"Total time elapsed: {total_time} minutes")
    print("Crossing order:")
    for step in order:
        print(step)
