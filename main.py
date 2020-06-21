import os
import argparse
import random

from faker import Faker

import file_operations

SKILLS_PER_HERO = 3
SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
]
LETTERS_MAPPING = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def get_runic_skills(skills, letters_mapping):
    runic_skills = []
    for skill in skills:
        for letter in skill:
            skill = skill.replace(letter, letters_mapping[letter])
        runic_skills.append(skill)
    return runic_skills


def get_random_number(lower=8, upper=14):
    return random.randint(lower, upper)


def generate_hero(skills, fake):
    skill_1, skill_2, skill_3 = random.sample(skills, SKILLS_PER_HERO)
    hero_data = {
        "first_name": fake.first_name_male(),
        "last_name": fake.last_name_male(),
        "town": fake.city(),
        "job": fake.job(),
        "strength": get_random_number(),
        "agility": get_random_number(),
        "endurance": get_random_number(),
        "intelligence": get_random_number(),
        "luck": get_random_number(),
        "skill_1": skill_1,
        "skill_2": skill_2,
        "skill_3": skill_3
    }
    return hero_data


def get_output_directory():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="output directory path for generated files")
    return parser.parse_args().output


if __name__ == '__main__':
    output_dir = get_output_directory()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    fake = Faker("ru_RU")
    runic_skills = get_runic_skills(SKILLS, LETTERS_MAPPING)
    for num in range(10):
        hero = generate_hero(runic_skills, fake)
        output_file_name = os.path.join(output_dir, f"hero{num}.svg")
        file_operations.render_template("src/template.svg", output_file_name, hero)



