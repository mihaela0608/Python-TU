def reading(name):
    try:
        f = open(name)
        f.read()
    except:
        print("There is no such file")
    else:
        return f.name
    finally:
        print("The file has been closed")
reading("errorEx")