import requests
import sys
command = sys.argv[1]

if command == "install" :
  package = sys.argv[2]
  print("[Downloading]: Downloading Package")
  url = "https://package-pln.neoncorp.eu.org/linux".package
  r = requests.get(url)


  # Retrieve HTTP meta-data
  print(r.status_code)
  print(r.headers['content-type'])
  print(r.encoding)
  if r.status_code == 500 :
    print("500: Server Error")
  else:
    if r.status_code == 404
      print("E: Package Not Found")
    else:
      with open('/bin', 'wb') as f:
      f.write(r.content)

if __name__=="__main__" :
  print("Invalid Command, Please write --help")
