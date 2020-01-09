import json
import pprint


class ParserJsonDict:

    # создаем конструктор класса
    def __init__(self, json_file_name, request_text):
        self._json_file_name = json_file_name
        self._request_text = request_text

    # создаем функцию для доступа к переменной self._json_file_name
    @property
    def json_file_name(self):
        return self._json_file_name

    # создаем функцию для доступа к переменной self._request_text
    @property
    def request_text(self):
        return self._request_text

    # создаем функцию для открытия файла json-формата
    @property
    def vacancies_dict(self):
        with open(self.json_file_name, 'r') as dict_json:
            loaded_dict = json.load(dict_json)
        return loaded_dict

vacancies_dict =    {
                    'vacancy_text': 'python',
                    'vacancies_count': 0,
                    'vacancy_avg_salary': 0,
                    'vacancies_skills': {}
                    }

vacancies_dict['vacancies_count'] = len(loaded_dict)

for element in loaded_dict.values():

    for skill_list in element['skills']:

        if skill_list['name'] not in vacancies_dict['vacancies_skills']:
            vacancies_dict['vacancies_skills'][skill_list['name']] = {
                                                                'skill_count': 1,
                                                                'skill_percent': 0
                                                             }
        if skill_list['name'] in vacancies_dict['vacancies_skills']:
            current_skill_count_value = vacancies_dict['vacancies_skills'][skill_list['name']]['skill_count']
            vacancies_dict['vacancies_skills'][skill_list['name']]['skill_count'] = current_skill_count_value + 1

for element in vacancies_dict['vacancies_skills'].values():

    element['skill_percent'] = round(element['skill_count'] * 100 / vacancies_dict['vacancies_count'], 1)

avg_salary = 0
vacancies_count_with_salary = 0
for element in loaded_dict.values():
    if element['salary'] is not None:
        if element['salary']['from'] is not None and element['salary']['currency'] == 'RUR':
            avg_salary += element['salary']['from']
            vacancies_count_with_salary += 1
        #pprint.pprint(element['salary']['to'])

avg_salary = round(avg_salary / vacancies_count_with_salary)

vacancies_dict['vacancy_avg_salary'] = avg_salary
# for element in loaded_dict.values():
#     for skill_list in element['skills']:
#         if skill_list['name'] in test_list['vacancies_skills']:
#             current_skill_count_value = test_list['vacancies_skills'][skill_list['name']]['skill_count']
#             test_list['vacancies_skills'][skill_list['name']]['skill_count'] = current_skill_count_value + 1
#         #

pprint.pprint(vacancies_dict)
        #for element_in_skill_list in range(0, len(skill_list)):
        #pprint.pprint(skill_list[element_in_skill_list])
        #pprint.pprint('{0} {1}'.format(element, skill['name']))
        #for skills_element in range(0, len(loaded_dict[element]['skills'])):

            #for skill_name in loaded_dict[element]['skills'][skills_element]:

            #pprint.pprint(loaded_dict[element]['skills'])