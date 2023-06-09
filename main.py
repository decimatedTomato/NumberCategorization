import AliquotSequence

def main():
    print("Let's start analyzing numbers!")
    try:
        while True:
            user_input = input("Number to analyze: ")
            if user_input in ["q", "quit", "exit"]:
                break
            test_value = None
            try:
                test_value = int(user_input)
            except ValueError:
                print(f"<{user_input}> is not a number, try again?")
                continue

            test_aliquot_property = AliquotSequence.aliquot_property(test_value)
            if test_aliquot_property != None:
                print(f"Aliquot sequence property of {test_value} is {test_aliquot_property}")
            else:
                print(f"{test_value} has no discernible aliquot property")
            print(f"Aliquot sequence starting at {test_value} is:\n{AliquotSequence.aliquot_sequence(test_value)}")
    except KeyboardInterrupt:
        pass
    print("Enough analyzing for now. Good bye :]")

if __name__ == "__main__":
    main()