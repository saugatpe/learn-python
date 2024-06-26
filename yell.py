def main():
    yell(["this","is","cs50"])

def yell(*words):
    uppercase = [word.upper() for word in words]
    print(uppercase)

if __name__ == "__main__":
    main()