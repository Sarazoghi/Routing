# Routing
It Is A Project To Find Best Route To Deliver Food To The Customers With BFS (Breadth First Search),DFS (Depth First Search),IDS (Iterative Deepening Search),UCS (Uniform Cost Search), A^* And Best First Search Algorithms



The description of the problem is as follows: 

Ali recently started working in a restaurant as a courier.
His task is to pick up some food from the restaurant (origin) and go to all the destinations he is told once to deliver the food to the customer.
Unfortunately, the municipality has closed some of the city's streets, and Ali cannot cross the barriers.
Yab Restaurant, where Ali works, has signed a contract with some of the cafes in the city to give the couriers of this restaurant free of charge. As a result, Ali can go to these stores during his journey and consume the free item of that cafe to get energy.



The goal of the problem: find a transmission so that Ali can start moving with the most energy possible and visit all the customers at once. (Numerical energy is between negative infinity and positive infinity).



# Limitations of the problem:


Ali can do only four actions:

Move up by one unit: U

Moving down by one unit: D

Move left by one unit: L

Move right by one unit: R


Ali cannot go out of the given range.
Ali can see all the streets and the energy that the use of that street takes from him.

# INPUT : 
Input instance :
6 10
1R 1 1 5 5 4 2C 1 15 1B
1 1 5 3 5 5 4 5 X X
5 1I 1 6 2 2 2 1 1 1T
X X 1 6 5 5 2 1 1 X
X X 1 X X 50 2 1C 1 X
1 1 1 2 2 2T 2 1 1 1

* The first and last cells affect the causal energy.
R -> Restaurant
C -> Coffee | Energy = 10
B -> Biscuit | Energy = 5
I -> Ice Cream | Energy = 12
T -> Goals

* The number written in each house is the cost of using that street (cell). By that number, the causal energy is reduced.
* As it is clear, consuming food on the way is not mandatory, but visiting all Targets is mandatory.
# PHASE ONE 
Implementation of the successor function

# PHASE TWO
1. BFS (Breadth First Search)
2. DFS (Depth First Search)
3. IDS (Iterative Deepening Search)
4. UCS (Uniform Cost Search)

# PHASE THREE
the Heuristic function should be implemented first, and then the following algorithms should be implemented:

5. A^*
6. Best First Search
