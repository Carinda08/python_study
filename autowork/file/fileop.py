import os

mf = "p:\\code\\python\\python_study\\README.md"
of = open(mf, 'r')
print(of.read())

mf = "p:\\code\\python\\python_study\\autowork\\file\\test.txt"
of = open(mf, 'w')
of.write("hello world\n")
of.write("hello python\n")
of.write("hello vim")
of.close()

of = open(mf)
print("List is : \n " + "".join(s for s in of.readlines()))
