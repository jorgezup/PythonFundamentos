'''text = str(input()).strip()
for letter in text:
        especiais =[]
        for i in range (32,126):
            especiais.append(chr(i))
        if letter in especiais:
            print(letter)
        else:
            print("Não tem")'''


class UniqueChars(object):

    def has_unique_chars(self, string):
        for letter in text:
            especiais = []
            for i in range(32, 126):
                especiais.append(chr(i))
            if letter in especiais:
                return True
            else:
                return False


text = str(input()).strip()
a = UniqueChars()
a.has_unique_chars(text)


