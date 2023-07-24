from flask import Flask, request, jsonify
from AI_Resume_Parser import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# API endpoint to process the PDF file
@app.route('/parse_resume', methods=['POST'])
@cross_origin()
def parse_resume():
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file found in the request'}), 400

    file = request.files['file']
    file.save('resume_new.pdf')

    # Read the contents of the file
    file_contents = file.read()
    
    # Check if the file is a PDF
    if file.filename.endswith('.pdf'):
        try:
            input_text = extract_text_from_pdf('resume_new.pdf')

            # Process the extracted text and generate the JSON output
            json_output = resume_parser_json(input_text)
            
            return jsonify(json_output), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file format. Only PDF files are supported'}), 400


@app.route('/get_user', methods=['GET', 'POST'])
@cross_origin()
def get_user():
    db = db.connect(MONGODB)
    user = request.get('username')
    selected_user=db.fetch(user) # if not exist --> None

    return jsonify(selected_user)
    

if __name__ == '__main__':
    app.run()
