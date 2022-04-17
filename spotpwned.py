from curses import raw
import requests
from pydub import AudioSegment
from pydub.playback import play
import io

unauth_server_certificate_base = 'https://spclient.wg.spotify.com'
certificate_common_name = ['widevine', 'playready', 'fairplay', 'spotify-invalid']

def get_widevine_certificate():
       application_cert = requests.get(f"{unauth_server_certificate_base}/{certificate_common_name[0]}-license/v1/application-certificate").content
       return application_cert

def initiate_content_recovery():
       headers = {}

       raw_bytes = requests.get('https://audio-fa.scdn.co/audio/7224408a3f0264b85f31d477618db65c9df27058?1650241870_oKSDqx8mBpg2fURrCYcEyt7CqI-ZUTulzZD-e8BjCjE=', headers=headers)
       try:
              print(f"Content bytes :: {raw_bytes.headers['Content-Range']}")
       except:
              print('Could not find content range (not sent in header response?)')
       audio = AudioSegment.from_file(io.BytesIO(raw_bytes.content), format='raw', frame_rate=44100, channels=2, sample_width=2).remove_dc_offset()
       # reduce volume as random data could damage speakers
       quieter = audio - 3.5
       play(quieter)

initiate_content_recovery()