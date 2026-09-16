

1. Encapsulation

Encapsulation keeps the product's information and actions together in one Product object, such as its name, price, and quantity. This helps keep the inventory organized and prevents important data from being changed incorrectly.

2. Abstraction

Abstraction means showing only the important parts of the program while hiding the complicated details. For example, a sellProduct() method can reduce the stock automatically without the user needing to know how it works.

3. Inheritance

Inheritance allows different types of products to get common properties and methods from a main Product class. For example, FoodProduct and DrinkProduct can inherit the product name, price, and quantity, which helps avoid repeating the same code.

4. Polymorphism

Polymorphism allows different types of products to use the same method but perform it in their own way. For example, FoodProduct and DrinkProduct can both use displayInfo() while showing information specific to each product.