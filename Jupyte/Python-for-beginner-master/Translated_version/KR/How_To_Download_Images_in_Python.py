# pip install google_images_download
from google_images_download import google_images_download  
  
# ��ü����
response = google_images_download.googleimagesdownload()  
  
search_queries = [
'The smartphone also features an in display fingerprint sensor.', 
'The pop up selfie camera is placed aligning with the rear cameras.', 
'''In terms of storage Vivo V15 Pro could offer 
   up to 6GB of RAM and 128GB of onboard storage.''', 
'The smartphone could be fuelled by a 3 700mAh battery.', 
] 
  
  
def downloadimages(query): 
    # keywords�� �˻����Դϴ�
    # format�� �̹��� ���� �����Դϴ�
    # limit�� �ٿ�ε� �� �̹��� ���Դϴ�.
    # print urs�� �̹��� ���� URL�� �μ��ϴ� ���Դϴ�
    # size�� �������� ("large, medium, icon") �� ������ ���ִ� �̹��� ũ���Դϴ�
    # aspect ratio�� �ٿ�ε� �� �̹����� ���� �ʺ� ������ ��Ÿ���ϴ�. ("tall, square, wide, panoramic") 
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit":4, 
                 "print_urls":True, 
                 "size": "medium", 
                 "aspect_ratio": "panoramic"} 
    try: 
        response.download(arguments) 
      
    # NotFound ���� ����ó��     
    except FileNotFoundError:  
        arguments = {"keywords": query, 
                     "format": "jpg", 
                     "limit":4, 
                     "print_urls":True,  
                     "size": "medium"} 
                       
        # �˻��� ������ ���� ���� ����
        try: 
            # �־��� ���ڿ� ���� ���� �ٿ�ε�
            response.download(arguments)  
        except: 
            pass
  
# Driver Code 
for query in search_queries: 
    downloadimages(query)  
    print()
