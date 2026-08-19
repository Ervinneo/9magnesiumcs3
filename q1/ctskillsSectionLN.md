# CT Skills Section

Add your content here about your CT skills.
Computational Thinking Exercise: Smart School Canteen Queue

Section: 9 - Magnesium
Name: Ervin Neonel Cordero
Date: 8/19/26

Annex A — Smart School Canteen Queue

Step 1: Identify the Big Problem

Main Problem:
The school canteen queue is slow and crowded because ordering, payment, and monitoring of food supplies are done manually.

Step 2: Identify Three to Four Sub-Problems

Students take too long to decide what to order.
A system could display available food items and their prices clearly so students can decide before reaching the cashier.

The cashier manually calculates the total and change.
A program could automatically calculate the total cost and the customer's change after payment is entered.

There is no system for tracking food inventory.
A system could decrease the available quantity whenever an item is purchased and notify staff when stock is low or empty.

The ordering process creates a long queue.
The system could organize orders and make payment faster so students spend less time at the cashier.

Step 3: Define Computational Thinking Approaches

Sub-Problem

CT Skill

Example Solution

Students take too long to decide what to order.

Abstraction

Show important information such as food name, price, and availability.

Cashier manually calculates totals and change.

Algorithm Design

Input selected items and payment, calculate the total, then calculate and display the change.

No system tracks food inventory.

Pattern Recognition

Track each item's quantity and recognize when stock reaches a low or zero level.

Ordering creates a long queue.

Decomposition

Separate ordering, payment, and inventory tasks so each part can be handled independently.

Step 4: Algorithmic Solution

Selected Sub-Problem: Automatically calculate the total cost and change.

Pseudocode

START

Display available food items and prices

Ask the student to select an item
Ask for the quantity

subtotal = item price × quantity

Ask for the amount of money given

IF money given < subtotal THEN
    Display "Insufficient payment"
ELSE
    change = money given - subtotal
    Display the total amount
    Display the change
END IF

END

Explanation

The algorithm makes the payment process faster by automatically calculating the total and change. It also checks if the student has given enough money before completing the transaction.

Reflection

Decomposing the canteen problem makes it easier to solve because the large problem can be divided into smaller tasks such as ordering, payment, inventory, and queue management. The CT skills used include decomposition, abstraction, pattern recognition, and algorithm design. These skills help make the canteen system more organized, efficient, and easier to develop.