'''
# Group 4
# Brian Higgins, Conner Lajoie
# Number guessing game; the computer randomly generates a four-integer list, and player has to create a list which perfectly matches it. If they fail 8 times, they're out.
'''

import check_input
import random


def generate_code():
        """
        Randomly shuffles a list of allowed integers, then makes another list using the first four integers of the randomized list.
        """
        usable_numbers = [1, 2, 3, 4, 5, 6]
        code = random.shuffle(usable_numbers)
        code = usable_numbers[:4]

        return code



def get_guess():
        """
        Gets and validates user input and adds it to a list
        """
        user_input = []
        while len(user_input) < 4:
            user_digit = check_input.get_int_range("Enter digit: ", 1, 6)
            if user_digit in user_input:
                print("Duplicate digit")
                continue
            user_input.append(user_digit)

        return user_input



def check_guess(code, guess): 
        """
        Compares user input to shuffled list, then creates list showing matches and mistmatches
        """
        exact = 0
        mismatched = 0
        for i in range(len(guess)):
            user_current = guess[i]
            if guess[i] == code[i]:
                exact += 1
            elif user_current in code:
                mismatched += 1

        stats = [exact, mismatched]
        return stats



def display_results(results):
        """
        displays match-mismatch list
        """
        verdict = results
        print("\nResults:")
        print(f"Exact matches: {verdict[0]}")
        print(f"Misplaced matches: {verdict[1]}\n")
        


def main():
    print("\n--Code Breaker!--\n" \
    "Crack the 4-digit code within 8 attempts to open the safe.\n" \
    "Each digit is between 1-6.\n")

    attempts = 0
    correct_answer = generate_code()

    while attempts < 8:
        user_answer = get_guess()
        verdict = check_guess(correct_answer, user_answer)
        print(f"\nYour guess: {user_answer}")
        display_results(verdict)
        if verdict[0] == 4:
             print("Victory.")
             break

        attempts += 1
        print(f"{8 - attempts} attempts left.")

    print(f"The code was {correct_answer}")
    print("All attempts exhausted. Failure.")
main()