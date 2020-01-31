import parser
import utils


DATA = parser.parse_data()


def get_all_salaries(data):
    not_formatted = [v.salary for v in data if v.salary != 'No salary']
    return not_formatted


utils.print_data(DATA)
