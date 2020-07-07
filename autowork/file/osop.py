import os

def joinpath():
    print("current path: %s" % os.getcwd())
    print("abs path: " + os.path.abspath(os.getcwd()))
    print("rel path: " + os.path.relpath(os.getcwd()))

    path = os.path.join('p:\\', 'code', 'python')
    print("joined path: " + path)
    os.chdir(path)
    print("Now current path:" + os.getcwd())

def pathname():
    myfile = "p:\\code\\python\\python_study\\README.md"
    print("dir name: " + os.path.dirname(myfile))
    print("file name: " + os.path.basename(myfile))
    print("both: (%s, %s)" % os.path.split(myfile))
    print("split all: " + "-".join(s for s in myfile.split(os.path.sep)))

if __name__ == '__main__':
    joinpath()
    pathname()
