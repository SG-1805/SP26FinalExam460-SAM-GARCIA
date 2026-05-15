"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Samuel Garcia
Student ID:  130737019

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
   return """ ##Part 1: Problem Analysis
- **Why a single shortest-path run from S is not enough:**
    A single Dujkstras run from S only tells the cheatpest cost from the entrance to each location. It cannot decide which relic should be visited first, second, or any order.

    - **What decision remains after all inter-location costs are known:**
    Adtewr the cheqatpest travel costs are known, the remaining descision is the roder in which to vists the relic chambers before going to the exit.

    - **Why this requires a search over orders (one sentence):**
    This problem requires a search over orders becuase different relic visit orders can produce different total fuel costs even when all shrotests path distances are already known.
    """


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    return [spawn] + relics


def run_dijkstra(graph, source):
    dist = {node: float('inf')for node in graph}
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    sources  = select_sources(spawn, relics, exit_node)
    dist_table = {}
    for s in sources:
        dist_table[s] = run_dijkstra(graph, s)
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    return """
    - **For nodes already finalized (in S):**
    Once a node is finalized, its distance is guarranteed to be the true shortest path from the source becuase Djikstras always selects the smallest available distance first.

    - **For nodes not yet finalized (not in S):**
    For nodes not yet finalized, their current distance represents the shortest path found so far using only nodes that have already been finalized.
    
    - **Initialization : why the invariant holds before iteration 1:**
    At the start, the source node has distance 0 and all other nodes are set to infinity, so the algorithm has not made any incorrect claims.

    - **Maintenance : why finalizing the min-dist node is always correct:**
    The node with the smallest current distance is finalized next, and because all edge weights are nonnegative, there cannot be a shorter path to it through an unfinalized node.

    - **Termination : what the invariant guarantees when the algorithm ends:**
    When the algorithm finishes, every reachable node has its true shortest-path distance from the source.

    - **Why This Matters for the Route Planner:**
    Correct shortest-path distances are necessary so the route planner can accurately compare different relic visit orders and choose the one with the minimum total cost.
    """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    return """
    - **The failure mode:** A greedy approach always picks the nearest next relic, but this can lead to a higher total cost overall.
    - **Counter-example setup:** In the example, S can reach B with cost 1 and A with cost 2, Traveling from B to A costs 100, while travleling fromA to B only costs 1.
    - **What greedy picks:** Greedy picks B first because B is the cheapest immediate relic from S.
    - **What optimal picks:** The optimal route is S -> A -> B -> T with total cost 4 in the provided example.
    - **Why greedy loses:** Greedy loses because choosing the cheapest next relic does not account for the future cost of reaching the remaining relics. For example route S -> B -> A -> T is very expensive since going from A to B is expensive, so the local cheapest produces a worse route.
    - ** What the Algorithm Must Explore:** The algorithm must explore different orders of visiting the relics to determine which order gives the lowest total fuel cost.
    """


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    best = [float('inf'), []]

    current_loc = spawn
    relics_remaining = set(relics)
    relics_visited_order = []
    cost_so_far = 0
    _explore(dist_table, current_loc, relics_remaining, relics_visited_order, cost_so_far, exit_node, best)
    return best[0], best[1]


def _explore( dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    # Safe to prune since nonnegative edge weights mean this path can only get more expensive.
    if cost_so_far >= best[0]:
        return
    if not relics_remaining:
        exit_cost = dist_table[current_loc][exit_node]
        total_cost = cost_so_far + exit_cost
        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = relics_visited_order.copy()
        return
    
    for relic in list(relics_remaining):
        travel_cost = dist_table[current_loc][relic]
        if travel_cost == float('inf'):
            continue
        relics_remaining.remove(relic)
        relics_visited_order.append(relic)
        _explore(dist_table, relic, relics_remaining, relics_visited_order, cost_so_far + travel_cost, exit_node, best)
        relics_remaining.add(relic)
        relics_visited_order.pop()

# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    dist_table = precompute_distances (graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")

def _test_part2():
    graph = {
        'S': [('A', 2), ('B', 5)],
        'A': [('B', 1)],
        'B': [('T', 3)],
        'T': []
    }

    print(select_sources('S', ['A', 'B'], 'T'))
    print(run_dijkstra(graph, 'S'))
    print(precompute_distances(graph, 'S', ['A', 'B'], 'T'))
def _edge_cases_test():
    #edge case 1: returned route should have only relics, no exit
    graph_1 = {
        'S': [('R', 1)],
        'R': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['R'], 'T')
    if cost != 2: print(f"Edge case 1 FAILED: expected 2 got {cost}")
    elif order != ['R']:print(f"Edge Case 1 FAILED: expected ['R'], got {order}")
    else : print("Edge Case 1 passed")
    #edge case 2: Recursive exploration with multiple relics, tests mutation during iteration issues
    graph_2 = {
        'S': [('A', 1), ('B', 1), ('C', 1)],
        'A': [('B', 1), ('C', 1), ('T', 10)],
        'B': [('A', 1), ('C', 1), ('T', 10)],
        'C': [('A', 1), ('B', 1), ('T', 1)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['A', 'B', 'C'], 'T')
    if cost != 4: print(f"Edge case 2 FAILED: expected 4 got {cost}")
    elif set(order) != {'A', 'B', 'C'}:print(f"Edge Case 2 FAILED: incorrect relic order, got {order}")
    else : print("Edge Case 2 passed")
    #edge case 3: Relic unreachable from spawn
    graph_3= {
        'S': [('A',1)],
        'A': [('T',1)],
        'R': [('T',1)],
        'T': []
    }
    cost, order = solve(graph_3,'S', ['R'], 'T')
    if cost != float('inf'):print(f"Edge case 3 FAILED: Expected inf, got{cost}")
    elif order !=[]:print(f"Edge case 3 FAILED: Expected [], got {order}")
    else: print("Edge case 3 passed")
    #edge case 4: Greedy first choice is not optimal.
    graph_4 = {
        'S': [('A', 1), ('B', 2)],
        'A': [('B', 100), ('T', 100)],
        'B': [('A', 1), ('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['A', 'B'], 'T')
    cost_ab = 1 + 100 + 1 
    cost_ba = 2 + 1 + 100 
    expected_cost = min(cost_ab, cost_ba)
    if cost != expected_cost: print(f"Edge case 4 FAILED: Expected cost 4, got {cost}")
    elif order != ['A', 'B']: print(f"Edge case 4 FAILED: Expected ['B', 'A'], got {order}")
    else : print("Edge Case 4 passed")
    #Edge case 5: no relics: go from spawn to exit
    graph_5 = {
        'S': [('T', 7)],
        'T': []
    }
    cost, order = solve(graph_5,'S',[], 'T')
    if cost != 7: print(f"Edge case 5 FAILED: Expected cost 7, got {cost}")
    elif order != []: print(f"Edge case 5 FAILED: Expected[], got {order}")
    else :print("Edge Case 5 passed")

if __name__ == "__main__":
    _run_tests()
    _edge_cases_test()
