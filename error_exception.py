if __name__ == '__main__':
    fh = None
    try:
        fh = open("testfile", "r")
        fh.write("This is my test file for exception handling!!")
    except IOError as e:
        print("Error: can\'t find file or read data - " + str(e))
    else:
        print("Written content in the file successfully")
    finally:
        fh.close()



