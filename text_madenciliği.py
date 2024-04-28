import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

url = 'https://www.kariyer.net/is-ilanlari?kw=muhasebe&huac=1'

# Web sitesinden veriyi al
response = requests.get(url)

# İstek başarılıysa, içeriği analiz et
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tüm span etiketlerini bul
    span_etiketleri = soup.find_all('span', class_='k-ad-card-title multiline')
    span_etiketleri2 = soup.find_all('span', class_='location')
    span_etiketleri3 = soup.find_all('span', class_='work-model')
    span_etiketleri4 = soup.find_all('span', class_='text')

    div_etiketi=soup.find_all('div', class_='subtitle')
    

    
    
    # Her bir span etiketi için başlık ve konumu çıkar ve yazdır
    for title_span, location_span, jop_name ,working_position,working_time in zip(span_etiketleri, span_etiketleri2,div_etiketi,span_etiketleri3,span_etiketleri4):
        title = title_span.text.strip()
        location = location_span.text.strip()
        jop_name=jop_name.text.strip()
        working_position=working_position.text.strip()
        working_time=working_time.text.strip()

        


        print(jop_name, ",", title, ",", location,",",working_position,",",working_time)
else:
    print("İstek başarısız oldu. Durum kodu:", response.status_code)

for i in range(1,5):
    url2=url+"&cp="+str(i)
    print(url2)
    response=requests.get(url2)

    if response.status_code== 200:
        soup=BeautifulSoup(response.content,"html.parser")
        span_etiketleri = soup.find_all('span', class_='k-ad-card-title multiline')
        span_etiketleri2=soup.find_all('span',class_='location')
        span_etiketleri3=soup.find_all('span',class_='work-model')
        span_etiketleri4=soup.find_all('span',class_='text')
        div_etiketi=soup.find_all('div',class_='subtitle')

        for title_span,location_span,jop_name,working_position,working_time in zip(span_etiketleri,span_etiketleri2,div_etiketi,span_etiketleri3,span_etiketleri4):
            title=title_span.text.strip()
            location=location_span.text.strip()
            jop_name=jop_name.text.strip()
            working_position=working_position.text.strip()
            working_time=working_time.text.strip()

            print(jop_name,",",title,",",location,",",working_position,",",working_time)
    else:
        print("istek basarısız oldu. Durum kodu:",response.status_code)

