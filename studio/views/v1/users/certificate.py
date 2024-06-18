from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import boto3
from botocore.exceptions import NoCredentialsError
from django.http import JsonResponse
from datetime import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from reportlab.lib.utils import ImageReader
from botocore.client import Config
from django.template.loader import render_to_string
from xhtml2pdf import pisa

def generate_certificate_html(name, date):
    # Render the HTML template with dynamic data
    html_string = render_to_string('certificate.html', {'name': name, 'date': date})
    
    # Convert HTML to PDF
    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html_string, dest=pdf_buffer)
    pdf_buffer.seek(0)
    
    if pisa_status.err:
        return None
    return pdf_buffer

def upload_to_s3(file_obj, bucket_name, file_name):
    s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
    try:
        s3.upload_fileobj(file_obj, bucket_name, file_name)
        # Return the S3 URL
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        return s3_url
    except NoCredentialsError:
        return None
    
def generate_cloudfront_url(file_name, cloudfront_domain):
    return f"https://{cloudfront_domain}/{file_name}"

    


class CertificateViewSet(viewsets.ModelViewSet):
    @action(detail=False,methods=['get'])
    def get_certificate(self, request):
    # Extract name and date from request (for example purposes, using fixed values)
        name = request.GET.get('name', 'John Doe')
        date = datetime.now().strftime("%Y-%m-%d")

        # Generate the certificate as PDF
        certificate_buffer = generate_certificate_html(name, date)

        # Define S3 bucket and file name
        bucket_name = 'tecc-media'
        file_name = f'certificates/{name}_{date}.pdf'

        # Upload to S3
        s3_url = upload_to_s3(certificate_buffer, bucket_name, file_name)
        if s3_url:
            # Generate the CloudFront URL
            cloudfront_domain = 'd1gt2w0mc3uw79.cloudfront.net'  # Replace with your CloudFront domain
            cloudfront_url = generate_cloudfront_url(file_name, cloudfront_domain)
            return JsonResponse({'url': cloudfront_url})
        else:
            return JsonResponse({'error': 'Failed to upload certificate'}, status=500)
            
        