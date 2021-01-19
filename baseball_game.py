# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    if user_input_number.isdigit(): return True
    else: return False


def is_between_100_and_999(user_input_number):
    num = int(user_input_number)
    if(num>=100 and num<=999): return True
    else: return False


def is_duplicated_number(three_digit):
    if (three_digit=='100'): return True
    num = [three_digit[0], three_digit[1], three_digit[2]]
    rst = len(set(num))
    return False if (rst==3) else True


def is_validated_number(user_input_number):
    if not is_digit(user_input_number): return False
    if not is_between_100_and_999(user_input_number): return False
    if is_duplicated_number(user_input_number): return False
    return True


def get_not_duplicated_three_digit_number():
    while True:
        num = get_random_number()
        if not (is_duplicated_number(str(num))): break
    return num


def get_strikes_or_ball(user_input_number, random_number):
    input_num = str(user_input_number)
    answer = str(random_number)
    strikes=0
    balls=0
    for i in range(3):
        for j in range(3):
            if(input_num[i]==answer[j]):
                if(i==j): strikes+=1
                else: balls+=1
    return [strikes, balls]


def is_yes(one_more_input):
    t = one_more_input.lower()
    if (t=='y' or t=='yes'): return True
    else: return False
    

def is_no(one_more_input):
    t = one_more_input.lower()
    if (t=='n' or t=='no'): return True
    else: return False


def main():
    game=True
    print("Play Baseball")
    user_input = ''
    while game:
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)
        while game:
            while game:
                user_input = input("Input guess number : ")
                if(user_input=='0'): break
                elif(is_validated_number(user_input)): break
                else: print("Wrong Input, Input again")
            if(user_input=='0'):
                game=False
                break
            strikes, balls = get_strikes_or_ball(user_input, random_number)
            print(f"Strikes : {strikes} , Balls : {balls}")

            if(strikes==3): break
        while game:
            more = input("You win, one more(Y/N)?")
            if(is_no(more)):
                game=False
                break
            elif(is_yes(more)): break
            else: print("Wrong Input, Input again")

    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
