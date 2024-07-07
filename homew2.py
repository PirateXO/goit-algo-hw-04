
def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        try:
                            cat_id = parts[0].strip()
                            name = parts[1].strip()
                            age = int(parts[2].strip())
                            
                            cat_info = {
                                "id": cat_id,
                                "name": name,
                                "age": age
                            }
                            cats_info.append(cat_info)
                        except ValueError:
                            continue
        return cats_info
    
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file '{path}': {str(e)}")
        return []

path_to_file = 'cats_info.txt'  # Шлях до файлу з інформацією про котів
cats_info = get_cats_info(path_to_file)

for cat in cats_info:
    print(cat)
