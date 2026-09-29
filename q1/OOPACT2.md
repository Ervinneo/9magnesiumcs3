


## Visibility Decisions

# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
No major changes were needed from my original design. 

## Visibility Decisions


| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
|Name |String  |Public(+) |Identify the official |
|Position |String |Public(+) |Identify the official's postion |
|Department |String |Public(+) |Identify the official's department |
|Yearsinservice |Integer |Private (-) |should be protected from invalid direct modifications |

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

![Class Diagram](images/classDiagramSG5.png)

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