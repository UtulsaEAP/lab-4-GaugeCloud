"""
Complete the following python code to reverse the string entered by the user.

Name: Gauge Cloud
Lab Time: 3:00
"""

def reverse_string():
   while True:
    text = input()
    if text.lower() == 'done' or text.lower() == 'd':
        break
    print(text[::-1])
        
    

if __name__ == "__main__":
    reverse_string()