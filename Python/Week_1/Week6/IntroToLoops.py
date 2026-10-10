prompt = input("Do you want to print the list?Y/N ")
geniuses = ["Jayden", "Dayyon", "Jahlil", "Michael", "TC"]

while (prompt == "Y"):
    for genius in geniuses:
        print(genius)
    prompt = input("Do you want to print the list again? Y/N ")