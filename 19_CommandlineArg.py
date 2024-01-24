# cd C:\Users\91973\Python_Training
# =========================
# print("hello world")
# print("command line argument")
# ===========================
# import sys
# print(" The command line parameter is ")
# print(sys.argv)
# ==========================
# import sys
# print(" This is commmand line python program execution")
# print("sys.argv is :", sys.argv)
# print("program name is : ", sys.argv[0])
# count = len(sys.argv)
# print("the number of parameters passed is len(sys.argv) :", count-1)
# # ==========================
# Reverse of string
# python 19_CommandlineArg.py python
import sys
s = sys.argv[1]
print(f"Input string is :  {s}")
print(f"Reverse of string : {s[::-1]}")
if s == s[::-1]:
    print("pellindrome")
else:
    print("It is not a pellindrom")
# =========================


# python .\25_CommandlineArg.py kayak.txt asdfadfadasdfasdfasdf asfdasdfad asdfasdfasdf asdfasdf
# fp=open(sys.argv[1],'w')
# for l in sys.argv[2:]:
# 	fp.write(l)

# fp.write(sys.argv[2])
# Assignment :
# Write all the program which we did till now in command line argument.
