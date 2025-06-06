#!/usr/bin/python3
"""
This module provides functions to serialize a dictionary to an XML file and
deserialize an XML file back to a dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file back to a dictionary."""

    tree = ET.parse(filename)
    root = tree.getroot()

    constructed_dictionary = {child.tag: child.text for child in root}
    return constructed_dictionary
