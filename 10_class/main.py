#from inheritance_common import *
from inheritance_multi import *
"""부모 메서드 호출하기"""

a = Korea('대한민국', 50000000, '서울')
a.show()
#a.show_name()
print(Korea.mro())
