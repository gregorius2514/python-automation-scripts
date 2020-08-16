#import yaml

class ConfigLoader():
    def __init__(self):
        # with open(configFilePath, 'r') as configFile:
        self.logFilePath ="/tmp/dummy.log"
        self.rootFilePath = "/tmp"

            # try:
            #     configuration = yaml.load(configFile)
            #     self.logFilePath = configuration.logger.logFilePath
            #     self.rootFilePath = configuration.finder.rootFilePath
            # except yaml.YAMLError as parseError:
            #     print("Error when try to parse config file: [{}], error: ".format(configFile, parseError))