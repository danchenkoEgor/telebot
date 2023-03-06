
d = {"А" : "A", "Б" : "B", "В" : "V", "Г" : "G",\
      "Д" : "D", "Е" : "E", "Ё" : "E",\
      "Ж" : "ZH", "З" : "Z", "И" : "I", "Й" : "I",\
      "К" : "K", "Л" : "L", "М" : "M", "Н" : "N",\
      "О" : "O", "П" : "P", "Р" : "R", "С" : "S",\
      "Т" : "T", "У" : "U", "Ф" : "F", "Х" : "KH",\
      "Ц" : "TS", "Ч" : "CH", "Ш" : "SH", "Щ" : "SHCH",\
      "Ы" : "Y", "Ъ" : "IE", "Э" : "E", "Ю" : "IU", "Я" : "IA", "Ь" : ""} 


def translator(string):
    for word, initial in d.items():
      string = string.replace(word, initial)
    return string 


