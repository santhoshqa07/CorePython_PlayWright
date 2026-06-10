#Approach 1

# import Pack1.module1
# import Pack1.Pack2.module2
#
#
# Pack1.module1.display()
# Pack1.Pack2.module2.show()

#Approach 2

# from Pack1.module1 import display
# from Pack1.Pack2.module2 import show
#
# display()
# show()

#Approach 2

# from Pack1 import module1
# from Pack1.Pack2 import module2
#
# module1.display()
# module2.show()


#Approach 3

from Pack1.module1 import *
from Pack1.Pack2.module2 import *

display()
show()






