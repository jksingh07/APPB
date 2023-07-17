# APPB
# AI Powered Portfolio Builder

The AI Powered Portfolio Builder is a web application designed to streamline the process of creating impressive portfolios. It addresses the time-consuming and manual aspects of portfolio creation, allowing individuals to showcase their skills and experiences effectively.

## Main Problem
The main problem addressed by the project is the time-consuming and manual process of creating a portfolio. Many individuals struggle to create an impressive portfolio that effectively showcases their skills and experiences. It often involves manually extracting relevant information from their resumes and designing the portfolio layout, which can be tedious and error-prone.

## Suggested Solutions
- **Resume Parsing:** Implement a resume parser that can automatically extract key information from the user's uploaded resume, such as personal details, education, work experience, skills, and achievements. This will eliminate the need for manual data entry and ensure accurate and consistent information extraction.

- **Template Selection:** Provide 2-3 pre-designed portfolio templates for users to choose from. These templates should be visually appealing and customizable to suit individual preferences. Each template should have predefined fields that correspond to the extracted information from the resume.

- **Editable Fields:** Allow users to easily edit and customize the fields in the selected portfolio template. They should have the flexibility to add or remove sections, modify text content, rearrange the layout, and upload additional documents or media files to personalize their portfolio.

- **Database Storage:** Store all the extracted details from the user's resume in a secure database. This will enable easy retrieval and management of user information, ensuring data integrity and privacy.

- **Hosted Unique Routes:** Generate a unique and hosted route for each user, which will display their final portfolio. This allows users to share their portfolios with others by simply sharing the unique URL. The hosted route should be easily accessible and provide a seamless browsing experience for viewers.

- **Recommendation System for Resume/Portfolio Improvement:** Implement a recommendation system that analyzes each section of the user's resume/portfolio, such as skills, experience, and summary, and provides personalized suggestions for improvement. The system can leverage natural language processing and machine learning techniques to identify areas where the user's resume/portfolio can be enhanced.

## Installation
To install the necessary dependencies, run the following command:

```bash
pip install flask PyPDF2 openai
```
## Starting the Flask API

To start the Python Flask API, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the API_AI_resume_parser.py file is located.
3. Run the following command to start the backend server:

```bash
python API_AI_resume_parser.py
```
The Flask API should start running, and you will see output indicating that the server is running.

4. Run the following commmand on terminal to test the API, Note: replace resume.pdf with your file

```bash
curl -X POST -F "file=@resume.pdf" http://127.0.0.1:5000/parse_resume
```


