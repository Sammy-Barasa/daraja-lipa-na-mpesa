
import base64
from config import Config


BusinessShortCode=Config["BUSINESS_SHORT_CODE"]
PassKey=Config["PASS_KEY"]

def get_password(timestamp):
    encode_= BusinessShortCode + PassKey + timestamp
    encoded_=base64.b64encode(encode_.encode())
    decoded_pass=encoded_.decode('utf-8')
    print(decoded_pass)
    return decoded_pass



