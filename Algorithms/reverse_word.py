def rec_rev(word):
    if len(word)>0: return rec_rev(word[1:])+word[0]
    else: return word
    
print(rec_rev(input()))
