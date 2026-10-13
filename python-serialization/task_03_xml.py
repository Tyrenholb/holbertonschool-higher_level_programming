#!/usr/bin/env python3
""""""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """take a Python dictionary and a filename as parameters"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="UTF-8")


def deserialize_from_xml(filename):
    """read the XML data from that file, and return
     a deserialized Python dictionary"""
    data = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        data[child.tag] = child.text

    return (data)
