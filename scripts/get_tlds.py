from urllib.request import urlopen

URL = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"

def write_file(file, tlds: list[str]):
    # Don't add new line to last tld
    for i in range(len(tlds) - 1):
        tlds[i] = tlds[i] + "\n"

    with open(file, "w") as f:
        f.writelines(tlds)

with urlopen(URL) as resp:
    status_code = resp.getcode()
    if status_code != 200:
        raise ValueError(f"status code not 200, status code: {status_code}")
    data = resp.read().decode("utf-8")

all_tlds = data.strip().split("\n")
all_tlds.pop(0) # Removes file header
all_tlds = [tld.lower() for tld in all_tlds]

country_code = [tld for tld in all_tlds if len(tld) == 2]
generic_code = [tld for tld in all_tlds if len(tld) > 2]
punycode = [tld for tld in all_tlds if tld.startswith("xn--")]

write_file("../all_tlds.txt", all_tlds)
write_file("../country_code_tlds.txt", country_code)
write_file("../generic_tlds.txt", generic_code)
write_file("../punycode_tlds.txt", punycode)
