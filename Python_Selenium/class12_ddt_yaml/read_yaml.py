import yaml

file = open('./data/login.yaml', 'r', encoding='utf-8')
values = yaml.load(stream=file, Loader=yaml.FullLoader)
for value in values:
    print(value)
