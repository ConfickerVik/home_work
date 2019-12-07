from xml.dom import minidom


class CreateXml:

    def create_xml(self, mas):
        doc = minidom.Document()

        # Создание основного тега 'soap:Envelope'
        root = doc.createElement('soap:Envelope')
        root.setAttribute('xmlns:soap', 'http://example.schemas.xmlsoap.org/soap/envelope/')
        doc.appendChild(root)

        # Создание тега 'Body'
        Body = doc.createElement('soap:Body')
        root.appendChild(Body)

        # Создание подтега в тег 'productID'
        productID = doc.createElement(mas[0])
        d = doc.createTextNode('12345')
        productID.appendChild(d)
        Body.appendChild(productID)

        # Создание подтега в тег 'Year'
        Year = doc.createElement(mas[1])
        w = doc.createTextNode('2019')
        Year.appendChild(w)
        Body.appendChild(Year)

        # Создание подтега в тег 'Month'
        Month = doc.createElement(mas[2])
        e = doc.createTextNode('July')
        Month.appendChild(e)
        Body.appendChild(Month)

        xml_str = doc.toprettyxml(indent="  ")

        with open("created_xml.xml", "w") as f:
            f.write(xml_str)
