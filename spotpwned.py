import requests
import sounddevice as sd

_unauthServerCertificateBase = "https://spclient.wg.spotify.com"
_certificateCommonName = ['widevine', 'playready', 'fairplay', 'spotify-invalid']

def get_widevine_certificate():
       application_cert = requests.get(f"{_unauthServerCertificateBase}/{_certificateCommonName[0]}-license/v1/application-certificate").content
       return application_cert

def initiate_content_recovery():
       header = {
                     'Accept': '*/*',
                     'Accept-Encoding': 'identity',
                     'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8',
                     'Connection': 'keep-alive',
                     'Host': 'audio-fa.scdn.co',
                     'Origin': 'https://open.spotify.com',
                     'Range': 'bytes=0-325213',
                     'Referer': 'https://open.spotify.com/',
                     'Sec-Fetch-Dest': 'empty',
                     'Sec-Fetch-Mode': 'cors',
                     'Sec-Fetch-Site': 'cross-site',
                     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.133 Safari/537.36',
                     'sec-ch-ua-mobile': '?0',
                     'sec-ch-ua-platform': 'Linux'
              }

       raw_bytes = requests.get('https://audio-fa.scdn.co/audio/7224408a3f0264b85f31d477618db65c9df27058?1650241870_oKSDqx8mBpg2fURrCYcEyt7CqI-ZUTulzZD-e8BjCjE=', headers=header)
       print(f"Content bytes :: {raw_bytes.headers['Content-Range']}")
       sd.play(raw_bytes.content, 44100)

print(f"G0t certificate :: {get_widevine_certificate()}")