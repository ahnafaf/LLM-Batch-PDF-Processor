# PDF Processor Documentation

This Python script is designed to process PDFs from provided URLs and generate summaries or perform specific tasks using OpenAI's GPT-3 model.

## Dependencies

To run this script, you need the following Python libraries:

- `io`
- `requests`
- `pdfminer`
- `openai`

Make sure to install them using pip:

```bash
pip install requests pdfminer.six openai
```

## Setting Up

Before using the script, make sure to set your OpenAI API key:

```python
openai.api_key = "YOUR_OPENAI_API_KEY"
```

## Functions

The script contains four functions:

- `get_pdf_text(pdf_file)`: This function takes a `BytesIO` object of a PDF file and extracts the text from it using `pdfminer`.

- `process_with_gpt(pdf_text)`: This function takes the extracted text from a PDF file and processes it with OpenAI's GPT-3 model. The processing task depends on the instruction provided in the "system" message. The processed text is then returned.

- `process_pdfs(pdf_urls)`: This function takes a list of URLs, retrieves the PDF files from the URLs, extracts the text, and processes the text with GPT-3. The function returns a dictionary where the keys are the URLs and the values are the GPT-3 processed texts.

- `pdf_links`: A list of PDF URLs to be processed. Replace `["link1", "link2", "link3"]` with your actual PDF URLs.

## Usage

To use the script, replace the placeholder in the "system" message in the `process_with_gpt()` function with the task you want GPT-3 to perform on the extracted PDF text. For example:

```python
{
    "role": "system",
    "content": "You are a helpful assistant. Summarize the following text."
}
```

Then, replace the `pdf_links` list with your actual PDF URLs:

```python
pdf_links = ["https://example.com/file1.pdf", "https://example.com/file2.pdf", "https://example.com/file3.pdf"]
```

Finally, call the `process_pdfs()` function and pass the `pdf_links` list:

```python
print(process_pdfs(pdf_links))
```

The script will then download the PDFs, extract the text, process the text with GPT-3, and print the results.

## Output

The output will be a dictionary where the keys are the URLs and the values are the GPT-3 processed texts. For example:

```python
{
    "https://example.com/file1.pdf": "Summary of file1.pdf...",
    "https://example.com/file2.pdf": "Summary of file2.pdf...",
    "https://example.com/file3.pdf": "Summary of file3.pdf..."
}
```
