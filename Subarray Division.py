def birthday(s, d, m):
    # Write your code here
    count = 0
    for i in range(m, n+1):
        if sum(s[i-m:i]) == d:
            count += 1
    return count


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)
