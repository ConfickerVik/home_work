from xml.dom import minidom


class Create_wsdl:

    def create_wsdl(self):
        doc = minidom.Document()

        # Создание основного тега 'definitions'
        root = doc.createElement('definitions')
        root.setAttribute('name', 'Name')
        doc.appendChild(root)

        # Создание тега 'Types'
        Types = doc.createElement('Types')
        root.appendChild(Types)

        # Создание подтега 'schema' в тег 'Types'
        schema = doc.createElement('schema')
        schema.setAttribute('targetNamespace', 'Target_name')
        Types.appendChild(schema)

        # Создание тега 'Message'
        Message = doc.createElement('Message')
        # Добавление атрибута 'name_sub' и присвоение ему значения 'KPO'
        Message.setAttribute('name', '1')
        root.appendChild(Message)

        # Создание подтега 'part' в тег 'Message'
        part = doc.createElement('part')
        part.setAttribute('name', 'body')
        part.setAttribute('element', 'body_element')
        Message.appendChild(part)

        # Создание тега 'portType'
        portType = doc.createElement('portType')
        portType.setAttribute('name', 'port_name')
        root.appendChild(portType)

        # Создание подтега 'operation' в тег 'portType'
        operation = doc.createElement('operation')
        operation.setAttribute('name', 'operation_name')
        portType.appendChild(operation)

        # Создание подтега 'input' в тег 'operation'
        inputq = doc.createElement('input')
        inputq.setAttribute('message', 'input_message')
        operation.appendChild(inputq)

        # Создание подтега 'output' в тег 'operation'
        outputq = doc.createElement('output')
        outputq.setAttribute('message', 'output_message')
        operation.appendChild(outputq)

        # Создание тега 'binding'
        binding = doc.createElement('binding')
        binding.setAttribute('type', 'binding_type')
        binding.setAttribute('name', 'binding_name')
        root.appendChild(binding)

        # Создание подтега 'soap:binding' в тег 'binding'
        soapbinding = doc.createElement('soap:binding')
        soapbinding.setAttribute('style', 'document')
        binding.appendChild(soapbinding)

        # Создание подтега 'oper' в тег 'binding'
        oper = doc.createElement('operation')
        oper.setAttribute('name', 'operation_name')
        binding.appendChild(oper)

        wsdl_str = doc.toprettyxml(indent="  ")

        with open("created_wsdl.xml", "w") as f:
            f.write(wsdl_str)
