def main():
    z = get_int("z: ")
    print(f"z is {z}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
           pass




if __name__ == "__main__":
    main()