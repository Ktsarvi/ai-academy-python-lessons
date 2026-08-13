works = input("Does the thing work? (yes/no): ").lower()

if works == "yes":
    print("DON'T MESS WITH IT!")
    print("NO PROBLEM!")
else:
    broke_it = input("Did you break it? (yes/no): ").lower()

    if broke_it == "yes":
        anyone_knows = input("Does anyone know? (yes/no): ").lower()

        if anyone_knows == "no":
            print("HIDE IT!")
            print("NO PROBLEM!")
        else:
            blame = input("Can you blame someone else? (yes/no): ").lower()

            if blame == "yes":
                print("NO PROBLEM!")
            else:
                print("SORRY TO HEAR THAT!")
    else:
        trouble = input("Will you be in trouble? (yes/no): ").lower()

        if trouble == "yes":
            blame = input("Can you blame someone else? (yes/no): ").lower()

            if blame == "yes":
                print("NO PROBLEM!")
            else:
                print("SORRY TO HEAR THAT!")
        else:
            print("THROW IT AWAY")
            print("NO PROBLEM!")