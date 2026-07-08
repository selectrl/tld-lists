def process_file(file: str):
    with open(file, "r") as f:
        tlds = sorted([tld.strip().lower() for tld in f.readlines()])

    # Don't add new line to last tld
    for i in range(len(tlds) - 1):
        tlds[i] = tlds[i] + "\n"

    with open(file, "w") as f:
        f.writelines(tlds)

process_file("../all_tlds.txt")
process_file("../country_code_tlds.txt")
process_file("../generic_tlds.txt")
process_file("../inactive_tlds.txt")
process_file("../private_tlds.txt")
process_file("../punycode_tlds.txt")
process_file("../restricted_tlds.txt")
process_file("../unrestricted_tlds.txt")
