from time import sleep
from requests import get


YOUR_ID = 4595629667715728

def count_seconds(seconds):
    for i in range(seconds, 0, -1):
        print(f"{i} seconds remaining\r", end='')
        sleep(1)
    print("                                \r")

while True:
    user_input = input("CODE: ")
    if user_input != "exit!":
        res = get(f"https://qsmp.global/api/answers?ans={user_input}&id={YOUR_ID}")
        print(res.content)
        count_seconds(65)
    else:
        break