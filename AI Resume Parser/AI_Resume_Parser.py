import openai
import json
#from pdfminer.high_level import extract_text
import re
import PyPDF2


##def extract_text_from_pdf(file_path):
##    text = extract_text(file_path)
##    return text


def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

def extract_resume_details(input_text):
    openai.api_key = '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'

    prompt = '''
    Extract the following details from the given resume JSON:

    - Experiences (company, position, duration, description)
    - Project Work (project_heading, project_desc)
    - Contact Info (email)
    - Intro Info (name, status)
    - About Info (firstPara, secondPara)
    - LinkedIn
    - Github
    - Email
    - Contact Info
    - Summary
    - Skills
    '''

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": input_text}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,
        n=1,
        stop=None
    )

    return response['choices'][0]['message']['content']

def resume_parser(input_text):
    output = extract_resume_details(input_text)

    
    # Extract Experiences
    experiences = re.findall(r'Company: (.+)\n\s+Position: (.+)\n\s+Duration: (.+)\n\s+Description:((?:.+\n)+)', output)
    experiences_list = []
    for experience in experiences:
        company, position, duration, description = experience
        description = re.findall(r'(.+)', description)
        experiences_list.append({
            "company": company,
            "position": position,
            "duration": duration,
            "description": description
        })

    # Extract Project Work
    project_work = re.findall(r'Project Heading: (.+)\n\s+Project Description: (.+)\n\s+Technologies: (.+)\n', output)
    project_work_list = []
    for project in project_work:
        project_heading, project_desc, technologies = project
        project_work_list.append({
            "project_heading": project_heading,
            "project_desc": project_desc,
            "technologies": technologies,
            "gitUrl": "",
            "extUrl": "",
            "imgSrc": ""
        })

    # Extract Contact Info
    try:
        contact_info = re.findall(r'Contact Info:\n- Email: (.+)', output)[0]
    except:
        contact_info = "",""
        
    # Extract Intro Info
    try:
        intro_info = re.findall(r'Intro Info:\n- Name: (.+)\n- Status: (.+)', output)
        name, status = intro_info[0]
    except:
        name, status = "",""
        
    # Extract About Info
    try:
        about_info = re.findall(r'About Info:\n- First Paragraph: (.+)\n- Second Paragraph: (.+)', output)
        first_para, second_para = about_info[0]
    except:
        first_para, second_para = "",""

    # Extract LinkedIn
    try:
        linkedin = re.findall(r'LinkedIn: (.+)', output)[0]
    except:
        linkedin = ""

    # Extract Github
    try:
        github = re.findall(r'Github: (.+)', output)[0]
    except:
        github = ""

    # Extract Email ID
    try:
        email_id = re.findall(r'Email: (.+)', output)[0]
    except:
        email_id = ""

    # Extract Summary
    try:
        summary = re.search(r'Summary:\s+([\s\S]+?)\n\n', output).group(1)
    except:
        summary = ""
        
    # Extract Skills
    try:
        skills_text = re.search(r'Skills:\s+([\s\S]+)', output).group(1)
        skills = re.findall(r'- (.+)', skills_text)
    except:
        skills = ""

    # Extract headerData
    header_data = {
        "resumeSrc": "",
        "logoSrc": "/assets/favicon-512x512.png"
    }

    # Extract footerData
    footer_data = {
        "gitUrl": "https://github.com/iamsahilsoni/SahilSoniWebPortfolio2023",
        "creditContent": "Design Motivation from Brittany Chiang",
        "creditUrl": "https://brittanychiang.com/",
        "selfCreditContent": "Built by <strong>Sahil Soni</strong>",
        "gitRepo": "iamsahilsoni/SahilSoniWebPortfolio2023"
    }


    # Extract socialMediaLinks
    social_media_links = {
        "githubUrl": github,
        "leetcodeUrl": "",
        "instaUrl": "",
        "twitterUrl": "",
        "linkedinUrl": linkedin
    }

    # Extract emails
    emails = [email_id]

    thanks_note = """Thank you for visiting my portfolio! <br /><br />
    Please don't hesitate to contact me through email or other platforms. I look forward to hearing from you soon!"""

    # Create the JSON object
    data = {
        "userData": {
            "experiences": experiences_list,
            "projectWork": project_work_list,
            "contactInfo": {"email": contact_info, "content":thanks_note},
            "introInfo": {"name": name, "status": status, "displayPic":"","summary": summary},
            "aboutInfo": {"firstPara": first_para, "secondPara": second_para, "displayPic":"", "skillsList":skills}
        },
        "headerData": header_data,
        "footerData": footer_data,
        "socialMediaLinks": social_media_links,
        "emails": emails
    }

    # Convert to JSON
    json_output = json.dumps(data, indent=4)

    return json_output



if __name__ == '__main__':
    input_text = extract_text_from_pdf('resume_jk.pdf')
    json_output = resume_parser(input_text)
    print(json_output)
    with open("data.json", "w") as outfile:
        outfile.write(json_output)
    
