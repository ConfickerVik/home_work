class OriginalProgram:
    FileProgram = ""

    def getFile(self):
        pass

    def setFile(self, PathFile):
        pass


class Reader:

    def readFile(self, FileProgram):
        pass

    def startAnalysis(self, BufferProgram):
        pass


class Lexer:
    TableLex = lambda: TableLexems()
    TableId = lambda: TableIdentifier()
    Errors = lambda: Error()

    def lexAnalysis(self):
        pass


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
        pass

    def addTriad(self):
        pass


class DSR:
    ListDSR = ""

    def getDSR(self):
        pass

    def setDSR(self):
        pass

    def addDSR(self):
        pass


class GenerationCode():
    Triads = lambda: Triads
    DSR = lambda: DSR

    def generate(self):
        pass
