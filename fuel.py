def main():
    fraction = get_value()
    if fraction == 100:
        print("F")
    elif fraction == 0:
        print("E")
    else:
         print(fraction,"%",sep="")


def get_value():
    while True:
        try:
            c =   input("Fraction: ")
            x ,y = c.split("/")
            x = int(x)
            y = int(y)
            if x > 4 or y > 4:
                continue
            if y == 0:
                continue
            div = (x /y)*100
            return round(div)
        

        except ValueError:
            pass

        except ZeroDivisionError:
            pass


if __name__ == "__main__":
    main()
