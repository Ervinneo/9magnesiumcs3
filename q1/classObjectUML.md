
# SG4 - Understanding Classes and Objects
## Class Name
Government Official

## Class Description
A GovernmentOfficial is a person who holds or has a position in the government and performs duties for the public.

## Properties
| Property | Data Type | Description |
|Property|Data Type|Description|
|Name |String |Name of the government official |
|Position |String |Official position |
|Department |String |Government department  |
|YearsInService |Int |Years they served in the government |

## Methods
| Method | Description |
|DisplayProfile()|Displays the official's Info|
|PerformDuty() |Represents the official's carrying out their responsibilities |

|updateYearsInService(years: int) |Updates the number of years the official has served. |
| | |

## Class Diagram

+------------------------------------------------+
|             GovernmentOfficial                |
+------------------------------------------------+
| name : string                                  |
| position : string                              |
| department : string                            |
| yearsInService : int                           |
+------------------------------------------------+
| displayProfile()                               |
| performDuty()                                  |
| updateYearsInService(years : int)              |
+------------------------------------------------+
## Design Explanation
### Why did you choose this class?
I chose this class because government officials play an important role in managing public services and helping communities.
### Which property is the most important? Why?
I think position is the most important because it tells us the official's role and responsibilities in the government.
### Which method is the most useful? Why?
I think displayProfile() is the most useful because it allows people to quickly view important information about a government official.
