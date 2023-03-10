def read_inventory(filename):
    infile = open(filename, 'r')
    package_list = []
    for line in infile:
        package_content = line.rstrip()
        package_list.append(package_content)
    infile.close()
    return package_list


def analyze_inventory(inventory):
    items_dict = {}
    for package in inventory:
        inside = package.split(",")
        for element in inside:
            content = element.split(" ")
            count = int(content[0])
            item_as_list = content[1:]
            item = " ".join(item_as_list)
            if item in items_dict:
                items_dict[item] += count
            else:
                items_dict[item] = count
    return items_dict


envanter = read_inventory("kolilistesimain.txt")
icerik = analyze_inventory(envanter)
koli_sayisi = 0
for key in icerik.keys():
    if key.endswith("kolisi"):
        koli_sayisi += icerik[key]
print("Totalde", koli_sayisi, "koli var.")
print("Bu koliler içerisinde şunlar bulunuyor:")
for key in icerik.keys():
    if not key.endswith("kolisi"):
        print("-" + str(icerik[key]), key)
print("Kolilerin dağılımıysa şu şekilde:")
for key in icerik.keys():
    if key.endswith("kolisi"):
        print("-" + str(icerik[key]), key)
