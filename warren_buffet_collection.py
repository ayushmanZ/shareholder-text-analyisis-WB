import os
import re
import requests
import nltk
from bs4 import BeautifulSoup

pip install PyPDF2

import PyPDF2

import PyPDF2
import csv
import re
import nltk
nltk.download('punkt')

def read_pdf(filename, page_range=None):
    """
    Reads the text content from a specified range of pages in a PDF file.
    :param filename: PDF file name
    :param page_range: Range of pages to read (e.g., [start_page, end_page])
    :return: Text content
    """
    with open(filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        if page_range is None:
            page_range = [0, len(reader.pages)]
        start_page, end_page = page_range
        for page_num in range(start_page, end_page):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def clean_text(text):
    """
    Cleans the text by removing special characters and extra spaces.
    :param text: Input text
    :return: Cleaned text
    """
    cleaned_text = re.sub('[^a-zA-Z0-9\s]', '', text)
    cleaned_text = re.sub('\s+', ' ', cleaned_text).strip()
    return cleaned_text

def tokenize_text(text):
    """
    Tokenizes the text into individual words.
    :param text: Input text
    :return: List of tokens
    """
    tokens = nltk.word_tokenize(text)
    return tokens

def save_as_csv(data, filename):
    """
    Saves the data as a CSV file.
    :param data: Data to be saved
    :param filename: Output filename
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    # List of PDF files and their corresponding page numbers to read
    pdf_files = [

        {'filename': '2020ar.pdf', 'pages': [5, 17]},
        {'filename': '2021ar.pdf', 'pages': [5, 17]},
        {'filename': '2022ar.pdf', 'pages': [5, 17]},
    ]

    # Read and combine the text from all the PDFs
    combined_text = ''
    for pdf_file in pdf_files:
        filename = pdf_file['filename']
        pages = pdf_file.get('pages')
        text = read_pdf(filename, pages)
        combined_text += text

    # Clean the text
    cleaned_text = clean_text(combined_text)

    # Tokenize the text
    tokenized_text = tokenize_text(cleaned_text)

    # Save as CSV
    output_filename = 'combined_tokenized_text.csv'
    save_as_csv(tokenized_text, output_filename)

if __name__ == '__main__':
    main()
