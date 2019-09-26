class HTMLReader:
    def __init__(self):
        self.converter = None

    def parse_html(self, text):
        i = 0
        while i < len(text):
            if text[i] != '<':
                self.converter.convert_character(text[i])
                i += 1
            else:
                tag = ""
                first_close_mark = True
                while text[i] != '>' or first_close_mark:
                    tag += text[i]
                    if text[i] == '>':
                        first_close_mark = False
                    i += 1
                tag += text[i]
                i += 1

                self.converter.convert_tag(tag)

    def show_output(self):
        print(self.converter.get_text())


class TextConverter:
    def __init__(self):
        pass

    def convert_character(self, char):
        pass

    def convert_tag(self, tag):
        pass


class ASCIIConverter(TextConverter):
    """
    Konwertuje tekst na ASCII pozbawiony całkowicie znaczników html.
    """
    def __init__(self):
        super().__init__()
        self.text = ""

    def convert_character(self, char):
        self.text += char

    def convert_tag(self, tag):
        i = 0
        while tag[i] != '>':
            i += 1
        i += 1
        while tag[i] != '<':
            self.text += tag[i]
            i += 1
        while tag[i] != '>':
            i += 1

    def get_text(self):
        return self.text


class ASCIIBigLettersConverter(TextConverter):
    """
    Zmienia tekst na taki, w którym wszystkie znaki objęte znacznikami zostaną zamienione na duże litery,
    a znaki nieobjęte znacznikami na małe.
    """
    def __init__(self):
        super().__init__()
        self.text = ""

    def convert_character(self, char):
        self.text += char.lower()

    def convert_tag(self, tag):
        i = 0
        while tag[i] != '>':
            i += 1
        i += 1
        while tag[i] != '<':
            self.text += tag[i].upper()
            i += 1
        while tag[i] != '>':
            i += 1

    def get_text(self):
        return self.text


class ASCIIBigLettersHTMLConverter(TextConverter):
    """
    Zmienia tekst na taki, w którym wszystkie znaki objęte znacznikami zostaną zamienione na duże litery,
    a znaczniki html pozostaną.
    """
    def __init__(self):
        super().__init__()
        self.text = ""

    def convert_character(self, char):
        self.text += char

    def convert_tag(self, tag):
        i = 0
        while tag[i] != '>':
            self.text += tag[i]
            i += 1
        while tag[i] != '<':
            self.text += tag[i].upper()
            i += 1
        while tag[i] != '>':
            self.text += tag[i]
            i += 1
        self.text += tag[i]

    def get_text(self):
        return self.text


class OtherMarkersConverter(TextConverter):
    """
    Zmienia tekst na taki, w którym wszystkie znaki objęte znacznikami zostaną zamienione następująco:
    <b>X</b> -> {b#X} itd.
    """
    def __init__(self):
        super().__init__()
        self.text = ""

    def convert_character(self, char):
        self.text += char

    def convert_tag(self, tag):
        i = 0
        while tag[i] != '>':
            if tag[i] == '<':
                self.text += '{'
            else:
                self.text += tag[i]
            i += 1
        self.text += '#'
        i += 1
        while tag[i] != '<':
            self.text += tag[i].upper()
            i += 1
        self.text += '}'

    def get_text(self):
        return self.text


class Configurator:
    def __init__(self, converter):
        self.reader = HTMLReader()
        self.reader.converter = converter

    def set_converter(self, converter):
        self.reader.converter = converter


if __name__ == '__main__':

    my_text = "A<b>l</b>a ma <i>k</i>o<u>t</u>a"

    config = Configurator(ASCIIConverter())

    config.reader.parse_html(my_text)
    config.reader.show_output()

    # zmiana konwertera na ASCII + Big Letters

    config.set_converter(ASCIIBigLettersConverter())

    config.reader.parse_html(my_text)
    config.reader.show_output()

    # zmiana konwertera na ASCII + Big Letters + HTML

    config.set_converter(ASCIIBigLettersHTMLConverter())

    config.reader.parse_html(my_text)
    config.reader.show_output()

    # zmiana konwertera na Other Markers

    config.set_converter(OtherMarkersConverter())

    config.reader.parse_html(my_text)
    config.reader.show_output()
