import requests
for x in range(100):
        url='https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/viewform'
        submission ={
                
	         'entry.1156409':'Tejesh Vaish'
	           ,'entry.210055283':'190908',
	           'entry.771155771':'Yes',
	            'entry.446099277':'https://github.com/tejeshvaish/8-languages-in-8-weeks'
              
              
        } 
        requests.post(url, submission)
