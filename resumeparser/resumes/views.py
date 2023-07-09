from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io
import pytesseract
import PyPDF2

import re

from resumes.models import resmesdetails

def form(request):
    return render(request, "form.html")

def form2(request):
    name = request.GET.get('name') 
    save_image_path = request.GET.get('save_image_path')
    extracted_details = extract_details_from_cv(save_image_path)
    name = extracted_details.get('name')
    email=extracted_details.get('email')
    phone = extracted_details.get('phone')
    college = extracted_details.get('college')
    specilization = extracted_details.get('specilization')
    graduation = extracted_details.get('graduation')
    gender = extracted_details.get('gender')
    # 'email','phone','college','specilization','graduation','gender
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print(name)


    return render(request, "form2.html",{'name': name,'phone':phone,'email':email,'gender':gender,'specilization':specilization,'college':college,'graduation':graduation})

def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    converter.close()
    fake_file_handle.close()
    return text


def uploadresume(request):
    if request.method == 'POST' and 'file' in request.FILES:
        resume = request.FILES['file']
        fs = FileSystemStorage()
        fp = fs.save(resume.name, resume)
        save_image_path = fs.path(fp)
        # extracted_details = extract_details_from_cv(save_image_path)
        # print("Extracted Details:\n", extracted_details)
        return HttpResponseRedirect(f'/form2?save_image_path={save_image_path}')
       
    return HttpResponse("Error: Invalid request")


def extract_details_from_cv(save_image_path):
    extracted_details = {}
    with open(save_image_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        cv_text = ''
        for page in pdf_reader.pages:
            cv_text += page.extract_text()

    # Extract name
   
# Example usage

        # Extract name
    # name_match = re.search(r"name[^\w\n]+([\w\s]+)", cv_text, re.IGNORECASE)
    # if name_match:
    #     extracted_details['name'] = name_match.group(1).strip()


    name_match = re.search(r"([A-Z][a-z]+\s+([A-Z][a-z]+\s*)+)", cv_text)
    if name_match:
        extracted_details['name'] = name_match.group(1)

    # Extract email
    email_match = re.search(r"[\w.-]+@[\w.-]+\.\w+", cv_text)
    if email_match:
        extracted_details['email'] = email_match.group().strip()

    # Extract phone number
    phone_match = re.search(r"\+?\d{10,12}", cv_text)
    if phone_match:
        extracted_details['phone'] = phone_match.group().strip()

        # Extract gender
    gender_match = re.search(r"Gender:\s+(Male|Female|Other)", cv_text)
    if gender_match:
        extracted_details['gender'] = gender_match.group(1)

        # Extract highest qualification
    qualification_match = re.search(r"Qualification:\s+(.+)" or "qualification" or "education", cv_text)
    if qualification_match:
        extracted_details['highest_qualification'] = qualification_match.group(1)


        
        # Extract college
    college_match = re.search(r"College:\s+(.+)", cv_text)
    if college_match:
        extracted_details['college'] = college_match.group(1)

        # Extract specialization/branch
    specialization_match = re.search(r"Specialization/Branch:\s+(.+)", cv_text)
    if specialization_match:
        extracted_details['specilization'] = specialization_match.group(1)

        # Extract year of graduation
    graduation_match = re.search(r"Year of Graduation:\s+(\d{4})", cv_text)
    if graduation_match:
        extracted_details['graduation'] = graduation_match.group(1)
   
    return extracted_details

def savedetails(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['mobile']
    gender = request.POST['gender']
    qualification = request.POST['qualification']
    college = request.POST['college']
    year=request.POST['graduation']
    ob=resmesdetails()
    ob.name=name
    ob.email=email
    ob.mob=phone
    ob.gender=gender
    ob.qualification=qualification
    ob.specilization=qualification
    ob.college=college
    ob.phone=1
    ob.resume=1
    ob.year=year
    ob.save()

    return HttpResponse('''<script>alert(" saved");window.location='/form'</script>''')