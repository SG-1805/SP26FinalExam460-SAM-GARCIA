# Development Log – The Torchbearer

**Student Name:** ___________________________
**Student ID:** ___________________________

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [May12]: Initial Plan

There will be two phases, frist I will run a Djikstra algorithm from the entrace and each relic to compute the shortest distances betwween all the important locations. Second I will put in a recursive backtracking search to attemps all possible orders of visitng relics and compute the total cost using the precomtuted distances. I belive that the search and logic can be a little tricky, but I believe it to be doable.
---

## Entry 2 – [May12]: Done with part 1 and 2! (kind of)
I finished part 1 by simply copy pasting the stuff i had set up in my read me and returning it (as instructed haha). I also finished part 2, although during part two i had a small bug(more like bad optimization?) that I ran into where I made the exit node a Dijsktras sources as well. oppsie. fFter giving this minimual thought i realized this was unecessary (i know should have realized thsat before), since the torchbeaer ends at the exit and and will therefore never need any distances starting from it (duh). Adding this avoids an extra Djisktra run and mathes the desired complexity of k+1 runs. I tested everything with a test_part2() that I wrote for the functions. i left it there it is directly underneath the run tests if you want to see it. 

## Entry 3 – [May13]: Parts 3,4, and 5! (busy day haha)

I finished the written correctness and search-design sections for Parts 3 and 4. Part 3 was mostly about understanding why Dijkstra’s algorithm works, especially the role of nonnegative edge weights and why finalizing the smallest-distance node is always safe. Part 4 focused on why a greedy strategy fails for this problem, since choosing the nearest next relic does not always produce the cheapest total route.

I used the example from the assignment to help explain the greedy failure case and to better understand why the algorithm needs to explore different relic visit orders instead of making local decisions.
I implemented the recursive search for Part 5 using backtracking. The search state tracks the current location, the remaining relics, the order of relics already visited, and the current fuel cost. The recursion works by choosing a remaining relic, exploring that route, and then undoing the choice during backtracking so the algorithm can try other possible orders.

One issue I ran into was accidentally modifying the same collection of relics across recursive calls without restoring it correctly afterward. This caused missing relics and incorrect search paths until I added the proper backtracking step with remove/add and append/pop operations. After fixing that, the recursive exploration started producing the expected route orders. I have not implemented any pruning logic yet. I am tired right now and ive been working on this for too long today. I will do that tommorow. 

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | .5 to 1 hour |
| Part 2: Precomputation Design | 1 to 2 hours|
| Part 3: Algorithm Correctness | .5 to 1 hour|
| Part 4: Search Design | .5 to 1 hour|
| Part 5: State and Search Space |4 - 5 hours |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
