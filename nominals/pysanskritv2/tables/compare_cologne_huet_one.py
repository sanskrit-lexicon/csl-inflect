""" compare_cologne_huet_one.py
 
"""
import sys
import compare_cologne_huet_file as COMPARE

if __name__ == "__main__":
 model = sys.argv[1]
 key = sys.argv[2]
 COMPARE.testprint(model,key)
