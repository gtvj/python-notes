def main():
    f = open('README.md')
    for line in f:
        print(line.rstrip())


if __name__ == '__main__':
    main()
