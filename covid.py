import requests
import json
import requests
a=0
cz=[]
for a in range(50):
    pincode=[400001,400002,400003,400004,400005,400006,400007,400008,400009,400010,400011,400012,400013,400014,400015,400016,400017,400018,400019,400020,400021,400025,400026,400027,400028,400029,400030,400031,400032,400033,400034,400035,400037,400049,400050,400051,400052,400053,400054,400055,400056,400057,400058,400059,400060,400061,400062,400063,400064,400065,400066,400067,400068,400069,400090,400091,400092,400093,400095,400096,400097,400098,400099,400101,400102,400103,400104]
    data={'key':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtYWlsSWRlbnRpdHkiOiJma2hhbjE2MjAwMEBnbWFpbC5jb20ifQ.gWIDHg5o72VCxmf04b2PyW19xaBMSrXV63Au0XU0H7Y', "pincode": pincode[a]}
    response=requests.post('https://data.geoiq.io/dataapis/v1.0/covid/pincodecheck',json.dumps(data))
    string=response.content
    string=string.decode("utf-8")
    index = string.find('"containmentZoneNames"')
    string= string[index:]
    index = string.find('[')
    string= string[index:]
    index = string.find('}, "status"')
    string=string[:index]
    flag=0
    x=0
    y=0
    li = list(string.split('"'))
    for x in range(len(li)):
        if li[x]==', ':
            flag=flag+1
    for y in range(flag):
        li.remove(', ')

    x=0
    for x in range(len(li)):
        cz.append(li[x])
x=0
for x in range(len(cz)):
    print(cz[x])
