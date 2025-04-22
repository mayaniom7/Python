employees = {
    101: {'emp_roll_no': 1, 'salary': 50000},
    101: {'emp_roll_no': 2, 'salary': 60000},
    102: {'emp_roll_no': 3, 'salary': 70000},
    102: {'emp_roll_no': 4, 'salary': 45000},
    103: {'emp_roll_no': 5, 'salary': 90000},
    103: {'emp_roll_no': 6, 'salary': 85000}
}

department_salaries = {}

for dept_no, info in employees.items():
    salary = info['salary']
    if dept_no not in department_salaries:
        department_salaries[dept_no] = [salary]
    else:
        department_salaries[dept_no].append(salary)
for dept_no, salaries in department_salaries.items():
    print(f"Dept {dept_no} - Min Salary: {min(salaries)}, Max Salary: {max(salaries)}")
