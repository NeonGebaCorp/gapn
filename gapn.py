import requests
import sys
command = sys.argv[1]
package = sys.argv[2]
if command == "install" :
  print("[Downloading]: Downloading Package")
  url = "https://package-pln.neoncorp.eu.org".package
  r = requests.get(url)

  with open('/bin', 'wb') as f:
  f.write(r.content)

  # Retrieve HTTP meta-data
  print(r.status_code)
  print(r.headers['content-type'])
  print(r.encoding)
  if r.status_code == 500 :
    print("500: Server Error")
  if r.status_code == 404
    print("E: Package Not Found")
