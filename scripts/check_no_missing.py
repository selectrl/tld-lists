def read_file(file) -> list[str]:
    with open(file, "r") as f:
        return sorted([tld.strip().lower() for tld in f.readlines()])


generic_tlds = read_file("../generic_tlds.txt")

seen_tlds = []
seen_tlds.extend(read_file("../inactive_tlds.txt"))
seen_tlds.extend(read_file("../private_tlds.txt"))
seen_tlds.extend(read_file("../punycode_tlds.txt"))
seen_tlds.extend(read_file("../restricted_tlds.txt"))
seen_tlds.extend(read_file("../unrestricted_tlds.txt"))

for tld in seen_tlds:
    generic_tlds.remove(tld)

for tld in generic_tlds:
    print(tld)
