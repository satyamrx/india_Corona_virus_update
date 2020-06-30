import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier 
# create an object to ToastNotifier class 
n = ToastNotifier() 

# corona virus update link
def getdata(url):
    r=requests.get(url)
    return r.text
htmldata=getdata("https://www.mohfw.gov.in/")
soup = BeautifulSoup(htmldata, 'html.parser')
#print(soup.prettify())
mydata_str=""
for tr in soup.find_all('tbody')[0].find_all("tr"):
#print(tr.get_text())
    mydata_str +=tr.get_text().lower()
mydata_str=mydata_str[1:]
item_list=mydata_str.split("\n\n")
data_list=[]
for item in item_list[37:41]:
    data_list.append(item.split("\n"))
# print(data_list[0][2])
# print(data_list[1][0])
# print(data_list[2][1])
# print(data_list[3][1])
result="Active Cases :"+str(data_list[0][2])+ "\nCured :"+str(data_list[1][0])+"\nDeaths :"+str(data_list[2][1])+"\nTotal Confirmed cases :"+str(data_list[3][1])
n.show_toast("corona virus update",result, duration = 10,icon_path="img.ico" )


