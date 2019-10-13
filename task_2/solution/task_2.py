input_string = 'maaaaaaaria'


def list_compression(str_1: str):
    count = 1
    result = str_1[0]

    for i in str_1[1:]:
        if result[-1] == i:
            count += 1
        else:
            result += str(count) + i
            count = 1

    result += str(count)

    if len(result) > len(str_1):
        return str_1

    return result

print(list_compression(input_string))
