# Class Attributes and Methods


## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision  
o major changes were needed from my original design.

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
|name |String |Public (+) |It can be accessed to identify the official. |
|position |String |Public (+) |It can be accessed to know the official's position. |
|department |String |Public (+) |It can be accessed to identify their department. |
|yearsInService |Integer |Private (-) |It should be protected from invalid direct modifications. |

## Updated UML Class Diagram
+------------------------------------------------+

| GovernmentOfficial |

+------------------------------------------------+

| + name : string |

| + position : string |

| + department : string |

| - yearsInService : int |

+------------------------------------------------+

| + displayProfile() |

| + performDuty() |

| + updateYearsInService(years : int) |

+------------------------------------------------+

## Python Implementation
[View Python Source](classImplementation.py)

## Test Run
![Test Run](images/classTestRun.png)

## Object Diagram
![Object Diagram](images/objectDiagram.png)

## Analysis
### Why did you make your chosen attribute private?

### Which method changes the state of your object?

### How did your two objects demonstrate that instances are independent?

### What is the difference between your class diagram and your object diagram?
