import requests
import pprint
import re
from hh_request import HHRequests

hh_url = 'https://api.hh.ru/'

hh_url_vacancies = f'{hh_url}vacancies'

requests_params = {'text': 'python', 'page': 1}


vacancy_text = input('Какую вакансию вы ишите? ').lower()
vacancy_town = input('В каком городе Вам хотелось бы работать? ').lower()

test_request = HHRequests(vacancy_text, vacancy_town)

test_request.hh_get_vacancy_inf

pprint.pprint(test_request)



#test_list = {'requirement': feedback['items'][vac_number]['snippet']['requirement'], 'salary': feedback['items'][vac_number]['salary']}


#regexp = re.compile(r'\w+\d\.\d|\w+', re.ASCII)
