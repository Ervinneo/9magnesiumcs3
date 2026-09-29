class GovernmentOfficial:
    def __init__(self, name, position, department, yearsInService):
        self.name = name
        self.position = position
        self.department = department
        self.__yearsInService = yearsInService

    def displayProfile(self):
        print("Name:", self.name)
        print("Position:", self.position)
        print("Department:", self.department)
        print("Years in Service:", self.__yearsInService)

    def performDuty(self):
        print(self.name, "is performing their duties as", self.position + ".")

    def updateYearsInService(self, years):
        if years >= 0:
            self.__yearsInService = years
            print("Years in service successfully updated.")
        else:
            print("Years in service cannot be negative.")


# Create two GovernmentOfficial objects
official1 = GovernmentOfficial(
    "Maria Santos",
    "Mayor",
    "Local Government",
    5
)

official2 = GovernmentOfficial(
    "Juan Reyes",
    "Governor",
    "Provincial Government",
    8
)

# Initial states
print("--- BEFORE ---")

print("\nObject 1:")
official1.displayProfile()

print("\nObject 2:")
official2.displayProfile()

# Change only Object 1
print("\nUpdating Object 1...")
official1.updateYearsInService(6)

# Demonstrate a method
official1.performDuty()

# Updated states
print("\n--- AFTER ---")

print("\nObject 1:")
official1.displayProfile()

print("\nObject 2:")
official2.displayProfile()