def main():
    import check_input
    import random


    def generate_code():
        usable_numbers = [1, 2, 3, 4, 5, 6]
        code = random.shuffle(usable_numbers)
        code = usable_numbers[:4]

        print("debug; computer code:", code)
        return code


    def get_guess():
        user_input = []
        while len(user_input) < 4:
            user_digit = check_input.get_int_range("Digits: ", 1, 6)
            if user_digit in user_input:
                print("Duplicate digit")
                continue
            user_input.append(user_digit)

        print("debug; my code:", user_input)
        return user_input


    def check_guess(code, guess):
        exact = 0
        mismatched = 0
        for i in range(len(guess)):
            print(i)
            user_current = guess[i]
            if i == code[i]:
                exact += 1
            elif user_current in code:
                mismatched += 1

        print([exact, mismatched])
        return [exact, mismatched]


    def display_results(results):
        display = f"Exact matches: {results[0]}\nMisplaced matches: {results[1]}"
        return display


    print("\n--Code Breaker!--\n" \
    "Crack the 4-digit code within 8 attempts to open the safe.\n" \
    "Each digit is between 1-6.\n")
    check_guess(generate_code(), get_guess())

main()