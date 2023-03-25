import sys
from itertools import permutations, combinations

# LOAD CSV INTO MAP 
with open("words_alpha.txt", "r") as dict_h:
    dictlines = dict_h.read()  
    dictlines_list = dictlines.lower().split("\n")


def main():
    print("The Super Descrambler!")
    print("By Saif and Faaris Ahmed")

    if len(sys.argv) > 1:
        inword = sys.argv[1].lower()
        print(f"You want to descramble the word: {inword}")
        if inword in dictlines_list:
            print(f"{inword} is already a real word")
        
        combos = [''.join(p).lower() for p in permutations(inword)]
        for c in combos:
            if c in dictlines_list:
                print(f"\tPossible descramble of << {inword} >> is << {c} >>")

    else:
        print("You have to give input on the command line, duh!")

if __name__ == '__main__':
    main()