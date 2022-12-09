from Node import Node


if __name__ == '__main__':
    prvy = Node("prvy")
    prvy.add_dir("dir11")
    prvy.add_dir("dir222222222")
    prvy.add_dir("dir3")
    prvy.add_file("file1", 23423)
    prvy.add_file("file2222222", 3223423)
    prvy.add_file("file3", 233)
    prvy.add_file("file4", 1123423)

    print(prvy)
    print(prvy.ls())
    print(prvy.size())

    druhy = Node("druhy")
    treti = Node("treti")
    svrty = Node("svrty")

