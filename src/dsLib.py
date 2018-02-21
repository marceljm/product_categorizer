# coding=utf-8

from constants import *
from adjust_category import *
from re import sub
from unidecode import unidecode


# check if a product is available
def available_product(lst):
    return 'true' in zanox_availability(lst)


# replace the dictionary key by the value
def convert(name, dic):
    output = ''
    for word in name.split():
        aux = dic.get(word)
        output += (aux if aux else word) + ' '
    return output[:-1]


# search for a feature in the name, returning its id
def search_feature(name, dic):
    name = name.split()
    for word in dic:
        if word in name:
            return str(dic[word])
    return ' '


# split the orginal data
def field_list(line):
    return line.split("\";\"")


# return the N first words of the name
def first_n_words(name, n):
    lst = name.split(' ')
    n = (n + 2) if (lst[0] in GROUP) else n
    output = ''
    for i in range(0, n):
        if (i < len(lst)):
            output += lst[i] + ' '
    return output[:-1]


# receive a product (as a list of features) from original data
# transform that and return the result in a new format (CSV)
def format_line(lst):
    name = transform_name(zanox_name(lst))
    brand = transform_name(zanox_brand(lst))
    category = adjust_category(name, zanox_category(lst))
    nameCategory = name + ' ' + transform_name(category)
    return first_n_words(name, 3) + ';' + brand + ';' + \
           search_feature(nameCategory, GENDER) + ';' + \
           search_feature(nameCategory, ROOM) + ';' + \
           search_feature(nameCategory, VEHICLE) + ';' + \
           search_feature(nameCategory, CONSOLE) + ';' + \
           search_feature(nameCategory, DEVICE) + ';' + \
           search_feature(nameCategory, PET) + ';' + \
           search_feature(nameCategory, MATTRESS) + ';' + \
           search_feature(nameCategory, CUP) + ';' + \
           category + '\n'


# output header
def header():
    return HEADER


# join whitespaces
def merge_space(name):
    return ' '.join(name.split())


# remove words from the name
def remove(name, lst):
    output = ''
    for word in name.split():
        if (word not in lst):
            output += word + ' '
    return output[:-1]


# remove accents
def remove_accents(name):
    return unidecode(name)


# remove bad chars
def remove_bad_chars(name):
    return sub("[\~\<\=\>\|\_\-\,\:\!\?\/\.\'\"\(\)\[\]\@\$\*\\\&\#\%\+\;\ª\°]", " ", name)


# receive a product (as a CSV row) from original data
# convert to list
def transform_line(line):
    line = trim_quotation_marks(line)
    return field_list(line)


# normalize a text
def transform_name(name):
    name = remove_bad_chars(name)
    name = name.lower()
    name = remove_accents(name)
    name = merge_space(name)
    name = convert(name, PLURAL_SINGULAR)
    name = convert(name, FEMALE_MALE)
    name = remove(name, BAD_WORDS)
    name = remove(name, COLORS)
    name = remove_bad_chars(name)
    return name


# remove quotation marks
def trim_quotation_marks(line):
    line = sub("^[^\"]*\"", "", line)
    return sub("\"[^\"]*$", "", line)


# validate product
def valid(lst, categoryCount):
    if not walmart_dataset:
        return True
    return available_product(lst) and valid_price(lst) and valid_category(lst, categoryCount)


# validate category
def valid_category(lst, categoryCount):
    category = zanox_category(lst)

    if categoryCount[category] < MIN_CATEGORY_SIZE:
        return False

    for word in INACTIVE:
        if word in category.lower():
            return False
    return True


# validate price
def valid_price(lst):
    return float(zanox_price(lst)) < MAX_VALID_PRICE


# check if it is a walmart dataset
def walmart_dataset(lst):
    return int(zanox_program_id(lst)) == WALMART_PROGRAM_ID


# product availability
def zanox_availability(lst):
    return lst[ZANOX_INDEX_AVAILABILITY]


# product brand
def zanox_brand(lst):
    return lst[ZANOX_INDEX_BRAND]


# product category
def zanox_category(lst):
    return lst[ZANOX_INDEX_CATEGORY] if not lst[ZANOX_INDEX_CATEGORY2] else lst[ZANOX_INDEX_CATEGORY] + ' / ' + lst[ZANOX_INDEX_CATEGORY2]


# product ean
def zanox_ean(lst):
    return lst[ZANOX_INDEX_EAN]


# product id
def zanox_id(lst):
    return lst[ZANOX_INDEX_ID]


# product name
def zanox_name(lst):
    return lst[ZANOX_INDEX_NAME]


# product price
def zanox_price(lst):
    return lst[ZANOX_INDEX_PRICE]


# program id
def zanox_program_id(lst):
    return lst[ZANOX_INDEX_PROGRAM_ID]
