string = 'able was i ere i saw ELBA'


def isPalindrome(ip):
    # convert string to lowercase
    ip = ip.lower()
    result = True
    ## Till we reach middle element of the string, compare first and last element.
    ## If they don't match, set return value to false and break
    for i in range(0, (int)((len(ip)) / 2)):
        if ip[i] != ip[-(i + 1)]:
            result = False
            break

    return result


def main():
    print("main")
    print(isPalindrome(string))
    print(isPalindrome('anna'))


if __name__ == "__main__":
    main()
