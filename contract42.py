def read_numbers_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.read().split(',')
            numbers = [int(num.strip()) for num in lines]
            return numbers
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
        return []
    except ValueError:
        print(f"Файл '{file_name}' містить некоректні дані.")
        return []


def sort_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers

def check_for_42(numbers):
    if 42 in numbers:
        print('Знайдено відповідь на основне питання життя, всесвіту, і взагалі усього! і нававіть питання моєї оцінки , 42 ІСНУЄЄЄЄЄЄ!!!!!!!!!')
    else:
        print('Відповідь не знайдена')

def write_numbers_to_file(file_name, numbers):
    try:
        with open(file_name, 'w') as file:
            for num in numbers:
                file.write(str(num) + '\n')
    except IOError:
        print(f"Не вдалося записати в файл '{file_name}'.")

def main():
    input_file = 'numbers.txt'
    output_file = 'sorted_numbers.txt'

    # Читання чисел з файлу
    numbers = read_numbers_from_file(input_file)

    # Сортування чисел
    sorted_numbers = sort_numbers(numbers)

    # Перевірка наявності числа 42 та вивід відповідної інформації
    check_for_42(sorted_numbers)

    # Запис відсортованих чисел у файл
    write_numbers_to_file(output_file, sorted_numbers)

if __name__ == "__main__":
    main()
