"""

from app import response1
from app import response2
from app import response3

def valid_response(response1, response2, response3):
    while True:
        print(response1) #good or bad
        if response1 == "good" or response1 == "Good" or response1 == "bad" or response1 == "Bad":
            
            print(response2) #temperature
            if isinstance(response2, float):
                if response2.is_integer() and round(response2, 1) == response2:

                    print(response3) #good or bad
                    if response3.is_integer() and round(response3, 0) == response3:
                        cnt = True
                        print(cnt)
                        break
                    else:
                        cnt = False
                        print(cnt)
                        break

def main():
    valid_response(response1, response2, response3)

main()

"""