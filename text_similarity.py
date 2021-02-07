"""
created by : Rajath Nagaraj.
Date and Time : 2/6/2021 - 6:00PM
Background : This file takes two text strings as input and provides a value between 0 and 1
including the boundaries 0 being not similar and 1 being most similar or same. The values can
be between 0 to 1 (including boundaries 0 and 1) ex output could  be 0, 0.4, 0.7, 0.8, 1.
"""

#Importing all the required packages.
import math # to perform basic math operations.
import string # to handle strings.
import numpy as np
import pandas as pd


def process_text(text:str)->dict:

    """
    args : text in form of string example "welcome to New Year 2021"
    return: The process text function return a dictionay with words and their frequency.
    Function disctiption : The function converts the text into lower case in the first step
    later it converts it into a list of words and creates a dictionary with the words with its
    corresponding frequency.
    """

    #Coverting the text to lower.
    text_to_lower = text.lower()
    #converting any punctuation to space.
    text_without_punc = str.maketrans('', '', string.punctuation)
    text_without_punc = text_to_lower.translate(text_without_punc)
    words_list = []
    #converting the string into a list
    words_list = text_without_punc.split()
    #Creating the dictionary with words corresponding to their frequency.
    word_counter = {}
    for word in words_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    return word_counter

def dotproduct_of_two_strings(doc1, doc2):

    """
    args: doc1 : string 1, doc2 : string 2
    return: dot_product of two string vectors.
    Function discription : This function performs the dot product for two strings.
    """

    dot_prod = 0
    for i in doc1:
        if i in doc2:
            dot_prod+= (doc1[i]*doc2[i])
    return dot_prod

def finding_vector_angle(doc1,doc2):

    """
    args: doc1 : string 1, doc2 : string 2
    return: cosine distance. .
    Function discription : This function performs the cosine distance for the words.s
    """

    nmrtr = dotproduct_of_two_strings(doc1, doc2)
    #Calculating the cosine distance nmrtr - Numerator and # dnmntr - Denominator.
    dnmntr = math.sqrt(dotproduct_of_two_strings(doc1, doc1)*dotproduct_of_two_strings(doc2, doc2))
    return (nmrtr / dnmntr)


# This function finds the overall similarity of the strings.
def finding_the_similarity(string1, string2):

    """
    args:  string 1 : str, string 2:str
    return: cosine distance. .
    Function discription : This function performs all the above functions calls function process text, vector_angle.
    """

    words_string1 = process_text(string1)
    # print("1",words_string1)
    words_string2 = process_text(string2)
    # print("2",words_string2)
    distance_of_two_strings = finding_vector_angle(words_string1, words_string2)
    return distance_of_two_strings



