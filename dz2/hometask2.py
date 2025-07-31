def encriptor():
    user_input = str(input("Enter text on russian: ") + " ")
    encript = { #а, е, ё, и, о, у, ы, э, ю, я
        "а":"е",
        "е":"ё",
        "ё":"и",
        "и":"о",
        "о":"у",
        "у":"ы",
        "ы":"э",
        "э":"ю",
        "ю":"я",
        "я":"а",
    }
                              
    user_input_enc = "".join(encript.get(c, c) for c in user_input) #   how to do it with this?  [ch for ch in user_input if (encript[ch]) ch is encript[ch]] 
    print(user_input_enc)                                             
    return None

def statistics():
    user_text = str(input("Input text : "))
    user_text = user_text.lower()

    frequency_letter = dict()
    unique_word = set()
    longest = ""
    def letter_frequency():
        for ch in user_text:
            if ch not in frequency_letter:
                frequency_letter[ch] = 1
            else:
                frequency_letter[ch] += 1
        return None
    def word_unique(u_text):
        possible_symbols_to_remove = [',', '.', '!', '-', '(', ')']
        for ch in possible_symbols_to_remove:
            text = "".join(u_text.replace(ch,''))         #if i write "user_text = user_text.replace(ch,"")", it stops recognizing user_text
            u_text = text
        word_list = list()
        word_list = text.split()

        unique_word.update(word_list)
        return None
    def longest_word(lo):
        lo = sorted(unique_word, key = len)[-1]    
        return lo                                  
    
    letter_frequency()
    word_unique(user_text)
    longest = longest_word(longest)

    print("Unique words : {}.\nLongest word : {}.\nLetter frequency : {}".format(unique_word,longest,frequency_letter))
    return None

def cleanup():
    to_format = [
    "  Иван Иванов  ", 
    "Петров;Петр ", 
    "Сидорова Анна ",           #logic for recognizing last names and first names ???
    "  ОЛЕГ КУЗНЕЦОВ  ",        # I'll just do it so shorter name goes first
    "МАРИЯ; ТРОФИМОВА"          # but my guess would be to make whole list of possible name and last name
    ]                           
    formatted = list()
    garbage = (';',':',',','.')

    for words in to_format:
        for g in garbage:
            if g in words:
                words = words.replace(g,' ')
        
        words = words.strip()
        words = words.lower()

        word = words.split()
        temp = list()
        for w in word:
            w = w[0].upper() + w[1:len(w)]
            temp.append(w)
        word = temp
        word.sort(key = len)
        words = word[0] + " " + word[1]
        formatted.append(words)
            
    print(formatted)

    return None


menu = {
    '1':encriptor,
    '2':statistics,
    '3':cleanup
}

func_call = str(input("Type what task you want to check.\nType '1' for encription.\nType '2' for text statistics.\nType '3' for data clean up.\n"))

while func_call == '1' or func_call == '2' or func_call == '3':
    menu[func_call]()
    func_call = str(input("Type what task you want to check.\nType '1' for encription.\nType '2' for text statistics.\nType '3' for data clean up.\n"))
