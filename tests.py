import pytest
from main import read_population_data, sort_by_area, sort_by_population

@pytest.fixture
def population_data():
    return [
        ('Україна', 603628, 41590213),
        ('Німеччина', 357592, 83783942),
        ('Франція', 551695, 65273511),
        ('Іспанія', 505990, 47329981),
        ('Італія', 301340, 60461826),
        ('Китай', 9706961, 1439323776),
        ('Індія', 3287590, 1380004385),
        ('США', 9372610, 331002651),
        ('Індонезія', 1904569, 273523615),
        ('Пакистан', 881913, 220892340)
    ]

def test_read_population_data(tmp_path, population_data):
    file_path = tmp_path / "test_population_data.txt"
    with open(file_path, 'w', encoding='utf-8') as file:
        for country, area, population in population_data:
            file.write(f"{country},{area},{population}\n")

    assert read_population_data(file_path) == population_data

def test_sort_by_area(population_data):
    expected_result = [
        ('Італія', 301340, 60461826),
        ('Німеччина', 357592, 83783942),
        ('Іспанія', 505990, 47329981),
        ('Франція', 551695, 65273511),
        ('Україна', 603628, 41590213),
        ('Пакистан', 881913, 220892340),
        ('Індонезія', 1904569, 273523615),
        ('Індія', 3287590, 1380004385),
        ('США', 9372610, 331002651),
        ('Китай', 9706961, 1439323776)
    ]
    assert sort_by_area(population_data) == expected_result

def test_sort_by_population(population_data):
    expected_result = [
        ('Пакистан', 881913, 220892340),
        ('Україна', 603628, 41590213),
        ('Іспанія', 505990, 47329981),
        ('Італія', 301340, 60461826),
        ('Франція', 551695, 65273511),
        ('Індонезія', 1904569, 273523615),
        ('Німеччина', 357592, 83783942),
        ('Індія', 3287590, 1380004385),
        ('США', 9372610, 331002651),
        ('Китай', 9706961, 1439323776)
    ]
    assert sort_by_population(population_data) == expected_result
