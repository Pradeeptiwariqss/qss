import configparser
conf = configparser.RawConfigParser()
conf.read('config.properties')
print(conf.sections())
print(conf.get('details', 'Name'))