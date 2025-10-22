import sys

from gaphor.storage.xmlwriter import XMLWriter


class Writer:
    def __init__(self):
        self.s = ""

    def write(self, text):
        self.s += text


def test_elements_1():
    w = Writer()
    xml_w = XMLWriter(w)
    xml_w.startDocument()
    xml_w.startElement("foo", {})
    xml_w.endElement("foo")

    xml = f"""<?xml version="1.0" encoding="{sys.getdefaultencoding()}"?>\n<foo/>"""
    assert w.s == xml, f"{w.s} != {xml}"


def test_elements_2():
    w = Writer()
    xml_w = XMLWriter(w)
    xml_w.startDocument()
    xml_w.startElement("foo", {})
    xml_w.startElement("bar", {})
    xml_w.endElement("bar")
    xml_w.endElement("foo")

    xml = f"""<?xml version="1.0" encoding="{sys.getdefaultencoding()}"?>\n<foo>\n<bar/>\n</foo>"""
    assert w.s == xml, w.s


def test_elements_test():
    w = Writer()
    xml_w = XMLWriter(w)
    xml_w.startDocument()
    xml_w.startElement("foo", {})
    xml_w.startElement("bar", {})
    xml_w.characters("hello")
    xml_w.endElement("bar")
    xml_w.endElement("foo")

    xml = f"""<?xml version="1.0" encoding="{sys.getdefaultencoding()}"?>\n<foo>\n<bar>hello</bar>\n</foo>"""
    assert w.s == xml, w.s


def test_elements_ns_default():
    w = Writer()
    xml_w = XMLWriter(w)
    xml_w.startDocument()
    xml_w.startPrefixMapping(None, "http://gaphor.devjavu.com/schema")
    xml_w.startElementNS(("http://gaphor.devjavu.com/schema", "foo"), "qn", {})
    xml_w.endElementNS(("http://gaphor.devjavu.com/schema", "foo"), "qn")

    xml = f"""<?xml version="1.0" encoding="{sys.getdefaultencoding()}"?>\n<foo xmlns="http://gaphor.devjavu.com/schema"/>"""
    assert w.s == xml, w.s


def test_elements_ns_1():
    w = Writer()
    xml_w = XMLWriter(w)
    xml_w.startDocument()
    xml_w.startPrefixMapping("g", "http://gaphor.devjavu.com/schema")
    xml_w.startElementNS(("http://gaphor.devjavu.com/schema", "foo"), "qn", {})
    xml_w.endElementNS(("http://gaphor.devjavu.com/schema", "foo"), "qn")

    xml = f"""<?xml version="1.0" encoding="{sys.getdefaultencoding()}"?>\n<g:foo xmlns:g="http://gaphor.devjavu.com/schema"/>"""
    assert w.s == xml, w.s
