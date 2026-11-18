class Patient:
    def __init__(self, name, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount
# method get 
    def get_name(self):
        return self.__name
#method set nem
    def set_name(self, name):
        self.__name = name
#method get
    def get_bill_amount(self):
        return self.__bill_amount
#method set bil
    def set_bill_amount(self, bill_amount: float):
        self.__bill_amount = bill_amount
#method calc bil
    def calculate_bill(self):
        return self.__bill_amount
#method show type
    def display_patient_type(self):
        return "regular Patient"

#clas of cenior
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        return "senior Citizen"

#clas of Philhealth
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

    def display_patient_type(self):
        return "philHealth Member"


patients = [Patient("Juan Dela Cruz", 15000.00),SeniorPatient("Maria Santos", 15000.00),PhilHealthPatient("Pedro Reyes", 15000.00)]

print("Hospital Billing System")

for patient in patients:
    print(f"Patient Name:  {patient.get_name()}")
    print(f"Patient Type: {patient.display_patient_type()}")
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}\n")