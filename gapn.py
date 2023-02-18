import requests
import sys
cmds = sys.argv[1]
package = sys.argv[2]
if cmds == "install" :
  
  print("[Downloading]: Downloading Package")
  url = "https://package-pln.neoncorp.eu.org/linux/",package
  r = requests.get(url, allow_redirects=True)




  # Retrieve HTTP meta-data
  print(r.status_code)
  print(r.headers['content-type'])
  print(r.encoding)
  if r.status_code == 500 :
    print("500: Server Error")
  else:
    if r.status_code == 404 :
      print("E: Package Not Found")
    else:
      open('/bin/',package, 'wb').write(r.content)

if __name__=="__main__" :
  print("Invalid Command, Please write --help")
