import os  # provides functions for creating and removing a directory, fetching its contents, changing and identifying
# the current directory, etc. The os is used to interact with the underlying operating system.


def main():
    i = 1
    path = 'C:/Users/chistev/Videos/a/'

    for file in os.listdir(path):
        filename = 'bcs6E' + str(i) + '.mp4'
        source = path + file
        filename = path + filename
        os.rename(source, filename)
        i += 1


main()
