from xml.dom.minidom import parse
import xml.dom.minidom


class DOMParser:
    def startDom(self, path_file_xml):
        DOMTree = xml.dom.minidom.parse(path_file_xml)
        collection = DOMTree.documentElement

        tariffs = collection.getElementsByTagName("Name")

        for tariff in tariffs:
            print("*" * 35)
            if tariff.hasAttribute("name"):
                print("Tariff title: %s" % tariff.getAttribute("name"))

            OperatorName = tariff.getElementsByTagName('OperatorName')[0]
            print("OperatorName: %s" % OperatorName.childNodes[0].data)
            Payroll = tariff.getElementsByTagName('Payroll')[0]
            print("Payroll: %s" % Payroll.childNodes[0].data)
        #    CallPrices = tariff.getElementsByTagName('CallPrices')[0]
        #    print("CallPrices: %s" % CallPrices.childNodes[0].data)
            Inside = tariff.getElementsByTagName('Inside')[0]
            print("Inside: %s" % Inside.childNodes[0].data)
            Outside = tariff.getElementsByTagName('Outside')[0]
            print("Outside: %s" % Outside.childNodes[0].data)
            Stationary = tariff.getElementsByTagName('Stationary')[0]
            print("Stationary: %s" % Stationary.childNodes[0].data)
            SMSPrice = tariff.getElementsByTagName('SMSPrice')[0]
            print("SMSPrice: %s" % SMSPrice.childNodes[0].data)
        #    Parametrs = tariff.getElementsByTagName('Parametrs')[0]
        #    print("Parametrs: %s" % Parametrs.childNodes[0].data)
            FavoriteNumber = tariff.getElementsByTagName('FavoriteNumber')[0]
            print("FavoriteNumber: %s" % FavoriteNumber.childNodes[0].data)
            Tariffication = tariff.getElementsByTagName('Tariffication')[0]
            print("Tariffication: %s" % Tariffication.childNodes[0].data)
            TarrifConnectionFee = tariff.getElementsByTagName('TarrifConnectionFee')[0]
            print("TarrifConnectionFee: %s" % TarrifConnectionFee.childNodes[0].data)
        print("*" * 35)
