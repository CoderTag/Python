# import os
# # __name__=os.path.dirname(os.path.abspath(__file__))
# __name__ = __file__
# print(__name__)
# __name__=__name__.replace('/','.').replace('.py','')
# print(__name__)
# __name__ = "level1.level2.lev2"
# from ..level1.level2 import lev2

import sys
# sys.path.insert(0,"../../package")
#export PYTHONPATH="../"
print(sys.path)
import level1.level3.level4
