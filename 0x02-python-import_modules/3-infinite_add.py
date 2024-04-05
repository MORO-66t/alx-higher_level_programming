#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    lenth = len(sys.argv) - 1
    for i in range(lenth):
        sum += int(sys.argv[i + 1])
    print(sum)
