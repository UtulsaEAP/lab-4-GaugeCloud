"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Gauge Cloud
Lab Time: 3:00

"""


def reverse_binary():
    user_num = int(input())
    while user_num > 0:
        print (user_num % 2, end="")
        user_num = user_num // 2

if __name__ == "__main__":
    reverse_binary()