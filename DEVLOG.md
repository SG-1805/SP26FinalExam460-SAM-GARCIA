# Development Log – The Torchbearer

**Student Name:** Samuel Garcia
**Student ID:** 130737019

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
## Entry 4 – [May14]: parts 5 and 6!
So today is the day I realized that I needed to actually do git commits every time i worked on this project. oops. well i hope that my devlogs are enough but anyway I did the pruning and the pipeline implementation today both of which took an embrassing amount of time to implement. It was not very many lines of code however I kept runnong into issues that kept crashing python however most of themwere silly typos(like forgetting nodes), indentation issues, or snytactical problems. However it is complete and passes all the provided tests. I have one more thing i would like to adress but that will be in the next devlog. 

## Entry 5 – [Date]: Post-Implementation Reflection + p7

Last entry so I decided to make some additional edge case test cases since I saw on the document that there would be other test cases. Just testing some edge cases to see if my proggram could handle them. It could not. Out of the 5 edge test cases written my program failed three of them. This is when I came to the realization that my code was kind of crummy. So before submitting a final version I of course have to make a little more robust. So scanning my code for the problem it eas actually quite a simple fix. The test cases that failed where the case where the route included the exit node, the case where the recursive search involved modifying the same set of remaining relics while iterating through it, and the case where there were no relics. After trying a few solutions my problem was that I has the line of code: best[1] = relics_visited_order + [exit_node], which bassically returned the relic order plus T, but i dont want that I want the order toi include only relics not the exit, I rewalced that line with best[1] = relics_visited_order.copy(). I also realized i forgot to do the readme for the last one so i just went ahead and did those. After finishing the implementation, the main thing I would improve with more time would be the pruning and optimization logic. Right now the recursive search works correctly, but in the worst case it still explores many unnecessary branches before finding the best route. I would like to implement a stronger lower bound estimate so the algorithm could eliminate bad paths earlier and run more efficiently on larger graphs. I would also improve the testing setup by adding more randomized and edge case heavy graphs. Some of the most useful bugs I found came from unusual recursive cases, especially involving backtracking and modifying collections during recursion. Finsihed by reviewing the document making changes to part 4, getting rid of some typos that I found, and making some final tweaks to the code.
---

## Final Entry – [May14]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | .5 to 1 hour |
| Part 2: Precomputation Design | 1 to 2 hours|
| Part 3: Algorithm Correctness | .5 to 1 hour|
| Part 4: Search Design | .5 to 1 hour|
| Part 5: State and Search Space |4 - 5 hours |
| Part 6: Pruning |1 hour |
| Part 7: Implementation |2-3 hours (including new tests) |
| README and DEVLOG writing |3-3.5 hours|
| **Total** |12.5 - 16.5 hours give or take|
