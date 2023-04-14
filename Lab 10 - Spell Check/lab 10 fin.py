import re

import arcade.color


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)
def linear_search (aiw, dictionary_list):
    # --- Linear search
    current_list_position = 0
    for line in aiw:
        line = line.strip()
        current_list_position += 1
        for word in split_line(line):
            if word.upper() not in dictionary_list:
                print("line", current_list_position, "wrong: ", word)

def binary_search (aiw_list, dictionary_list):
    current_list_postion = 0
    for line in aiw_list:
        current_list_postion +=1
        for word in split_line(line):
            lower_bound = 0
            upper_bound = len(aiw_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:

                middle_pos = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("Line:", current_list_postion, "wrong:", word)

def main():
    dictionary_words = open("dictionary.txt")
    dictionary_list = []
    for line in dictionary_words:
        line = line.strip()
        dictionary_list.append(line)

    aiw = open("AliceInWonderLand200.txt")
    aiw_list = []
    for line in aiw:
        line = line.strip()
        aiw_list.append(line)

    print("-~- Linear Search -~-")
    linear_search(aiw_list, dictionary_list)
    print("--- Binary Search ---")
    binary_search(aiw_list, dictionary_list)

main()


