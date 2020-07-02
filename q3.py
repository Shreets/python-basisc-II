# 3. Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

para = 'I scared away rats with my bat . Thank god the dog chased away a cat sitting on my arts based on a star'
word_list = para.split()
print(word_list)
sort_words = []
anagrams = {}
for word in word_list:
    word.split()
    word = ''.join(sorted(word))
    sort_words.append(word)

for i in range(len(sort_words)):
    anagram=[]
    for j in range(len(sort_words)):
        if i == j:
            continue
        if sort_words[i] == sort_words[j]:
            anagram.append(word_list[j])
    anagrams[word_list[i]] = anagram

print(anagrams)
