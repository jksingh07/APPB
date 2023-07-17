from flask import Flask, request, jsonify
import json
import PyPDF2
from AI_Resume_Parser import *

app = Flask(__name__)

# API endpoint to process the PDF file
@app.route('/parse_resume', methods=['POST'])
def parse_resume():
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file found in the request'}), 400

    file = request.files['file']
##    print(file)
    file.save('resume_new.pdf')
    # Read the contents of the file
    file_contents = file.read()

##    print(file_contents)
    
    # Check if the file is a PDF
    if file.filename.endswith('.pdf'):
        try:
            # Read the PDF file and extract text
##            pdf_reader = PyPDF2.PdfReader(file)
##            text = ""
##            for page in pdf_reader.pages:
##                text += page.extract_text()

            input_text = extract_text_from_pdf('resume_new.pdf')

            # Process the extracted text and generate the JSON output
            json_output = resume_parser(input_text)
            
            # Replace the following example code with your actual processing logic
##            json_output = {'text': text}
            
            return jsonify(json_output), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file format. Only PDF files are supported'}), 400

if __name__ == '__main__':
    app.run()
