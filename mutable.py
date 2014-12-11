class Translator(object):
    def __init__(self, trans={}):
        self.trans = trans

spa = Translator()
spa.trans["hello"] = "hola"

port = Translator()
port.trans["hello"] = "oi"

print "'hello' in portuguese is", port.trans["hello"]
print "'hello' in spanish is",    spa.trans["hello"]
