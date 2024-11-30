from collections import Counter

def main():
    bookPath = 'books/frankenstein.txt'
    print(f'--- Begin report of {bookPath} ---')
    text = get_book_path(bookPath)
    word_count = count_words(text)
    print(f'{word_count} words found in the document')
    characterDict = count_characters(text)
    for key, value in characterDict.items():
        print(f'The \'{key}\' character was found {value} times')
    print('--- End report ---')

def get_book_path(path):
    with open(path) as f:
        return f.read()
def count_words(words):
    words = words.split()
    return len(words)
def count_characters(text):
    lowered_string = text.lower()
    char_dict = Counter(lowered_string)
    counter_dict = dict(char_dict)
    return counter_dict


    
main()