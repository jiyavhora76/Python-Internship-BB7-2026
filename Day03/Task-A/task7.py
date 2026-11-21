employees = ["Jiya", "Aksa", "Aamena", "Ruhin", "Aaysha"]

salaries = [25000, 30000, 28000, 35000, 32000]

for name, salary in zip(employees, salaries):
    print(name, ":", salary)