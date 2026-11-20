units = int(input("Enter electricity units: "))
ration_card = input("Do you have a ration card? (yes/no): ").strip().lower()
age = int(input("Enter age of family member: "))

if units <= 100:
    print("Full Subsidy")
elif 101 <= units <= 200 and ration_card == "yes":
    print("Partial Subsidy")
elif units > 200 and age > 80:
    print("Eligible for Special Subsidy")
else:
    print("No Subsidy")
