__author__ = 'yi-linghwong'

import re

a = 'love#1'

if re.search('[#]+[0-9]+[0-9]', a):

    print ('good')

else:

    print ('no')




