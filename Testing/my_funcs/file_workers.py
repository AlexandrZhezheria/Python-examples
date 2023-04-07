def read_from_file(filepath):
    with open(filepath, "r") as f_o:
        return f_o.readline()

print(read_from_file("prodfile.txt"))
