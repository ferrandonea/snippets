# way cooler than printing

"""
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL
    """

import logging
#from logging import root
# import root logger but not necessary in this tutorial

# basic logging
# notice they do not all get displayed by default


def test():
    print('-'*20)
    logging.debug('debug message here')
    logging.info('info message here')
    logging.warning('warning message here')
    logging.error('error message here')
    logging.critical('critical message here')
    print('-'*20)


test()


def test():
    print('=-'*20)
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(f"Log Level: {level}")
    logging.debug('debug message here')
    logging.info('info message here')
    logging.warning('warning message here')
    logging.error('error message here')
    logging.critical('critical message here')
    print('-='*20)


test()

# getting and setting logging levels
# allows filtering

#get the root logger
rootlog = logging.getLogger()
print ('Level : ' + logging.getLevelName(rootlog.getEffectiveLevel()))

#set it to debug
rootlog.setLevel(logging.DEBUG)
test()

#set it to critical
rootlog.setLevel(logging.CRITICAL)
test()

#set it to warning
rootlog.setLevel(logging.WARNING)
test()

#root is the name of the logger

# Log to a file
# using logging basicConfig() only can be used one you can not change it
# it has to be used BEFORE any action

handler = logging.FileHandler('file.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 

handler.setFormatter(formatter)
rootlog.addHandler(handler)
rootlog.setLevel(logging.DEBUG)
rootlog.debug('test')
test()
