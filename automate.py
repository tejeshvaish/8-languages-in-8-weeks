import urllib
from urllib.request import Request 

user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
header={'User-Agent' : user_agent}
url = "https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/viewform"
# values from your form. You will need to include any hidden variables if you want to..
values= {
'Name': 'Tejesh Vaish',
'Roll Number':'190908',
'Did you use a python script':'Yes',
'Link to github repo/pastebin where I can see your script':'https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/viewform'
}
print(values)
data = urllib.parse.urlencode(values)
Request(url, data,header )
