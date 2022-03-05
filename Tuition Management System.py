# create python application for Tuition Management System

Trainer_1 = input("Enter Trainer Name 1:")
Subject_1 = input("Enter First Trainer Subject:")
L_of_month = int(input("Enter Total lecture of Trainer 1:"))
teach_student = int(input("Enter student of teach this month:"))
incentive = 5000
cut_in_salary = 8000

# Total salary of trainer
totalsalryoftrainer_1 = 20000

TA = 20000 * 0.1
DA = 20000 * 0.07
HRA = 20000 * 0.2
PF = 20000 * 0.18

# Total salary of Trainer 1
total_1 = totalsalryoftrainer_1 + TA + DA + HRA - PF


# Teacher lecture in a month

if L_of_month >= 12:
    print("L_of_month is grater than 12")
    net_sal = total_1 + incentive
    print(net_sal)

elif L_of_month < 12:
    print("L_of_month is less than 12")
    net_sal = total_1 - cut_in_salary
    print(net_sal)



# Trainer 2
T_2 = input("Enter Trainer 2 Name:")
T_S = input("Enter Trainer 2 Subject: ")
L_of_month2 = int(input("Enter total lecture of month:"))

incentive_2 = 10000
cut_2 = 8000
TA_2 = 0.1 * 30000
DA_2 = 0.07 * 30000
HRA_2 = 0.2 * 30000
PF_2 = 0.18 * 30000

# Total salary of trainer 2
totalsalaryoftrainers_2 = 30000

# Total salary after incentive
total1 = totalsalaryoftrainers_2 + TA + DA + HRA - PF

if L_of_month2 >= 16:
    print("L_of_month2 is greater than 16")
    net_sal_1 = totalsalaryoftrainers_2 + incentive_2
    print(net_sal_1)


elif L_of_month2 < 16:
    print("Lecture of Month is less than 16 ")
    net_sal_1 = totalsalaryoftrainers_2 - cut_2
    print(net_sal_1)


# Searching OF All Information of trainer
nos = int(input("Enter no to search :"))
if nos == 1:
    total1 = totalsalryoftrainer_1 + incentive + TA + DA + HRA - PF
    print("*" * 50)
    Net = total1 - cut_in_salary - incentive
    print("*" * 50)
    print(total1)
    print("*" * 50)
    print("L_of month is less then 12")
    print("*" * 50)
    print(Net)
    print("*" * 50)

nos = int(input("Enter No to search :"))
if nos == 2:
    total1 = totalsalaryoftrainers_2 + incentive + TA + DA + HRA - PF
    print("*" * 50)
    total2 = total1 - cut_2 - incentive
    print("*" * 50)
    print(total1)
    print("*" * 50)
    print(total2)
    print("*" * 50)

print("*" * 50)
print("\tTrainer-1:-", Trainer_1)
print("*" * 50)
print("\tSubject-1:-", Subject_1)
print("*" * 50)
print("\tLecture Of Month:-", L_of_month)
print("*" * 50)
print("\tTeach Student in Month:-", teach_student)
print("*" * 50)
print('\tTotal Salary-1:-', totalsalryoftrainer_1)
print("*" * 50)
print("\tTotal-1:-", total_1)
print("*" * 50)

print("\t\tTrainer-2 All Information\t\t")
print("*"*50)
print("\tTrainer-2:-", T_2)
print("*" * 50)
print("\tSubject-2:-", T_S)
print("*" * 50)
print("\tLecture Of Month-2:-", L_of_month2)
print("*" * 50)
print("\tTeach Student in Month:-", teach_student)
print("*" * 50)
print("\tTotal Salary-2:-", totalsalaryoftrainers_2)
print("*" * 50)
print("\tTotal-1:-", total1)
print("*" * 50) 

