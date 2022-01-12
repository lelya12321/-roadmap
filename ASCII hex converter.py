class Converter():
    @staticmethod
    def to_ascii(h):
        import codecs
        return codecs.decode(h, 'hex').decode('utf-8')

    @staticmethod
    def to_hex(s):
        return s.encode('utf-8').hex()
