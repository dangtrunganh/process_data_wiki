
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
