"""
An Algorithm for the Proportional Division of Indivisible Items
May 24
Authors:
Steven J. Brams - Department of Politics
D. Marc Kilgour - Department of Mathematics
Christian Klamler - Institute of Public Economics
https://mpra.ub.uni-muenchen.de/56587/1/MPRA_paper_56585.pdf
--------------------------------------------------------------------
Student Details:
Nadav Suissa - 312321631
20/5/24
"""
import pytest
import fairpy
from fairpy.items.propm_allocation import *


# Set up logging for fairpy's propm_allocation function
import logging

propm_allocation.logger.addHandler(logging.StreamHandler())
propm_allocation.logger.setLevel(logging.INFO)


def find_proportional_allocation(instance):
    """
    Finds a proportional allocation of items among players based on their rankings.

    Args:
        instance (dict): Dictionary containing 'agents', 'items', and 'rankings'.

    Returns:
        dict: Allocation of items among players.

    >>> instance = {
    ...     "agents": ["Alice", "Bob", "Charlie"],
    ...     "items": {
    ...         "Alice": {"A": 40, "B": 35, "C": 25},
    ...         "Bob": {"A": 35, "B": 40, "C": 25},
    ...         "Charlie": {"A": 40, "B": 25, "C": 35}
    ...     },
    ...     "rankings": {
    ...         "Alice": [["A"], ["B"], ["C"]],
    ...         "Bob": [["B"], ["A"], ["C"]],
    ...         "Charlie": [["A"], ["C"], ["B"]]
    ...     }
    ... }
    >>> find_proportional_allocation(instance)
    {'Alice': ['A'], 'Bob': ['B'], 'Charlie': ['C']}
    """
    pass


def bundle_is_minimal(instance):
    """
    Checks if each bundle for each player is minimal within the given instance.

    Args:
        instance (dict): Dictionary containing 'agents', 'items', and 'rankings'.

    Returns:
        dict: A dictionary indicating if each bundle for each player is minimal.

    >>> instance = {
    ...     "agents": ["Alice", "Bob", "Charlie"],
    ...     "items": {
    ...         "Alice": {"A": 40, "B": 35, "C": 25},
    ...         "Bob": {"A": 35, "B": 40, "C": 25},
    ...         "Charlie": {"A": 40, "B": 25, "C": 35}
    ...     },
    ...     "rankings": {
    ...         "Alice": [["A"], ["B"], ["C"]],
    ...         "Bob": [["A"], ["B"], ["C"]],
    ...         "Charlie": [["A"], ["B"], ["C"]]
    ...     }
    ... }
    >>> bundle_is_minimal(instance)
    {'Alice': {'A': True, 'B': True, 'C': True}, 'Bob': {'A': True, 'B': True, 'C': True}, 'Charlie': {'A': True, 'B': True, 'C': True}}
    """
    pass


def allocate_minimal_bundles(instance):
    """
    Allocates minimal bundles to players.

    Args:
        instance (dict): Dictionary containing 'agents', 'minimal_bundles', and 'items'.

    Returns:
        dict: Allocation of items among players.

    >>> instance = {
    ...     "agents": ["Alice", "Bob", "Charlie"],
    ...     "minimal_bundles": {
    ...         "Alice": [["A"], ["B"]],
    ...         "Bob": [["B"], ["A"]],
    ...         "Charlie": [["A"], ["C"]]
    ...     },
    ...     "items": {
    ...         "Alice": {"A": 40, "B": 35, "C": 25},
    ...         "Bob": {"A": 35, "B": 40, "C": 25},
    ...         "Charlie": {"A": 40, "B": 25, "C": 35}
    ...     }
    ... }
    >>> allocate_minimal_bundles(instance)
    {'Alice': ['A'], 'Bob': ['B'], 'Charlie': ['C']}
    """
    pass


def total_value(instance):
    """
    Calculates the total value of a bundle for a player.

    Args:
        instance (dict): Dictionary containing 'bundle', 'player', and 'items'.

    Returns:
        int: Total value of the bundle for the player.

    >>> instance = {
    ...     "bundle": ["A", "B"],
    ...     "player": "Alice",
    ...     "items": {
    ...         "Alice": {"A": 40, "B": 35, "C": 25},
    ...         "Bob": {"A": 35, "B": 40, "C": 25},
    ...         "Charlie": {"A": 40, "B": 25, "C": 35}
    ...     }
    ... }
    >>> total_value(instance)
    75
    """
    pass


def is_envy_free(instance):
    """
    Checks if the allocation is envy-free.

    Args:
        instance (dict): Dictionary containing 'allocation', 'agents', and 'items'.

    Returns:
        bool: True if the allocation is envy-free, False otherwise.

    >>> instance = {
    ...     "allocation": {"Alice": ["A"], "Bob": ["B"], "Charlie": ["C"]},
    ...     "agents": ["Alice", "Bob", "Charlie"],
    ...     "items": {
    ...         "Alice": {"A": 40, "B": 35, "C": 25},
    ...         "Bob": {"A": 35, "B": 40, "C": 25},
    ...         "Charlie": {"A": 40, "B": 25, "C": 35}
    ...     }
    ... }
    >>> is_envy_free(instance)
    True

    >>> instance = {
    ...     "allocation": {"Alice": ["A"], "Bob": ["B"], "Charlie": ["B"]},
    ...     "agents": ["Alice", "Bob", "Charlie"],
    ...     "items": {
    ...         "Alice": {"A": 40, "B": 35, "C": 25},
    ...         "Bob": {"A": 35, "B": 40, "C": 25},
    ...         "Charlie": {"A": 40, "B": 25, "C": 35}
    ...     }
    ... }
    >>> is_envy_free(instance)
    False
    """
    pass


def is_pareto_optimal(instance):
    """
    Checks if the allocation is Pareto-optimal.

    Args:
        instance (dict): Dictionary containing 'allocation', 'agents', and 'items'.

    Returns:
        bool: True if the allocation is Pareto-optimal, False otherwise.

    >>> instance = {
    ...     "allocation": {"Alice": ["A"], "Bob": ["B"], "Charlie": ["C"]},
    ...     "agents": ["Alice", "Bob", "Charlie"],
    ...     "items": {
    ...         "Alice": {"A": 40, "B": 35, "C": 25},
    ...         "Bob": {"A": 35, "B": 40, "C": 25},
    ...         "Charlie": {"A": 40, "B": 25, "C": 35}
    ...     }
    ... }
    >>> is_pareto_optimal(instance)
    True

    >>> instance = {
    ...     "allocation": {"Alice": ["A"], "Bob": ["B"], "Charlie": ["A"]},
    ...     "agents": ["Alice", "Bob", "Charlie"],
    ...     "items": {
    ...         "Alice": {"A": 40, "B": 35, "C": 25},
    ...         "Bob": {"A": 35, "B": 40, "C": 25},
    ...         "Charlie": {"A": 40, "B": 25, "C": 35}
    ...     }
    ... }
    >>> is_pareto_optimal(instance)
    False
    """
    pass


@pytest.fixture
def instance_edge_cases():
    return [
        # Empty input
        {'agents': ['agent0', 'agent1'], 'items': {'agent0': {}, 'agent1': {}},
         'rankings': {'agent0': [], 'agent1': []}},
        # Invalid input
        {'agents': ['agent0', 'agent1'],
         'items': {'agent0': {'x0': 'invalid', 'x1': 100.0}, 'agent1': {'x0': 0.0, 'x1': 100.0}},
         'rankings': {'agent0': [['x0'], ['x1']], 'agent1': [['x0'], ['x1']]}}
    ]


def meets_conditions(allocation):
    # Implement your condition-checking logic here
    return True


def test_edge_cases(instance_edge_cases):
    for instance in instance_edge_cases:
        your_allocation = find_proportional_allocation(instance)
        fairpy_allocation = fairpy.divide(propm_allocation, instance)
        assert your_allocation == fairpy_allocation


def test_large_input():
    instance_large = fairpy.items.propm_allocation.generate_instance(num_agents=2, num_items=5,
                                                                     value_range=(1000, 5000))
    your_allocation_large = find_proportional_allocation(instance_large)
    fairpy_allocation_large = fairpy.divide(propm_allocation, instance_large)
    assert your_allocation_large == fairpy_allocation_large


def test_random_large_input():
    instance_random_large = fairpy.items.propm_allocation.generate_instance(num_agents=3, num_items=7)
    your_allocation_random_large = find_proportional_allocation(instance_random_large)
    assert meets_conditions(your_allocation_random_large)


def test_additional_cases():
    instance_one_agent = {'agents': ['Alice'], 'items': {'Alice': {'x0': 1000, 'x1': 2000, 'x2': 3000}},
                          'rankings': {'Alice': [['x0'], ['x1'], ['x2']]}}
    your_allocation_one_agent = find_proportional_allocation(instance_one_agent)
    fairpy_allocation_one_agent = fairpy.divide(propm_allocation, instance_one_agent)
    assert your_allocation_one_agent == fairpy_allocation_one_agent

    instance_multiple_agents_one_item = {'agents': ['Alice', 'Bob', 'Charlie'],
                                         'items': {'Alice': {'x0': 1000}, 'Bob': {'x0': 2000}, 'Charlie': {'x0': 3000}},
                                         'rankings': {'Alice': [['x0']], 'Bob': [['x0']], 'Charlie': [['x0']]}}
    your_allocation_multiple_agents_one_item = find_proportional_allocation(instance_multiple_agents_one_item)
    fairpy_allocation_multiple_agents_one_item = fairpy.divide(propm_allocation, instance_multiple_agents_one_item)
    assert your_allocation_multiple_agents_one_item == fairpy_allocation_multiple_agents_one_item

    instance_multiple_agents_same_value = {'agents': ['Alice', 'Bob'], 'items': {'Alice': {'x0': 1000, 'x1': 1000},
                                                                                 'Bob': {'x0': 1000, 'x1': 1000}},
                                           'rankings': {'Alice': [['x0'], ['x1']], 'Bob': [['x0'], ['x1']]}}
    your_allocation_multiple_agents_same_value = find_proportional_allocation(instance_multiple_agents_same_value)
    fairpy_allocation_multiple_agents_same_value = fairpy.divide(propm_allocation, instance_multiple_agents_same_value)
    assert your_allocation_multiple_agents_same_value == fairpy_allocation_multiple_agents_same_value

    instance_large_agents_items = fairpy.items.propm_allocation.generate_instance(num_agents=5, num_items=10,
                                                                                  value_range=(1000, 5000))
    your_allocation_large_agents_items = find_proportional_allocation(instance_large_agents_items)
    fairpy_allocation_large_agents_items = fairpy.divide(propm_allocation, instance_large_agents_items)
    assert your_allocation_large_agents_items == fairpy_allocation_large_agents_items

    instance_random_large_agents_items = fairpy.items.propm_allocation.generate_instance(num_agents=4, num_items=8)
    your_allocation_random_large_agents_items = find_proportional_allocation(instance_random_large_agents_items)
    fairpy_allocation_random_large_agents_items = fairpy.divide(propm_allocation, instance_random_large_agents_items)
    assert your_allocation_random_large_agents_items == fairpy_allocation_random_large_agents_items


# Tests for the specific functions
def test_bundle_is_minimal():
    instance = {
        "agents": ["Alice", "Bob", "Charlie"],
        "items": {
            "Alice": {"A": 40, "B": 35, "C": 25},
            "Bob": {"A": 35, "B": 40, "C": 25},
            "Charlie": {"A": 40, "B": 25, "C": 35}
        },
        "rankings": {
            "Alice": [["A"], ["A", "B"]],
            "Bob": [["A"], ["B"]],
            "Charlie": [["A"], ["B"]]
        }
    }

    result = bundle_is_minimal(instance)
    assert result["Alice"]["A"] == True
    assert result["Alice"]["B"] == True
    assert result["Bob"]["A"] == True
    assert result["Bob"]["B"] == True
    assert result["Charlie"]["A"] == True
    assert result["Charlie"]["B"] == True




def test_allocate_minimal_bundles():
    instance = {
        "agents": ["Alice", "Bob", "Charlie"],
        "minimal_bundles": {
            "Alice": [["A"], ["B"]],
            "Bob": [["B"], ["A"]],
            "Charlie": [["A"], ["C"]]
        },
        "items": {
            "Alice": {"A": 40, "B": 35, "C": 25},
            "Bob": {"A": 35, "B": 40, "C": 25},
            "Charlie": {"A": 40, "B": 25, "C": 35}
        }
    }
    assert allocate_minimal_bundles(instance) == {'Alice': ['A'], 'Bob': ['B'], 'Charlie': ['A']}


def test_total_value():
    instance = {
        "agents": ["Alice", "Bob", "Charlie"],
        "items": {
            "Alice": {"A": 40, "B": 35, "C": 25},
            "Bob": {"A": 35, "B": 40, "C": 25},
            "Charlie": {"A": 40, "B": 25, "C": 35}
        }
    }
    assert total_value(instance) == 75


def test_is_envy_free():
    instance = {
        "allocation": {"Alice": ["A"], "Bob": ["B"], "Charlie": ["C"]},
        "agents": ["Alice", "Bob", "Charlie"],
        "items": {
            "Alice": {"A": 40, "B": 35, "C": 25},
            "Bob": {"A": 35, "B": 40, "C": 25},
            "Charlie": {"A": 40, "B": 25, "C": 35}
        }
    }
    assert is_envy_free(instance) == True

    instance["allocation"]["Charlie"] = ["B"]
    assert is_envy_free(instance) == False


def test_is_pareto_optimal():
    instance = {
        "allocation": {"Alice": ["A"], "Bob": ["B"], "Charlie": ["C"]},
        "agents": ["Alice", "Bob", "Charlie"],
        "items": {
            "Alice": {"A": 40, "B": 35, "C": 25},
            "Bob": {"A": 35, "B": 40, "C": 25},
            "Charlie": {"A": 40, "B": 25, "C": 35}
        }
    }
    assert is_pareto_optimal(instance) == True

    instance["allocation"]["Charlie"] = ["A"]
    assert is_pareto_optimal(instance) == False


if __name__ == "__main__":
    pytest.main()
