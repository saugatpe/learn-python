import emoji

def main():
    # Prompt the user for a string that may contain emoji codes or aliases
    user_input = input("Input: ")
    
    # Convert the input string into the corresponding emojis
    emojized_output = emoji.emojize(user_input, language='alias')
    
    # Print the emojized string
    print("Output:", emojized_output)

if __name__ == "__main__":
    main()
