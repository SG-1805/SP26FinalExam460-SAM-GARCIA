# The Torchbearer

**Student Name:** Samuel Garcia
**Student ID:** 130737019
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis


- **Why a single shortest-path run from S is not enough:**
 A single Dijkstras run from S only tells the cheapest cost from the entrance to each location. It cannot decide which relic should be visited first, second, or any order.

- **What decision remains after all inter-location costs are known:**
 After the cheapest travel costs are known, the remaining descision is the order in which to visit the relic chambers before going to the exit.

- **Why this requires a search over orders (one sentence):**
This problem requires a search over orders because different relic visit orders can produce different total fuel costs even when all shortests path distances are already known.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection


| Source Node Type | Why it is a source |
|---|---|
| Entrance/spawn node | This is nessecary to compute the cheapest cost from the starting locationto each relic  |
| Relic chamber nodes | this is needed to compute the cheapest costs from each relic to the remaining relics and to the exit |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | Nested dictionary/ dictionary of dictionaries |
| What the keys represent |Outer keys are the source node; the inner keys are destination nodes |
| What the values represent |Shortest path fuel costs from the source node to the destination node |
| Lookup time complexity |O(1) (on average) |
| Why O(1) lookup is possible |python dictionaries use hash table lookup for keys |

### Part 2c: Precomputation Complexity


- **Number of Dijkstra runs:**  k+1
- **Cost per run:** O(m log n)
- **Total complexity:** O((k+1)m log n)
- **Justification (one line):** Dijkstras runs once from the entrance and once from each k relic

---

## Part 3: Algorithm Correctness


### Part 3a: What the Invariant Means


- **For nodes already finalized (in S):**
  Once a node is finalized, its distance is guarranteed to be the true shortest path from the source becuase Djikstras always selects the smallest available distance first.

- **For nodes not yet finalized (not in S):**
  For nodes not yet finalized, their current distance represents the shortest path found so far using only nodes that have already been finalized.

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  At the start, the source node has distance 0 and all other nodes are set to infinity, so the algorithm has not made any incorrect claims.

- **Maintenance : why finalizing the min-dist node is always correct:**
  The node with the smallest current distance is finalized next, and because all edge weights are nonnegative, there cannot be a shorter path to it through an unfinalized node.

- **Termination : what the invariant guarantees when the algorithm ends:**
  When the algorithm finishes, every reachable node has its true shortest-path distance from the source.

### Part 3c: Why This Matters for the Route Planner


Correct shortest-path distances are necessary so the route planner can accurately compare different relic visit orders and choose the one with the minimum total cost.


---

## Part 4: Search Design

### Why Greedy Fails


- **The failure mode:** A greedy approach always picks the nearest next relic, but this can lead to a higher total cost overall.
- **Counter-example setup:** In the example, S can reach B with cost 1 and A with cost 2, Traveling from B to A costs 100, while travleling fromA to B only costs 1.
- **What greedy picks:** Greedy picks B first because B is the cheapest immediate relic from S.
- **What optimal picks:** The optimal route is S -> A -> B -> T with total cost 4 in the provided example.
- **Why greedy loses:** Greedy loses because choosing the cheapest next relic does not account for the future cost of reaching the remaining relics. For example route S -> B -> A -> T is very expensive since going from A to B is expensive, so the local cheapest produces a worse route.

### What the Algorithm Must Explore


- The algorithm must explore different orders of visiting the relics to determine which order gives the lowest total fuel cost.

---

## Part 5: State and Search Space

### Part 5a: State Representation


| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | node | The node where the recursive search currently is. |
| Relics already collected | relics_visited_order | list[node] | The relics collected so far, stored in the order they were visited. |
| Fuel cost so far | cost_so_far | int/float | The total fuel cost accumulated by the current partial route. |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | set, using relics_remaining |
| Operation: check if relic already collected | Time complexity: O(1) average case |
| Operation: mark a relic as collected | Time complexity: O(1) average case with remove() |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) average case with add() |
| Why this structure fits | A set supports fast membership checks and simple remove/add operations during backtracking. |

### Part 5c: Worst-Case Search Space


- **Worst-case number of orders considered:**  k!
- **Why:**  With k relics, the algorithm could have to try every possible ordering of the relic chambers.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking


- **What is tracked:** The algorithm tracks the lowest complete route cost found so far and the relic order that produced it in best.
- **When it is used:** It is checked during recursion before exploring a branch further.
- **What it allows the algorithm to skip:** It allows the algorithm to skip any partial route whose current cost is already at least as large as the best complete route found so far.

### Part 6b: Lower Bound Estimation


- **What information is available at the current state:** The algorithm knows current_loc, relics_remaining, relics_visited_order, cost_so_far, and the current best complete solution.
- **What the lower bound accounts for:** The lower bound uses the fuel already spent, cost_so_far, as the minimum possible final cost for this branch.
- **Why it never overestimates:** Because all edge weights are nonnegative, finishing the route can only add zero or more fuel, so cost_so_far is never greater than the true final cost of that branch.


### Part 6c: Pruning Correctness


- If cost_so_far is already greater than or equal to the best complete route found, then no continuation of that branch can produce a better solution. This pruning is safe because nonnegative edge weights mean the cost cannot decrease later in the route
---

## References

> Bullet list. If none beyond lecture notes, write that.

- lecture notes +slides +python documentation
