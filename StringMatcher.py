import string

def convertToRawString(str):
    str_in_lower_case = str.lower().strip()
    return str_in_lower_case.translate(str.maketrans('', '', string.punctuation))


def calculateSimilarityIndex(str1, str2):
    raw_str1 = convertToRawString(str1)
    raw_str2 = convertToRawString(str2)

    dict_of_str1 = raw_str1.split(" ")
    dict_of_str2 = raw_str2.split(" ")


    if len(dict_of_str1) <= len(dict_of_str2):
        dict_of_lowest_len_str = dict_of_str1
        dict_of_highest_len_str = dict_of_str2
    else:
        dict_of_lowest_len_str = dict_of_str2
        dict_of_highest_len_str = dict_of_str1

    word_count = 0

    for i in dict_of_lowest_len_str:
        if i in dict_of_highest_len_str:
            word_count+=1

    similarity_index = round(word_count/(len(dict_of_lowest_len_str)+len(dict_of_highest_len_str)-word_count),5)
    print(similarity_index)
    return similarity_index



