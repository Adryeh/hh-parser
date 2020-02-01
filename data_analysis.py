import parser
import utils


DATA = parser.parse_data()


def get_all_salaries(data):
    not_formatted = [v.salary for v in data if v.salary != 'No salary']
    return not_formatted


def get_ruble_salaries(data):
    rub = [s for s in data if 'руб' in s]
    return rub


def get_dollar_salaries(data):
    usd = [s for s in data if 'USD' in s]
    return usd


def get_avg_from_ruble_salaries(data):
    formatted = []
    for salary in data:
        if '-' in salary:
            continue
        salary = int(''.join([ch for ch in salary if ch.isdigit()]))
        formatted.append(salary)
    return sum(formatted) // len(formatted)


all_salaries = get_all_salaries(DATA)
usd_salaries = get_dollar_salaries(all_salaries)
rub_salaries = get_ruble_salaries(all_salaries)
rub_avg = get_avg_from_ruble_salaries(rub_salaries)


utils.print_data(DATA)
