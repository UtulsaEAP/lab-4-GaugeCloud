"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Gauge Cloud
Lab Time: 3:00
"""

def norm():
    x = int(input())
    dislist = []
    i = 1
    while i <= x:
        y = float(input())
        dislist.append(y)
        i += 1
    large = max(dislist)

    for item in dislist:
        value = item / large
        print(f'{value:.2f}')
if __name__ == "__main__":
    norm()