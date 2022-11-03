import re

class HovercraftFullOfEels(Exception):
    pass

class Gruszczyk_Not_Defined(Exception):
    pass

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email: str) -> bool:
    if re.fullmatch(regex, email):
      return True
    else:
        raise Gruszczyk_Not_Defined("W moim bucie jest waz")
      #raise HovercraftFullOfEels("My hovercraft is full of eels")

def test_isValid():
    assert isValid("name.surname@gmail.com")
    assert isValid("anonymous123@yahoo.co.uk")
    assert isValid("anonymous123@...uk")
    assert isValid("...@domain.us")

if __name__ == "__main__":
    #test_isValid()
    isValid("name.surname@gmail.com")
    isValid("anonymous123@yahoo.co.uk")
    isValid("anonymous123@...uk")
    isValid("...@domain.us")

