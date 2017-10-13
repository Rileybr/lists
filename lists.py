# Word, Line, and Character Counter By Brandon Riley
# 10/13/17
# Counts words, lines, and characters in a given document


def main():
    characters = 0
    words = 0
    my_file = open("sample.txt", "r")   # imports the file we are using
    file_contents = my_file.readlines()
    my_file.close()
    print("Lines:", len(file_contents))   # finds the number of lines
    for y in file_contents:  # finds the number of words
        words += len(y.split())
    print("Words:", words)
    for x in file_contents:  # finds the number of characters
        characters += len(x)
    print("Characters:", characters)


main()
