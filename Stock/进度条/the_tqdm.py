
''' 
@File    :   the_tqdm.py
@Time    :   2022/11/23 21:24:56
'''
from tqdm import tqdm
import time

def main():
    for i in tqdm(range(10000)):
        time.sleep(1)
        pass


if __name__ == "__main__":
    main()
