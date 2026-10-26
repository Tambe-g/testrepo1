import csv 
with open('data/emp.csv' , newline='' ) as file: 
    data = csv.DictReader(file)
    for row_number,row in enumerate(data, start=2):
        employee_id = row['id']
        salary = row['salary']
        if int(salary) < 0 :
            raise ValueError('salary is negative at ' , row_number)
        if not employee_id:
            raise ValueError('employee_id is missing at row' , row_number)

    print('load into target system ')

    

