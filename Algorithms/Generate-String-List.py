import FileIO
Text = FileIO.read_text()
CleanText = ''
for letter in Text:
    if letter.isalpha() or letter == ' ':
        CleanText += letter.lower()
    #end if
#next letter
FileIO.output_list(CleanText.split())
