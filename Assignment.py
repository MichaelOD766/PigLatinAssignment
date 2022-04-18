
def pig_latin():
    sentence = input("Sentence: ")
    words = sentence.split()

    for i, word in enumerate(words) :
        """
        if first letter is vowel, if yes concatinate 'way'
        """
        if word[0] in "AEIOUaeiou":
            words[i] = words[i] + "way"
        else:
            """
            get a vowel position and fix all consonants before the 
            vowel with 'ay' at the end
            """
            hasVowel = False

            for j, letter in enumerate(word):
                if letter in "AEIOUaeiou":
                    words[i] = word[j:] + word[:j] + "ay"
                    hasVowel = True
                    break
# If it doesn't have a vowel then add 'ay' to end
            if (hasVowel ==  False):
                words[i] = words[i] + "ay"

    
    output = " ".join(words)
    print(output.capitalize())


pig_latin()