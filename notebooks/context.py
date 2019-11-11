import os
import sys

"""
This enables us to use the ybhack package in our notebooks 
outside the root for nice separation of lib code and jupyter notebooks.
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ybhack
