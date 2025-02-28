if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        com, *arr = input().split()
        match com:
            case "insert":
                list.insert(int(arr[0]), int(arr[1]))
            case "remove":
                list.remove(int(arr[0]))
            case "append":
                list.append(int(arr[0]))
            case "sort":
                list.sort()
            case "pop":
                list.pop()
            case "reverse":
                list.reverse()
            case "print":
                print(list)