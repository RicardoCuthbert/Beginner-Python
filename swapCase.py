def swap_case(s):
    # text = ""
    # for x in s:
    #     if (x.isupper()):
    #         text += x.lower()
    #     else:
    #         text += x.upper()   
    return "".join([x.lower() if x.isupper() else x.upper() for x in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)