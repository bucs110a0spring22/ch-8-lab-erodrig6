class StringUtility:
  def __init__(self, string):
    self.string = string
  def __str__(self):
    return self.string
  
  
  def vowels(self):
    count = 0
    vowels = ['a', 'e', 'i' 'o' 'u' 'A' 'E' 'I' 'O' 'U']
    vowelString = str(self)
    for vowel in vowels:
      for letters in vowelString:
        if letters in vowel:
          count = count + 1
    if count < 5:
      return str(count)
    else:
      return 'many'

  def bothEnds(self):
    bothEndsString = str(self)
    if len(bothEndsString) < 3:
      return ''
    else:
      return bothEndsString[0] + bothEndsString[1] + bothEndsString[-2] + bothEndsString[-1]
  
  def fixStart(self):
    fixStartString = str(self)
    returnString = ''
    if len(fixStartString) < 2:
      return fixStartString
    else:
      i = 0
      replaceChar = fixStartString[0]
      for letters in fixStartString:
        if letters == replaceChar and i != 0:
          returnString = returnString + '*'
        else:
          returnString = returnString + letters
        i = i + 1
    return returnString
          
  def asciiSum(self):
    asciiSumString = str(self)
    asciiSum = 0
    for letters in asciiSumString:
      asciiSum = asciiSum + ord(letters)
    return asciiSum
  
  def cipher(self):
    cipherString = str(self)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    phrase = cipherString
    ciphed = ""
    space = " "
    for character in phrase:
      if character in letters.lower():
        newletters = chr(((ord(character) + len(phrase) - 97) % 26) + 97)
        ciphed += newletters
      elif character in letters.upper():
        newletters = chr(((ord(character) + len(phrase) - 65) % 26) + 65)  
        ciphed += newletters
      elif character in space: 
        ciphed += character 
    return ciphed
      
          
    
 


  
  
  
