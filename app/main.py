import sys

tokens = {}
tokens = {"(" : "LEFT_PAREN",
          ")" : "RIGHT_PAREN"}

def tokenize(file_contents):
    for ch in file_contents:
        if ch in tokens:
            print(f"{tokens[ch]} {ch} null")
    print("EOF  null")

def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!", file=sys.stderr)

    if file_contents:
        tokenize(file_contents)
    else:
        print("EOF  null") # Placeholder, replace this line when implementing the scanner


if __name__ == "__main__":
    main()
