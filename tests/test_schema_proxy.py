#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c), 2018-2019, SISSA (International School for Advanced Studies).
# All rights reserved.
# This file is distributed under the terms of the MIT License.
# See the file 'LICENSE' in the root directory of the present
# distribution, or http://opensource.org/licenses/MIT.
#
# @author Davide Brunato <brunato@sissa.it>
#
import unittest
import lxml.etree

from elementpath import *
from elementpath.namespaces import XML_LANG_QNAME

try:
    # noinspection PyPackageRequirements
    import xmlschema
except (ImportError, AttributeError):
    xmlschema = None

try:
    from tests import test_xpath2_parser
except ImportError:
    # Python2 fallback
    import test_xpath2_parser


@unittest.skipIf(xmlschema is None, "xmlschema library >= v1.0.7 required.")
class XPath2ParserXMLSchemaTest(test_xpath2_parser.XPath2ParserTest):

    if xmlschema:
        schema = XMLSchemaProxy(
            schema=xmlschema.XMLSchema('''
            <!-- Dummy schema, only for tests -->
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://xpath.test/ns">
            <xs:element name="test_element" type="xs:string"/>
            <xs:attribute name="test_attribute" type="xs:string"/>
            </xs:schema>''')
        )
    else:
        schema = None

    def setUp(self):
        self.parser = XPath2Parser(namespaces=self.namespaces, schema=self.schema, variables=self.variables)

    def test_xmlschema_proxy(self):
        context = XPathContext(root=self.etree.XML('<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"/>'))

        self.wrong_name("schema-element(nil)")
        self.wrong_name("schema-element(xs:string)")
        self.check_value("schema-element(xs:complexType)", None)
        self.check_value("schema-element(xs:schema)", context.item, context)
        self.check_tree("schema-element(xs:group)", '(schema-element (: (xs) (group)))')

        context.item = AttributeNode(XML_LANG_QNAME, 'en')
        self.wrong_name("schema-attribute(nil)")
        self.wrong_name("schema-attribute(xs:string)")
        self.check_value("schema-attribute(xml:lang)", None)
        self.check_value("schema-attribute(xml:lang)", context.item, context)
        self.check_tree("schema-attribute(xsi:schemaLocation)", '(schema-attribute (: (xsi) (schemaLocation)))')

    def test_instance_expression(self):
        element = self.etree.Element('schema')
        context = XPathContext(element)

        # Test cases from https://www.w3.org/TR/xpath20/#id-instance-of
        self.check_value("5 instance of xs:integer", True)
        self.check_value("5 instance of xs:decimal", True)
        self.check_value("9.0 instance of xs:integer", False if xmlschema.__version__ >= '1.0.8' else True)
        self.check_value("(5, 6) instance of xs:integer+", True)
        self.check_value(". instance of element()", True, context)

        self.check_value("(5, 6) instance of xs:integer", False)
        self.check_value("(5, 6) instance of xs:integer*", True)
        self.check_value("(5, 6) instance of xs:integer?", False)

        self.check_value("5 instance of empty-sequence()", False)
        self.check_value("() instance of empty-sequence()", True)

    def test_treat_expression(self):
        element = self.etree.Element('schema')
        context = XPathContext(element)

        self.check_value("5 treat as xs:integer", [5])
        # self.check_value("5 treat as xs:string", ElementPathTypeError)   # FIXME: a bug of xmlschema!
        self.check_value("5 treat as xs:decimal", [5])
        self.check_value("(5, 6) treat as xs:integer+", [5, 6])
        self.check_value(". treat as element()", [element], context)

        self.check_value("(5, 6) treat as xs:integer", ElementPathTypeError)
        self.check_value("(5, 6) treat as xs:integer*", [5, 6])
        self.check_value("(5, 6) treat as xs:integer?", ElementPathTypeError)

        self.check_value("5 treat as empty-sequence()", ElementPathTypeError)
        self.check_value("() treat as empty-sequence()", [])

    def test_castable_expression(self):
        self.check_value("5 castable as xs:integer", True)
        self.check_value("'5' castable as xs:integer", True)
        self.check_value("'hello' castable as xs:integer", False)
        self.check_value("('5', '6') castable as xs:integer", False)
        self.check_value("() castable as xs:integer", False)
        self.check_value("() castable as xs:integer?", True)

    def test_cast_expression(self):
        self.check_value("5 cast as xs:integer", 5)
        self.check_value("'5' cast as xs:integer", 5)
        self.check_value("'hello' cast as xs:integer", ElementPathValueError)
        self.check_value("('5', '6') cast as xs:integer", ElementPathTypeError)
        self.check_value("() cast as xs:integer", ElementPathValueError)
        self.check_value("() cast as xs:integer?", [])
        self.check_value('"1" cast as xs:boolean', True)
        self.check_value('"0" cast as xs:boolean', False)


@unittest.skipIf(xmlschema is None, "xmlschema library >= v1.0.7 required.")
class LxmlXPath2ParserXMLSchemaTest(XPath2ParserXMLSchemaTest):
    etree = lxml.etree


if __name__ == '__main__':
    unittest.main()
