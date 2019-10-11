import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.OperatorName = ""
        self.Payroll = ""
#        self.CallPrices = ""
        self.Inside = ""
        self.Outside = ""
        self.Stationary = ""
        self.SMSPrice = ""
#        self.Parametrs = ""
        self.FavoriteNumber = ""
        self.Tariffication = ""
        self.TarrifConnectionFee = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "Name":
            print("*" * 35)
            title = attributes["name"]
            print("Tariff title:", title)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "OperatorName":
            print("OperatorName:", self.OperatorName)
        elif self.CurrentData == "Payroll":
            print("Payroll:", self.Payroll)
#        elif self.CurrentData == "CallPrices":
#            print("CallPrices:", self.CallPrices)
        elif self.CurrentData == "Inside":
            print("Inside:", self.Inside)
        elif self.CurrentData == "Outside":
            print("Outside:", self.Outside)
        elif self.CurrentData == "Stationary":
            print("Stationary:", self.Stationary)
        elif self.CurrentData == "SMSPrice":
            print("SMSPrice:", self.SMSPrice)
#        elif self.CurrentData == "Parametrs":
#            print("Parametrs:", self.Parametrs)
        elif self.CurrentData == "FavoriteNumber":
            print("FavoriteNumber:", self.FavoriteNumber)
        elif self.CurrentData == "Tariffication":
            print("Tariffication:", self.Tariffication)
        elif self.CurrentData == "TarrifConnectionFee":
            print("TarrifConnectionFee:", self.TarrifConnectionFee)
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "OperatorName":
            self.OperatorName = content
        elif self.CurrentData == "Payroll":
            self.Payroll = content
#        elif self.CurrentData == "CallPrices":
#            self.CallPrices = content
        elif self.CurrentData == "Inside":
            self.Inside = content
        elif self.CurrentData == "Outside":
            self.Outside = content
        elif self.CurrentData == "Stationary":
            self.Stationary = content
        elif self.CurrentData == "SMSPrice":
            self.SMSPrice = content
#        elif self.CurrentData == "Parametrs":
#            self.Parametrs = content
        elif self.CurrentData == "FavoriteNumber":
            self.FavoriteNumber = content
        elif self.CurrentData == "Tariffication":
            self.Tariffication = content
        elif self.CurrentData == "TarrifConnectionFee":
            self.TarrifConnectionFee = content


class SAXParser:
    def startSax(self, path_file_xml):
        # create an XMLReader
        parser = xml.sax.make_parser()

        # override the default ContextHandler
        handler = MovieHandler()
        parser.setContentHandler(handler)

        parser.parse(path_file_xml)
        print("*" * 35)
