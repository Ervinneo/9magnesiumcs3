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


# New Related Class
class Department:
    def __init__(self, departmentName):
        self.departmentName = departmentName
        self.officials = []

    def addOfficial(self, official):
        self.officials.append(official)
        print(official.name, "has been added to", self.departmentName)

    def displayOfficials(self):
        print("\nDepartment:", self.departmentName)
        print("List of Government Officials:")

        for official in self.officials:
            print("\n--------------------")
            official.displayProfile()


# Create Department Object
department1 = Department("Local Government")

# Create Three GovernmentOfficial Objects
official1 = GovernmentOfficial(
    "Maria Santos",
    "Mayor",
    "Local Government",
    5
)

official2 = GovernmentOfficial(
    "Juan Reyes",
    "Governor",
    "Local Government",
    8
)

official3 = GovernmentOfficial(
    "Ana Cruz",
    "Councilor",
    "Local Government",
    3
)


# BEFORE RELATIONSHIP
print("--- BEFORE RELATIONSHIP ---")

print("Department:", department1.departmentName)
print("Number of officials:", len(department1.officials))

print("\nCreated Officials:")
official1.displayProfile()
print()
official2.displayProfile()
print()
official3.displayProfile()


# BUILDING RELATIONSHIP
print("\n--- BUILDING RELATIONSHIP ---")

department1.addOfficial(official1)
department1.addOfficial(official2)
department1.addOfficial(official3)


# AFTER RELATIONSHIP
print("\n--- AFTER RELATIONSHIP ---")

department1.displayOfficials()


# Demonstrate accessing related objects
print("\n--- ACCESSING DATA THROUGH RELATIONSHIP ---")

for official in department1.officials:
    print(official.name, "is a", official.position,
          "in", official.department)