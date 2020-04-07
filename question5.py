from test import test

def count_words(words):
    count = 0
    for word in words:
        count += 1
        if(word == "sam"):
            break
    return count


def test_suite():
    test(count_words(["asdas", "aiusdui", "sam", "ouoisau", "jhsad"]) == 3)
    test(count_words(["asdas", "aiusdui", "ouoisau", "jhsad"]) == 4)
    test(count_words([]) == 0)
    test(count_words(["sam", "ouoisau", "jhsad"]) == 1)
    test(count_words(["asdas"]) == 1)

test_suite()