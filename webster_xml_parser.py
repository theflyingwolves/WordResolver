import xml.etree.ElementTree as ET

def parse(fileName):
	return ET.parse(fileName).getroot()

def parsedttag(node):
	text = node.text
	for child in node:
		if child.text is not None:
			text += child.text
	return text

def get_definitions_from_file(fileName):
	definitions = []
	entry = parse(fileName)[0]
	for child in entry:
		if child.tag == "def":
			for subchild in child:
				if subchild.tag == "dt":
					definitions.append(parsedttag(subchild))
			break;
	return definitions