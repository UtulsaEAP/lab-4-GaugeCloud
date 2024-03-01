"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name:Gauge Cloud
Lab Time: 3:00
"""

def password_mod():
    word = input()
    password = ''
    word = word.replace('i','1')
    word = word.replace('a','@')
    word = word.replace('m','M')
    word = word.replace('B','8')
    word = word.replace('s','$')
    word = word + '!'
    print(word)

if __name__ == "__main__":
    password_mod()