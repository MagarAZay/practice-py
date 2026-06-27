def vowel(sentence):
  count = 0
  vowels ="aeiou"
  for i in sentence:
    if i in vowels:
      count +=1
  return count
print(vowel("abracadabra"))
