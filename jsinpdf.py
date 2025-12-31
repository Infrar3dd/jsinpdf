#!/usr/bin/env python3
import argparse
import PyPDF2
import io

def add_javascript_to_pdf(input_pdf, output_pdf, javascript_code):

    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()
        
        # Копируем все страницы
        for page in reader.pages:
            writer.add_page(page)
        
        # Добавляем JavaScript в качестве открытого действия
        writer.add_js(javascript_code)
        
        # Сохраняем результат
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Utility to embed JS to PDF')
    parser.add_argument('-i','--input', help='Input PDF')
    parser.add_argument('-o','--output', help='Output PDF')
    parser.add_argument('-js','--javascript', help='File with JS code')
    args = parser.parse_args()

    try:
        with open(f"{args.javascript}", 'r') as f:
            sample_js = f.read()

        add_javascript_to_pdf(args.input, args.output, sample_js)

        print("Done!")
    except:
        parser.print_help()