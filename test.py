import requests
import socket
import re




def main():
    
 in_addr = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 in_addr.connect((input("Enter a website URL : "),443))
 print("내부 IP  주소: " , in_addr.getsockname()[0])
    
 req = requests.get("https://ipconfig.kr",timeout=10)
 req.raise_for_status()
    
 match = re.search(r'<div class="card-ip-value">(\d{1,3}(?:\.\d{1,3}){3})</div>', req.text)
 if not match:
        raise RuntimeError("외부 IP 주소를 찾지 못했습니다.")
          
 out_addr = match.group(1)
 print("외부 IP 주소 : ", out_addr)
    
if __name__ == "__main__":
    print("hello python thanks for language model")
    main()
     