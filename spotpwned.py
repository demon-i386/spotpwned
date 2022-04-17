import requests
import sounddevice as sd

unauth_server_certificate_base = 'https://spclient.wg.spotify.com'
certificate_common_name = ['widevine', 'playready', 'fairplay', 'spotify-invalid']


def get_widevine_certificate():
       application_cert = requests.get(f"{unauth_server_certificate_base}/{certificate_common_name[0]}-license/v1/application-certificate").content
       return application_cert


def initiate_content_recovery():
       headers = {}

       raw_bytes = requests.get('https://audio-fa.scdn.co/audio/7224408a3f0264b85f31d477618db65c9df27058?1650241870_oKSDqx8mBpg2fURrCYcEyt7CqI-ZUTulzZD-e8BjCjE=', headers)
       print(f"Content bytes :: {raw_bytes.headers['Content-Range']}")
       sd.play(raw_bytes.content, 44100)

print(f"G0t certificate :: {get_widevine_certificate()}" + ('\n'*3))