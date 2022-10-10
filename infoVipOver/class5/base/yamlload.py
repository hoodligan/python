import yaml


class YamlUtil:
    def __init__(self,yaml_file):
        self.yaml_file=yaml_file

    def read_yaml(self):
        with open(self.yaml_file,encoding='utf-8')as f:
            value=yaml.load(f,Loader=yaml.FullLoader)
            # print(value)
        return value

if __name__ == '__main__':
    YamlUtil('../data/login.yml').read_yaml()
