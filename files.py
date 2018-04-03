def main():
    input_file = open('README.md', 'rt')  # Open the file in 'read' and 'text' mode
    output_file = open('README-copy.md', 'wt')  # Open or create
    for line in input_file:
        print(line.rstrip(), file=output_file)  # Note: we're using print here but passing an output file
        print('.', end='', flush=True)  # Printing to standard out
    output_file.close()
    print('\ndone')


if __name__ == '__main__':
    main()
