from io import BytesIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import requests
import openai

openai.api_key = ""

def get_pdf_text(pdf_file):
    resource_mgr = PDFResourceManager()
    fake_file_handle = BytesIO()
    converter = TextConverter(resource_mgr, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_mgr, converter)

    for page in PDFPage.get_pages(pdf_file):
        page_interpreter.process_page(page)

    text = fake_file_handle.getvalue().decode("utf-8")

    converter.close()
    fake_file_handle.close()

    return text

def process_with_gpt(pdf_text):
    responses = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """FILL IN WHAT YOU WANT GPT TO DO"""
            },
            {
                "role": "user",
                "content": pdf_text
            }
        ]
    )
    return responses['choices'][0]['message']['content']

def process_pdfs(pdf_urls):
    result = {}
    for url in pdf_urls:
        response = requests.get(url)
        pdf_file = BytesIO(response.content)
        pdf_text = get_pdf_text(pdf_file)
        gpt_result = process_with_gpt(pdf_text)
        result[url] = gpt_result
    return result

pdf_links = ["link1", "link2", "link3"]

print(process_pdfs(pdf_links))
