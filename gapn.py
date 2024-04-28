import requests
import sys
import os

def download_package(package_name):
    url = f"https://package-pln.neoncorp.eu.org/linux/{package_name}"
    response = requests.get(url, allow_redirects=True)

    if response.status_code == 500:
        print("500: Server Error")
        return

    if response.status_code == 404:
        print("E: Package Not Found")
        return

    content_type = response.headers['content-type']
    if not content_type.startswith('application/octet-stream'):
        print(f"W: Unexpected content type: {content_type}")
        return

    file_path = os.path.join('/bin', package_name)
    with open(file_path, 'wb') as f:
        f.write(response.content)

    print(f"I: Package downloaded to {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid command format. Use: python script.py install <package_name>")
        sys.exit(1)

    cmd, package_name = sys.argv[1:3]
    if cmd != "install":
        print(f"Invalid command '{cmd}'. Use 'install' to download a package.")
        sys.exit(1)

    download_package(package_name)
