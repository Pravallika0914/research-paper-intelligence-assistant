import pdfplumber

def extract_text(path):
    text = ""
    page_count = 0

    with pdfplumber.open(path) as pdf:
        page_count = len(pdf.pages)

        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"

    return text, page_count