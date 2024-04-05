def read_population_data(file_path):
    population_data = []

    # Читання даних з файлу
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Розділення рядка на компоненти: назва країни, площа, населення
            country, area, population = line.strip().split(',')
            # Перетворення площі та населення в числовий формат
            area = float(area)
            population = int(population)
            # Додавання даних до списку
            population_data.append((country, area, population))

    return population_data


def sort_by_area(population_data):
    # Сортування даних за площею
    sorted_by_area = sorted(population_data, key=lambda x: x[1])
    return sorted_by_area


def sort_by_population(population_data):
    # Сортування даних за населенням
    sorted_by_population = sorted(population_data, key=lambda x: x[2])
    return sorted_by_population



def main():
    """
    """
    file_path = r'C:\\Users\\user\\Desktop\\ci_cd\\info.txt' 
    try:
        population_data = read_population_data(file_path)
        sorted_by_area = sort_by_area(population_data)
        sorted_by_population = sort_by_population(population_data)

        print("Відсортовані дані за площею:")
        for country, area, population in sorted_by_area:
            print(f"{country}: Площа: {area}, Населення: {population}")

        print("\nВідсортовані дані за населенням:")
        for country, area, population in sorted_by_population:
            print(f"{country}: Площа: {area}, Населення: {population}")

    except FileNotFoundError:
        print("Файл не знайдено.")

if __name__ == "__main__":
    main()