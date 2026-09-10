import check_input
import random

def generate_code():
        usable_numbers = [1, 2, 3, 4, 5, 6]
        code = random.shuffle(usable_numbers)
        code = usable_numbers[:4]

        print("DEBUG computer code:", code) # FIXME debug

        return code



def get_guess():
        user_input = []
        while len(user_input) < 4:
            user_digit = check_input.get_int_range("Digit: ", 1, 6)
            if user_digit in user_input:
                print("Duplicate digit")
                continue
            user_input.append(user_digit)

        print("DEBUG my code:", user_input) # FIXME debug

        return user_input



def check_guess(code, guess): 
        exact = 0
        mismatched = 0
        for i in range(len(guess)):
            user_current = guess[i]
            if guess[i] == code[i]:
                print(f"DEBUG match user guess is {i} actual code is {code[i]}") # FIXME debug
                exact += 1
            elif user_current in code:
                print(f"DEBUG mismatch user guess is {i} actual code is {code[i]}") # FIXME debug
                mismatched += 1

        stats = [exact, mismatched]
        return stats



def display_results(results):
        verdict = results
        print("\nResults:")
        print(f"Exact matches: {verdict[0]}")
        print(f"Misplaced matches: {verdict[1]}\n")
        


def main():
    print("\n--Code Breaker!--\n" \
    "Crack the 4-digit code within 8 attempts to open the safe.\n" \
    "Each digit is between 1-6.\n")

    attempts = 0
    while attempts <= 8:
        verdict = check_guess(generate_code(), get_guess())
        display_results(verdict)
        if verdict[0] == 4:
             print("Victory.")
             break
        attempts += 1

main()