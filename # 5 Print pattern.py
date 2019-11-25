# 5 Print pattern


def show_stars(rows):
    a = "*"
    for i in range(int(rows)):
        print(a)
        a+="*"
    return

show_stars((input("Enter the number of rows: ")))