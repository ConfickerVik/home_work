class OriginalProgram:
    FileProgram = ""

    def getFile(self):
        pass

    def setFile(self, PathFile):
        print("Получили файл!\n")


class Reader:

    def readFile(self, FileProgram):
        print("Прочитали текст!\n")

    def startAnalysis(self, BufferProgram):
        pass


class Lexer:
    TableLex = lambda: TableLexems()
    TableId = lambda: TableIdentifier()
    Errors = lambda: Error()

    def lexAnalysis(self):
        print("Получили таблицу лексем, вывели!\n")
        print("Получили таблицу индентификаторов, вывели!\n")


class Parser:
    Table = lambda: TableIdentifier()
    Errors = lambda: Error()

    def parsing(self):
        pass


class SemanticAnalizer:
    Table = lambda: TableIdentifier()
    Errors = lambda: Error()

    def semanticAnalysis(self):
        pass


class Error:
    ErrorList = ""

    def getErrorList(self):
        pass

    def setErrorList(self, ErrorList):
        pass

    def addError(self, Error):
        pass


class TableLexems:
    LexemList = ""

    def getTable(self):
        pass

    def setTable(self, Table):
        pass

    def addLexem(self, Lexem):
        pass


class TableIdentifier:
    IdentifierList = ""

    def getTable(self):
        pass

    def setTable(self, HashList):
        pass

    def addIdentifier(self, Iden):
        pass


class PrepareGeneration:
    Errors = lambda: Error()

    def createTriads(self):
        pass

    def createDSR(self):
        pass

    def beginGeneration(self):
        pass


class Triads:
    TriadsList = ""

    def getList(self):
        pass

    def setList(self):
        print("Получили список триад, вывели!\n")

    def addTriad(self):
        pass


class DSR:
    ListDSR = ""

    def getDSR(self):
        pass

    def setDSR(self):
        print("Получили дерево синтаксического разбора, вывели!\n")

    def addDSR(self):
        pass


class GenerationCode():
    Triads = lambda: Triads
    DSR = lambda: DSR

    def generate(self):
        print("Получили объектный код, вывели!\n")


if __name__ == '__main__':
    objOP = OriginalProgram()
    objOP.setFile(" ")
    objR = Reader()
    objR.readFile(" ")
    objL = Lexer()
    objL.lexAnalysis()
    objT = Triads()
    objT.setList()
    objD = DSR()
    objD.setDSR()
    objGC = GenerationCode()
    objGC.generate()
