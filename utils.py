def print_data(data: list):
    for idx, item in enumerate(data):
        print(f'ID: {idx+1}\nTitle: {item.title}\nCompany: {item.company}\nMetro: {item.metro}\nLink: {item.link}')
        print('=' * 100)
