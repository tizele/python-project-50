def generate_diff(data1, data2):

    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = sorted(keys1.union(keys2))

    diff = "{\n"
    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff += f"   {key}: {data1[key]}\n"
            else:
                diff += f" - {key}: {data1[key]}\n"
                diff += f" + {key}: {data2[key]}\n"
        elif key in data1:
            diff += f" - {key}: {data1[key]}\n"
        else:
            diff += f" + {key}: {data2[key]}\n"
    diff += "}"

    return diff




