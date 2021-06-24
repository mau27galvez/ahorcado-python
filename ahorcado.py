import random

def print_array(array):
    for element in array:
        print(element)


def find_all(array, x):
    indices = []
    n = len(array)

    for i in range(n):
        if array[i] == x:
            indices.append(i)

    return indices


def get_word(array):
    word_index = random.randint(0, len(array))

    return array[word_index]


def check_letter(word, letter, letter_state):
    is_in = letter in word
    letter_state[letter] = True

    return is_in


def get_is_gamme_over(tries):
    if tries >= 6:
        return True
    else:
        return False


def print_art(arts, index):
    print(arts[index])


def print_letters_found(letters, letter_state, main_text):
    for letter in letters:
        if letter_state[letter]:
            indices_found_length = len(find_all(letters, letter))
            indices_found = find_all(letters, letter)

            for i in range(indices_found_length):
                main_text[indices_found[i]] = letter

    print(" ".join(main_text))


def get_dictionary(array):
    current_list  = list(array)
    dictionary = {}

    dictionary = dictionary.fromkeys(current_list, False)

    return dictionary


def get_base_text(word):
    base_text = ["_"] * len(word)
    # base_text_length = len(word)

    # for i in range(base_text_length):
    #     base_text.append("_")

    return base_text



def main():
    is_game_over = False
    tries = 0
    current_word = get_word(words)
    letter_state = get_dictionary(current_word)
    base_text = get_base_text(current_word)

    print(welcome)

    while(not is_game_over):
        print_art(arts, tries)
        print_letters_found(current_word, letter_state, base_text)

        if  "".join(base_text).find("_") == -1:
            print("H A S  G A N A D O")
            exit()

        user_letter = input("Intenta una letra: ")

        is_rigth = check_letter(current_word, user_letter, letter_state)

        if not is_rigth:
            tries += 1

        is_game_over = get_is_gamme_over(tries)

        if is_game_over:
            print_art(arts, tries)
            print("H A Z  P E R D I D O  :(")
            exit()


if __name__ == "__main__":
    arts = [
    """
   _________|
   |        |
 	    |
  	    |
	    | 
	    | 
	    |
	    |============|
    """,
    """
   _________|
   |        |
   0	    |
  	    |
	    | 
	    | 
	    |
	    |============|

    """,
    """
   _________|
   |        |
   0	    |
   |	    |
   |	    | 
	    | 
	    |
	    |============|
    """,
    """
   _________|
   |        |
   0	    |
   |\	    |
   |	    | 
	    | 
	    |
	    |============|
    """,
    """
   _________|
   |        |
   0	    |
  /|\	    |
   |	    | 
	    | 
	    |
	    |============|
    """,
    """
   _________|
   |        |
   0	    |
  /|\	    |
   |	    | 
    \	    | 
	    |
	    |============|
    """,
    """
    
   _________|
   |        |
   0	    |
  /|\	    |
   |	    | 
  / \	    | 
	    |
	    |============|
    """]
    words = ["palabra", "poncho", "tarantula", "animal", "calculadora", "corona", "pintura", "lenguaje", "panatalla"]
    is_game_over = False
    welcome = "B I E N V E N I D @  A  E L  A H O R C A D O"

    main()