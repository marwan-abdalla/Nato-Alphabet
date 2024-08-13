import pandas as pd


def nato_dictionary():
    # Read the CSV file into a DataFrame
    alphabet_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")
    # Create the dictionary from the DataFrame
    nato_dict = {row["letter"]: row["code"] for index, row in alphabet_data_frame.iterrows()}
    # Asks user to input a sentence
    user_input = input("Please type a sentence: ").upper()
    # Converts the input sentence into NATO phonetic alphabet words
    nato_dict = [nato_dict[letter] for letter in user_input]

    return nato_dict


def main():

    """
    Main function to run the NATO phonetic alphabet conversion program.

    """
    continue_using = True

    while continue_using:
        user_decision = input("Would you like to input a sentence? Type 'Y' or 'N': ")
        if user_decision.upper() == 'Y':
            print(nato_dictionary())
        elif user_decision.upper() == 'N':
            continue_using = False
        else:
            print("Invalid input, Please Type 'Y' or 'N'.")


main()
