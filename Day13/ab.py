#Approach 1

import a
import b

aobj = a.Animal()
bobj = b.Bird()

aobj.display()
bobj.display()

#Approach 2

from a import Animal
from b import Bird

aobj = Animal()
bobj = Bird()

aobj.display()
bobj.display()

#Approach 3

from a import *


from b import *

aobj = Animal()
bobj = Bird()

aobj.display()
bobj.display()

