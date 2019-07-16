'''Amazon Fresh

Amazon Fresh is a grocery delivery service that offers consumers the option of purchasing their groceries online and schedule future deliveries of purchased groceries. Amazon's backend system dynamically tracks each Amazon Fresh delivery truck and automatically assigns the next deliveries in a truck's plan. To accomplish this, the system generates an optimized delivery plan with X destinations. The most optimized plan would deliver to the closest X destinations from the start among all of the possible destinations in the plan.

Given an array of N possible delivery destinations, implement an algorithm to create the delivery plan for the closest X destinations.

Input
The input to the function/method consists of three arguments:
numDestinations, an integer representing the total number of possible delivery destinations for the truck (N);
allLocations, a list where each element consists of a pair of integers representing the x and y coordinates of the delivery locations; from aonecode.com
numDeliveries, an integer representing the number of deliveries that will be delivered in the plan (X).

Output from aonecode.com
Return a list of elements where each element of the list represents the x and y integer coordinates of the delivery destinations.from aonecode.com

Constraints
numDeliveries <= numDestinations from aonecode.com

Note
The plan starts from the truck's location [0, 01. The distance of the truck from a delivery destination (x, y) is the square root of x^2 + y^2. If there are ties then return any of the locations as long as you satisfy returning X deliveries.from aonecode.com

Example
Input:
numDestinations = 3 from aonecode.com
allocations = [[1, 2], [3, 4], [1, -1]]
numDeliveries = 2 from aonecode.com

Output:
[[1, -1], [1, 2]] from aonecode.com

Explanation:
The distance of the truck from location [1, 2] is square root(5) = 2.236 from aonecode.com
The distance of the truck from location [3, 4] is square root(25) = 5
The distance of the truck from location [1, -1] is square root(2) = 1.414 from aonecode.com
numDeliveries is 2, hence the output is [1, -1] and [1, 2].


TestCase 1
Statue: Correctfrom aonecode.com
Expected: 1 2 from aonecode.com
Returned: 1 2

Testcane 2
Status: Correct
Expected: 2 4 3 6 5 3 from aonecode.com
Returned: 2 4 3 6 5 3 
'''

import numpy as np
import operator
d,c={} ,{}
l =[]

def deliver( no_desc,  alllocation,  no_delivery):
    for i in alllocation:
        c[distance(i[0],i[1])] = i
    d=sorted(c.items(),key=operator.itemgetter(0))
    for i in range(no_delivery):
       l.append(d[i][1])
    print(l)

    
def distance( a , b):
    return(np.sqrt(a**2+b**2))

no_desc = int(input("enter the no. of destination "))
no_delivery=int(input("enter the no. of delivery"))
print("enter the location coordinate",end='\n')
alllocation =[]
for i in range(no_desc):
    location =  [int(x) for x in input().split()]
    alllocation.append(location)
    
deliver( no_desc, alllocation , no_delivery)

