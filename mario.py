def main():
    height = int(input("enter the heoght: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)


if __name__ == "__main__":
    main()