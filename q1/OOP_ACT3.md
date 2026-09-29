1. Identify your original class.
GovernmentOfficial
2. What does it represent?
Shows the Government official with a name, position , department , and years in service . 
3. Which existing attributes and methods will still be useful when it interacts with another class?
The attributes store official information, while the methods display, manage, and update it.

1. New class name?  
Department
2. Description
Shows a government department that manages multiple government officials
3. Why should these two classes be connected?
A department contains and manages multiple government officials. Each government official is assigned to one department, allowing the department to access their information through their objects.


1. Multiplicity
1 : 0
2. Explain why this multiplicity fits your system in 2-3 sentences
One department can have zero or more government officials assigned to it. This relationship is appropriate because a department can manage multiple officials rather than being limited to only one.















Answer each question in 3 - 4 sentences using your own words.
1. What is the association between your two classes? Explain the relationship using your actual system.
2. What multiplicity did you choose, and why? Explain why 1:1, 1:0..*, or another multiplicity is
appropriate.
3. How did you implement the relationship in Python? Identify which attribute stores the related object
or objects.
4. Why did you store an object reference instead of copying its data? Use one example from your
implementation.
5. If your relationship uses “many,” why is a list appropriate? Explain what the list actually contains.