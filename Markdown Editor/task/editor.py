# write your code here
commands = "plain bold italic header link inline-code ordered-list unordered-list new-line"
markdown_text = str()


def plain_formatter():
    return input("Text: ")


def bold_formatter():
    return f"**{input('Text: ')}**"


def italic_formatter():
    return f"*{input('Text: ')}*"


def header_formatter():
    while True:
        level = int(input("Level: "))
        if level < 1 or level > 6:
            print("The level should be within the range of 1 to 6")
        else:
            return f"{'#' * level} {input('Text: ')}\n"


def link_formatter():
    return f"[{input('Label: ')}]({input('URL: ')})"


def inline_code_formatter():
    return f"`{input('Text: ')}`"


def new_line_formatter():
    return "\n"


def list_formatter():
    row_text = list()
    while True:
        num_of_rows = int(input("Number of rows: "))
        if num_of_rows <= 0:
            print("The number of rows should be greater than zero")
            continue
        else:
            for rows in range(num_of_rows):
                row_text.append(input(f"Row #{rows + 1}: "))

        return row_text


while True:
    user_input = input("Choose a formatter: ")
    if user_input == "!done":
        with open("output.md", "w", encoding="UTF-8") as f:
            f.write(markdown_text)
        break
    elif user_input == "!help":
        print(f"""Available formatters: {commands}\nSpecial commands: !help !done""")
        continue
    elif user_input in commands:
        if user_input == "plain":
            markdown_text += plain_formatter()
        elif user_input == "bold":
            markdown_text += bold_formatter()
        elif user_input == "italic":
            markdown_text += italic_formatter()
        elif user_input == "header":
            markdown_text += header_formatter()
        elif user_input == "link":
            markdown_text += link_formatter()
        elif user_input == "inline-code":
            markdown_text += inline_code_formatter()
        elif user_input == "unordered-list":
            help_list = list_formatter()
            for i in range(len(help_list)):
                markdown_text += f"* {help_list[i]}\n"
        elif user_input == "ordered-list":
            help_list = list_formatter()
            for i in range(len(help_list)):
                markdown_text += f"{i + 1}. {help_list[i]}\n"
        else:
            markdown_text += new_line_formatter()
    else:
        print("Unknown formatting type or command")
        continue
    print(markdown_text)

