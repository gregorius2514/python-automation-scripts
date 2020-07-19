import yaml

class ConfigLoader():
    def __init__(self, configFilePath = 'config.yml'):
        with open(configFilePath, 'r') as configFile:
            try:
                self.configuration = yaml.load(configFile)
            except yaml.YAMLError as parseError:
                print('Error when try to parse config file: [{}], error: '.format(configFile, parseError))