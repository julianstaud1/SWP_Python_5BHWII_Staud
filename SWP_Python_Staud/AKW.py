def outer_function(nachricht, zahl,  *args, **kwargs):
    print(f"Nachricht: {nachricht}")
    print(f"Die Zahl: {zahl}")

    # Innere Methode
    def inner_function():
        print("Innere Funktion:")
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")

    inner_function()

    # Zugriff auf *args
    if args:
        print("Die args:")
        for i, arg in enumerate(args, start=1):
            print(f"  {i}: {arg}")

    # Zugriff auf **kwargs
    if kwargs:
        print("Die kwargs:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")


def main():
    kwargel = {'mo':2,'di':10,'mi':3,'do':4}
    outer_function("Args und kwargs!", 42, 4, "Buchhalter", name="Sepp", alter=62, **kwargel)
    #outer_function(  "hallo sepp", 4 , 3, "beispiel")


if __name__ == "__main__":
    main()
