import re
sample_html = ("<img src='https://example.com/image1.jpg'>"
               " <img src='http://example.com/image2.png'>"
               " <img src='https://example.com/image3.gif'>"
               " <img src='https://example.com/image.txt'>"
               " <img src='https://example.com/image.log'>")
def extract_image_links(html_text):
    re_cod = r'(https?://[^\'" >]+(?:\.[jpg]\w{2}))'
    html_text = re.findall(re_cod, html_text)
    return html_text


image_links = extract_image_links(sample_html)
if image_links:
  for image_link in image_links:
    print(image_link)
else:
  print("Нет ссылок с картинками в HTML тексте.")