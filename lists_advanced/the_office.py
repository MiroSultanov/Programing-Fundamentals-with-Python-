# employees = input().split(" ")
# employees = list(map(int, employees))
# factor = int(input())
#
# happy_employees = list(filter(lambda emp: emp >= sum(employees) / len(employees), employees))
# if len(happy_employees) >= len(employees) / 2:
#     print(f"Score: {happy_employees}/{len(employees)}. Employees are happy!")
# else:
#     print(f"Score: {happy_employees}/{len(employees)}. Employees are not happy!")

employees = input().split(" ")
factor = int(input())

employees = list(map(lambda emp: int(emp) * factor, employees))
filtered = list(filter(lambda emp: emp >= sum(employees) / len(employees), employees))
if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")



