from pattern_1 import pattern_1
from pattern_2 import pattern_2
from pattern_3 import pattern_3
from pattern_4 import pattern_4
from pattern_5 import pattern_5
from pattern_6 import pattern_6


if __name__ == "__main__":
    character = input("please select the pattern character(ex.: #/*/!):")
    size = int(input("Please select the pattern size(number of lines):"))
    while 1:
        select_pattern = int(input("select the pattern you want to print(there are 5):"))
        if select_pattern == 1:
            print("Pattern-1:")
            pattern_1(size, character)
        elif select_pattern == 2:
            print("Pattern-2:")
            pattern_2(size, character)
        elif select_pattern == 3:
            print("Pattern-3:")
            pattern_3(size, character)
        elif select_pattern == 4:
            print("Pattern-4:")
            pattern_4(size, character)
        elif select_pattern == 5:
            print("Pattern-5:")
            pattern_5(size, character)
        elif select_pattern == 6:
            print("Pattern-6:")
            pattern_6(size, character)
        else:
            print("Bye! Bye!")
            break