import xml.etree.ElementTree as ET
import os
from os.path import isfile, join
import re

PATH_SPLITED_FILE = '/home/anhdt157/VTA/WIKI/output_split/'
OUTPUT_RESULT = '/home/anhdt157/VTA/WIKI/output_parquet/'


# tree = ET.parse('../data/0.xml')
#
# root = tree.getroot()
def get_content_article(article):
    # each article
    result_dict_df = {}

    # NAME
    result_dict_df['name'] = article.get('name')

    # REDIRECT
    list_redirect = []

    # CATEGORY
    list_category = []

    # ARTICLE
    list_content = []

    for content in article:
        if content.tag == 'redirect':
            list_redirect.append(clean_text(content.get('name')))
        if content.tag == 'category':
            list_category.append(clean_text(content.get('name')))
        if content.tag == 'content':
            for ph in content:
                tag_ph = ph.tag
                print('=====================')
                print(ph.text)
                # if tag_ph == 'h':
                #     if ph.text is None:
                #         result_h = '<HHH>HNoneH</HHH>\n'
                #     else:
                #         result_h = '<HHH>' + ph.text + '</HHH>\n'


def clean_text(text):
    # replace
    text = text.replace('&apos;', '\'')
    text = re.sub('\s+', ' ', text)
    return text


def main_process():
    count = 0
    list_files = [f for f in os.listdir(PATH_SPLITED_FILE) if isfile(join(PATH_SPLITED_FILE, f))]
    for file_index in range(len(list_files)):
        # INPUT_DATA
        result_each_splited_file = ''
        file_name = list_files[file_index]
        path_file = os.path.join(PATH_SPLITED_FILE, file_name)

        print(file_index)
        print(path_file)

        # each file
        # tree = ET.parse(path_file)
        # OUTPUT_RESULT
        output_name = file_name.replace('.xml', '.txt')
        output_result = os.path.join(OUTPUT_RESULT, output_name)

        root = ET.parse(path_file).getroot()
        for article in root.findall('article'):
            print(get_content_article(article))
        #     # name_article = article.get('name')
        #     # print('===========NAME=============')
        #     # print("Name = " + name_article)
        #     result_each_splited_file += content_of_article(article)
        #     count += 1
        #     # print('Content = ' + result_x)
        # with open(output_result, 'w') as fw:
        #     fw.write(result_each_splited_file)
        #
        # print('DONE -->', output_result)
        # print('Current - count - file = ', str(count))


if __name__ == '__main__':
    main_process()
# # count_x = 0
# # for article in root.findall('article'):
# #     count_x += 1
# #     name_article = article.get('name')
# #     print('===========NAME=============')
# #     print("Name = " + name_article)
# #     result_x = content_of_article(article)
# #     print('Content = ' + result_x)
# # print("NUMBER_OF_ARTILCES = " + str(count_x))
# count = 0
# only_files = [f for f in listdir(PATH_SPLITED_FILE) if isfile(join(PATH_SPLITED_FILE, f))]
# for file_index in range(len(only_files)):
#     result_each_splited_file = ''
#     file_name = only_files[file_index]
#     path_file = PATH_SPLITED_FILE + '/' + file_name
#     print(file_index)
#     print(path_file)
#
#     # each file
#     # tree = ET.parse(path_file)
#     output_name = file_name.replace('.xml', '.txt')
#     output_result = OUTPUT_RESULT + '/' + output_name
#     root = ET.parse(path_file).getroot()
#     for article in root.findall('article'):
#         # name_article = article.get('name')
#         # print('===========NAME=============')
#         # print("Name = " + name_article)
#         result_each_splited_file += content_of_article(article)
#         count += 1
#         # print('Content = ' + result_x)
#     with open(output_result, 'w') as fw:
#         fw.write(result_each_splited_file)
#
#     print('DONE -->', output_result)
#     print('Current - count - file = ', str(count))

# def content_of_article(article):
#     # each article
#     final_result = '<NNN>' + article.get('name') + '</NNN>\n'
#     # child of article
#     for content in article:
#         # print('content=tag -> ' + content.tag)
#         if content.tag == 'redirect':
#             final_result += '<RRR>' + content.get('name') + '</RRR>\n'
#         if content.tag == 'category':
#             final_result += '<CCC>' + content.get('name') + '</CCC>\n'
#         if content.tag == 'content':
#             for ph in content:
#                 tag_ph = ph.tag
#                 # print('ph=', tag_ph)
#                 # case 1: tag h before tag p
#                 if tag_ph == 'h':
#                     if ph.text is None:
#                         # ph.text = 'KNoneK'
#                         # print("OMG-ph-None: ", ph)
#                         result_h = '<HHH>HNoneH</HHH>\n'
#                     else:
#                         result_h = '<HHH>' + ph.text + '</HHH>\n'
#                     final_result += result_h
#                     # print(result_h)
#                 if tag_ph == 'p':
#                     have_header = False
#                     for hh in ph:
#                         if hh.tag == 'h':
#                             have_header = True
#                             if hh.text is None:
#                                 # hh.text = 'KNoneK'
#                                 # print("OMG-hh-None: ", hh)
#                                 result_hh = '<HHH>HNoneH</HHH>\n'
#                             else:
#                                 result_hh = '<HHH>' + hh.text + '</HHH>\n'
#                             final_result += result_hh
#                             # print(result_hh)
#                     # result_p = 'PPP ' + ph.text + ' PPP'
#                     # print(result_p)
#                     if have_header:
#                         # case 2: tag h in tag p
#                         result_p = " ".join((" ".join(ph.itertext())).split()[1:])
#                         result_p = result_p.replace(' , ', ', ')
#                         result_p = result_p.replace(' . ', '. ')
#                         result_p = result_p.replace(' .', '. ')
#                         result_p = '<PPP>' + result_p + '</PPP>\n'
#                         final_result += result_p
#                         # print(result_p)
#                     else:
#                         result_p = " ".join((" ".join(ph.itertext())).split())
#                         result_p = result_p.replace(' , ', ', ')
#                         result_p = result_p.replace(' . ', '. ')
#                         result_p = result_p.replace(' .', '. ')
#                         result_p = '<PPP>' + result_p + '</PPP>\n'
#                         final_result += result_p
#                         # print(result_p)
#     return final_result + '#####\n'
#
#
# # count_x = 0
# # for article in root.findall('article'):
# #     count_x += 1
# #     name_article = article.get('name')
# #     print('===========NAME=============')
# #     print("Name = " + name_article)
# #     result_x = content_of_article(article)
# #     print('Content = ' + result_x)
# # print("NUMBER_OF_ARTILCES = " + str(count_x))
# count = 0
# only_files = [f for f in listdir(PATH_SPLITED_FILE) if isfile(join(PATH_SPLITED_FILE, f))]
# for file_index in range(len(only_files)):
#     result_each_splited_file = ''
#     file_name = only_files[file_index]
#     path_file = PATH_SPLITED_FILE + '/' + file_name
#     print(file_index)
#     print(path_file)
#
#     # each file
#     # tree = ET.parse(path_file)
#     output_name = file_name.replace('.xml', '.txt')
#     output_result = OUTPUT_RESULT + '/' + output_name
#     root = ET.parse(path_file).getroot()
#     for article in root.findall('article'):
#         # name_article = article.get('name')
#         # print('===========NAME=============')
#         # print("Name = " + name_article)
#         result_each_splited_file += content_of_article(article)
#         count += 1
#         # print('Content = ' + result_x)
#     with open(output_result, 'w') as fw:
#         fw.write(result_each_splited_file)
#
#     print('DONE -->', output_result)
#     print('Current - count - file = ', str(count))
