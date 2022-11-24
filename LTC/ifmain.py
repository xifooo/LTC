def mult(x, y):
    print(x*y)
    
mult(3,4)
print(mult(4,5))

import os
from pathlib import Path
# print(__name__, __file__)
# print(os.path.basename(__file__))
# print(os.path.splitext(__file__)[0])
# print(os.path.basename(os.path.splitext(__file__)[0]))
# print(os.path.abspath("."))
print(Path(__file__).parent)
