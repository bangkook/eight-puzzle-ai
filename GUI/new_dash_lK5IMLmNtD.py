import abstra.dashes as ad
import sys
sys.path.append('../eight-puzzle-ai/Code')  # Add the directory containing Code.py to the sys.path
from Code import get_hi  # Now, you can import get_hi from Code.py
get_hi()

x = 2
y = 3

def get_sum():
    return x + y

def show_sum():
    ad.alert(get_sum())
