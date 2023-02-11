def read_inventory(filename):
    infile = open(filename, 'r')
    packages = []
    package_content_list = []
    for line in infile:
        content = line.rstrip()
        content_list = content.split(",")
        package = ''.join(content_list[0])
        packages.append(package)
        package_content_list.append(content_list[1:])
    infile.close()
    return packages, package_content_list


def tupilize_content(listoflist):
    result_as_tup = []
    for i in listoflist:
        k = []
        for j in i:
            inside = j.split(" ")
            x, y = int(inside[0]), " ".join(inside[1:])
            k.append((x, y))
        result_as_tup.append(k)
    return result_as_tup


def get_items_dict(listoflistoftup):
    d = {}
    d_value = 0
    for package in listoflistoftup:
        for element in package:
            if element[1] not in d.values():
                d[d_value] = element[1]
                d_value += 1
    return d

packages, package_content_list = read_inventory("kolilistesimain.txt")
package_content_as_tup = tupilize_content(package_content_list)
items_dict = get_items_dict(package_content_as_tup)

print("koli", end=",")
for i in range(len(items_dict)):
    if i != len(items_dict) - 1:
        print(items_dict[i], end=",")
    else:
        print(items_dict[i])

for j in range(len(packages)):
    print(packages[j], end=",")
    line_dict = {}
    for k in range(len(package_content_as_tup[j])):
        line_dict[package_content_as_tup[j][k][1]] = package_content_as_tup[j][k][0]
    for m in range(len(items_dict)):
        if items_dict[m] not in line_dict.keys():
            line_dict[items_dict[m]] = 0
    values = []
    for f in items_dict.values():
        values.append(f)
    for p in range(len(values)):
        if p != len(values) - 1:
            print(line_dict[values[p]], end=",")
        else:
            print(line_dict[values[p]])








