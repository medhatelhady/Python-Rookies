def n_letter(text, letter, n):
    length = len(text)
    remainder = n % length
    i = n //length
    return text.count(letter) * i + text.count(letter,0,remainder)
    
