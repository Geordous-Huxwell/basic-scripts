import mathModule
print(mathModule.PI)
from mathModule import PI
print(PI)
from mathModule import *
print(PI)
print(locals())

import mathModule
print(mathModule.add(4,9))
