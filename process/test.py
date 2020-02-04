import wiki_dump_parser as parser
import untangle
# parser.xml_to_csv('/home/anhdt157/Trung-Anh/Virgo-Trung-Anh/Data-Wiki/Main/enwiki-20181001-corpus.xml')
# parser.xml_to_csv('/home/anhdt157/Trung-Anh/Virgo-Trung-Anh/Data-Wiki/Main/wikidatawiki-20200201-stub-articles26.xml')

# ===========
# articles = untangle.parse('../data/test.xml')
#
# for page in articles.mediawiki.page:
#     print(page.article)
#     # for text in page.revision.text:
#     #     print(text.cdata)
#
# # print(articles)

# <foo>
#    <bar>
#       <type foobar="1"/>
#       <type foobar="2"/>
#    </bar>
# </foo>

import xml.etree.ElementTree as ET
tree = ET.parse('../data/test1.xml')
root = tree.getroot()
print(root.tag)
test = root[0][0][0]
# x = test.tostring()
print(type(test))
print("=========1")
print(" ".join(test.itertext()))
print("=========2")
print(" ".join((" ".join(test.itertext())).split()))
# for child in root:
#     print(child.tag, child.attrib)

# for type_tag in root.findall('bar/type'):
#     value = type_tag.get('foobar')
#     print(value)
# for article in root.findall('article'):
#     value = article.get('name')
#     print(value)
