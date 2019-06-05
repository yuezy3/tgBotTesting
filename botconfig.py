import os.path
import sys 
import configparser

# check config file existence, if not exists,  tell 
# user to edit and exit
script_path = os.path.dirname(os.path.abspath( __file__ ))
configFileName = "botConfig.cfg"
configpath = os.path.join(script_path, configFileName)
config = configparser.ConfigParser()
token = ''
proxy = ''
if os.path.isfile(configpath) :
    print("Config file exists and go on\n")
else:
    print("Found no config file missing, need it in {}".format(configpath))
    sys.exit(0)
# reading config file and inspect tonken and proxy setting
with open(configpath,'r',encoding='utf-8') as f:
    config.read_file(f)
    if not config.has_option('main', 'token') or not config['main']['token']:
        print('need token in {}\n'.format(configpath))
        sys.exit(0)
    token = config['main']['token']
    if not config.has_option('main', 'token'):
        proxy = ''
    else:
        proxy = config['main']['proxy']
