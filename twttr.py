def main():
    Input = input("Input: ")
    print(shorten(Input))


def shorten(word):
    vowel = "AEIOUaeiou"
    return "".join([char for char in word if char not in vowel])

                  
if __name__ == "__main__":
    main()