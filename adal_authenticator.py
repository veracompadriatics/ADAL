import ConfigParser
import json
import logging
import os
import sys
import adal

dir_path = os.path.abspath(os.path.dirname(sys.argv[0]))
print 'Current dir: ' + dir_path
try:
  Config = ConfigParser.ConfigParser()
  Config.read(dir_path+'/adal.ini')
  Config.sections()
  directory=Config.get('directory','directory')
  clientid=Config.get('directory','clientid')
except Exception, e:
  print "No adal.ini or Missing Active Directory configuration parameters in adal.ini!"
  sys.exit(1)

username=os.environ['PAM_USER']
print "user "+username
password=''
for line in sys.stdin:
  password=password + line
print "pass "+password

authority_url = ('https://login.windows.net/' + directory)
RESOURCE = '00000002-0000-0000-c000-000000000000'
try:
  context = adal.AuthenticationContext(authority_url)
  token = context.acquire_token_with_username_password(RESOURCE, username, password, clientid)
#  print(json.dumps(token, indent=2))
  print "Auth success"
  sys.exit(0)
except Exception, e:
  print "Auth failed"
  sys.exit(1)
