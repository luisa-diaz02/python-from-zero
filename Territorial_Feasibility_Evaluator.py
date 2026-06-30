
# TERRITORIAL FEASIBILITY EVALUATOR

print(" ______________________________________________________________________")
print("|              ===== TERRITORIAL FEASIBILITY EVALUATOR =====           |")
print("| ===== WELCOME TO THE TERRITORIAL FEASIBILITY EVALUATOR PROGRAM ===== |")
print("|______________________________________________________________________|")

# Obtain client data:

cliente_name = input("Name: ").title().strip()
client_income = float(input("Monthly Income: "))
credit_history = input("Credit History (excellent: yes/no): ")
has_guarantee = input("Do you have a guarantee/co-signer? (yes/no): ")

print("\nThank you for providing your information. We will now evaluate your eligibility for the territorial feasibility evaluation based on the provided data.\n")

# Evaluate eligibility based on income, credit history, and guarantee status
if client_income > 2000 and credit_history.lower() == "yes":
    print("________________________________________________________________________")
    print(f"Client Name: {cliente_name}")
    print(f"Monthly Income: ${client_income:.2f}")
    print(f"Credit History: {credit_history} ")
    print(f"Guarantee/Co-signer: {has_guarantee}")
    print(f"{cliente_name}, APPROVED. Ready for contract signing")
    print("________________________________________________________________________")
elif client_income <= 2000 and has_guarantee.lower() == "yes":
    print("________________________________________________________________________")
    print(f"Client Name: {cliente_name}")
    print(f"Monthly Income: ${client_income:.2f} ")
    print(f"Credit History: {credit_history}")
    print(f"Guarantee/Co-signer: {has_guarantee}")
    print(f"{cliente_name}, APPROVED WITH CONDITIONS. Requires guarantor review")
    print("________________________________________________________________________")
else:
    print("_________________________________________________________________________")
    print(f"Client Name: {cliente_name}")
    print(f"Monthly Income: ${client_income:.2f} ")
    print(f"Credit History: {credit_history}")
    print(f"Guarantee/Co-signer: {has_guarantee}")
    print(f"{cliente_name}, REJECTED. Does not meet the risk policies")
    print("_________________________________________________________________________")
