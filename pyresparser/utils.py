import os
import re
from pdfminer.high_level import extract_text as pdf_extract_text
from docx import Document

def extract_text(file_path, file_extension):
    """
    Extract text from resume file based on file extension.
    Supports PDF and DOCX formats.
    """
    text = ""
    if file_extension.lower() == '.pdf':
        text = pdf_extract_text(file_path)
    elif file_extension.lower() == '.docx':
        doc = Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
    else:
        # For other file types, try reading as plain text
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception:
            text = ""
    return text

def extract_name(nlp_doc, matcher=None):
    # Dummy implementation: extract first PERSON entity
    for ent in nlp_doc.ents:
        if ent.label_ == 'PERSON':
            return ent.text
    return None

def extract_email(text):
    email_regex = r'[\w\.-]+@[\w\.-]+\.\w+'
    matches = re.findall(email_regex, text)
    return matches[0] if matches else None

def extract_mobile_number(text, custom_regex=None):
    # Basic regex for phone numbers
    phone_regex = custom_regex if custom_regex else r'\+?\d[\d -]{8,}\d'
    matches = re.findall(phone_regex, text)
    return matches[0] if matches else None

def extract_skills(nlp_doc, noun_chunks, skills_file=None):
    # Dummy implementation: return empty list
    return []

def extract_entity_sections_grad(text):
    # Dummy implementation: return empty dict
    return {}

def get_number_of_pages(file_path):
    # Dummy implementation: return 1
    return 1
