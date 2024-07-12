alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(text, shift):
#   newStr = ""
#   for letter in text:
#     if letter not in alphabet:
#       newStr += letter
#     else:
#       oldIdx = alphabet.index(letter)
#       newStr += alphabet[(oldIdx + shift) % 26]
#   print(f"The encoded text is {newStr}")

# def decrypt(text, shift):
#   newStr = ""
#   for letter in text:
#     if letter not in alphabet:
#       newStr += letter
#     else:
#       oldIdx = alphabet.index(letter)
#       newStr += alphabet[(oldIdx - shift)]
#   print(f"The encoded text is {newStr}")

# if direction == "encode":
#   encrypt(text,shift)
# elif direction == "decode":
#   decrypt(text, shift)

def caesar(text, shift, direction):
  newStr = ""
  for letter in text:
    if letter not in alphabet:
      newStr += letter
    else:
      oldIdx = alphabet.index(letter)
      if direction == "encode":
        newIdx = (oldIdx + shift) % 26
      elif direction == "decode":
        newIdx = oldIdx - shift
      newStr += alphabet[newIdx]
  print(f"The encoded text is {newStr}")

caesar(text, shift, direction)