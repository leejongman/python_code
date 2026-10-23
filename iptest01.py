import requests
import socket
import re


class IP_ADDRESS:

  def get_ip_address(self): 
    self.in_addr = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.in_addr.connect((input("Enter a Website : "),443))
    print("local 내부IP 주소: ",self.in_addr.getsockname()[0])

    
  def get_public_ip(self):   
    req = requests.get("http://ipconfig.kr",timeout = 10)
    req.raise_for_status()
    return req
    
  def match_ip(self):
    match = re.search(r'<div class="card-ip-value">(\d{1,3}(?:\.\d{1,3}){3})</div>',self.get_public_ip().text)
 
    if not match:
      raise RuntimeError("외부 IP 주소를 찾지 못했습니다.")
    return match

  def print_ip(self):
    out_addr = self.match_ip().group(1)
    print("public 외부 IP 주소 : ",out_addr)
    out_addr = self.in_addr.getpeername()[0]
    print("상대 서버 IP 주소 : ",out_addr)
    
def main():
    ip_addr = IP_ADDRESS()
    ip_addr.get_ip_address()
    ip_addr.get_public_ip()
    ip_addr.match_ip()
    ip_addr.print_ip()

if __name__ == "__main__":
      main()
      print("Hello Python World thanks!!")
    