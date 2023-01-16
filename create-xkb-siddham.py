# Read text files
with open("input/devanagari.txt", "r") as f:
    d = f.read().split("\n")
with open("input/siddham.txt", "r") as f:
    s = f.read().split("\n")
# Create mapping from text files: {unicode_generic_name : unicode_code }
def get_characters(l: [str]) -> dict[str, str]:
    result = {}
    for line in l:
        split = line.split("\t")
        if len(split) != 3: # Does not match
            continue
        symbol, unicode_code, unicode_name = split
        generic_name = " ".join(unicode_name.split(" ")[1:]) # Remove first word
        result[generic_name] = unicode_code
    return result
devanagari = get_characters(d)
siddham = get_characters(s)
common_keys = devanagari.keys() & siddham.keys()
devanagari_to_siddham = {devanagari[key].replace("U+", "U"): siddham[key].replace("U+", "U") for key in common_keys}
# # Write yaml
# with open("devanagari-to-siddham.yaml", "w") as f:
#    f.writelines([f"{k}: {v}\n" for k, v in devanagari_to_siddham.items()])

# Read xdb file
with open("input/xkb-in.orig", "r") as f:
    xkb_in = f.read()
# Replace characters
for k, v in devanagari_to_siddham.items():
    xkb_in = xkb_in.replace(k, v)
    xkb_in = xkb_in.replace(k.lower(), v)
    xkb_in = xkb_in.replace(k.lower().capitalize(), v)
# Write out
with open("output/xkb-in.siddham", "w") as f:
    f.write(xkb_in)

