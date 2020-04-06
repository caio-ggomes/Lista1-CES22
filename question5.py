def count_words(words):
    count = 0
    for word in words:
        count += 1
        if(word == "sam"):
            break
    return count

words = ["asd", "asfer", "aresvds", "sam", "fwesofj", "auibsodu"]
print(count_words(words))