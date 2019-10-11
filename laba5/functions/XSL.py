import lxml.etree as ET


class XSLhtml:
    def translate(self, path_file_xml, path_file_xsl):
        dom = ET.parse(path_file_xml)
        xslt = ET.parse(path_file_xsl)
        transform = ET.XSLT(xslt)
        newdom = transform(dom)

        with open("html.html", "w") as file:
            file.write((ET.tostring(newdom, pretty_print=True)).decode("UTF-8"))
        print("\nHTML create ok")