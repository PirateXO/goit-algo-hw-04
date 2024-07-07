
def add_salary_record(path, name, salary):
    try:
        with open(path, 'a', encoding='utf-8') as file:
            file.write(f"{name},{salary}\n")
    except Exception as e:
        print(f"Error writing to file '{path}': {str(e)}")

def total_salary(path):
    total_sum = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 2:
                        try:
                            salary = int(parts[1].strip())
                            total_sum += salary
                            count += 1
                        except ValueError:
                            continue
    
        if count == 0:
            average_salary = 0
        else:
            average_salary = total_sum / count
        
        return total_sum, average_salary
    
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None, None
    except Exception as e:
        print(f"Error reading file '{path}': {str(e)}")
        return None, None

path_to_file = 'salaries.txt'  

name = input("Введіть прізвище розробника: ")
salary = input("Введіть заробітну плату розробника: ")

add_salary_record(path_to_file, name, salary)

total_sum, average_salary = total_salary(path_to_file)

if total_sum is not None and average_salary is not None:
    print(f"Загальна сума зарплат: {total_sum}")
    print(f"Середня зарплата: {average_salary}")