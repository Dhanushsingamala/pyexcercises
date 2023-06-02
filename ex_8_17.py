def lines_to_paragraphs(lines):
    #intialising empty list 
    paragraphs = []
    current_paragraph = []

    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace

        if line:  # If line is not empty
            current_paragraph.append(line)
        elif current_paragraph:  # If line is empty and there is content in current_paragraph
            paragraph = ' '.join(current_paragraph)  # Join the lines with a space separator
            paragraphs.append(paragraph)
            current_paragraph = []  # Reset current_paragraph

    if current_paragraph:  # Add the last paragraph if it exists
        paragraph = ' '.join(current_paragraph)
        paragraphs.append(paragraph)

    return paragraphs


# Example lines with your name "Dhanush Reddy"
lines = [
    "Hello,",
    "My name is Dhanush Reddy.",
    "I am a software engineer.",
    "",
    "I love coding and learning new technologies.",
    "Dhanush Reddy is my full name.",
    "Thank you!",
]

paragraphs = lines_to_paragraphs(lines)

# Print the paragraphs
count = 1
for paragraph in paragraphs:
    print(f'paragraph:{count}')
    print(paragraph)
    print()
    count += 1
