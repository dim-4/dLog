from dlog import *

l = Logger(line_length=120, time_format="local-%H:%M:%S", compact=True)

my_data = {'a': 'xyz', 'b': 123, 'c': ['uvw '*100]*10,
           'd': [_ for _ in range(1000)]}

l.info('hello-world'*40 + " hi", my_data, color=MAG, divider=MAG,
       show_metadata=False)
l.info('hello-world ' + " hi", data={"a": "b", "c": [1, 2, 123]},
       color=YELLOW, divider=YELLOW)
l.debug('hello-world ' + " hi", data={"a": "b", "c": [1, 2, 123]},
        color=YELLOW, divider=YELLOW+UND)
l.warning('hello-world ' + " hi", data={"a": "b", "c": [1, 2, 123]},
          color=YELLOW, divider=YELLOW+UND)
l.error('hello-world ' + " hi", data={"a": "b", "c": [1, 2, 123]},
        color=YELLOW, divider=YELLOW+UND)
l.critical('hello-world ' + " hi", data={"a": "123_456", "c": [1, 2, 123456]},
           color=YELLOW, divider=YELLOW+UND)

l.critical("Hello friend.", div=MAG)

l.crit("Hello friend.", div=MAG)

l("Hello friend.", div=GRN)  # shortcut for l.info

try:
    x = 5 / 0
except Exception as e:
    l.info(exc=e)
x = {"a": "b", "c": [_ for _ in range(100)]}

l.json(x, msg="json format:")  # json format for quick copying 
