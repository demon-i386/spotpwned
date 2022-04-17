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

       raw_bytes = requests.get('https://audio-fa.scdn.co/audio/8ba8885b19dd6fdfdd9beaf9a1a093492190ad68?1650315911_noN25xZ7UCEMxkdJ9f-MObdZNPYt98Rk3yjffyObcvk=', headers=headers)
       try:
              print(f"Content bytes :: {raw_bytes.headers['Content-Range']}")
       except:
              print('Could not find content range (not sent in header response?)')
       audio = AudioSegment.from_file(io.BytesIO(raw_bytes.content), format='mp4', frame_rate=44100, channels=2, sample_width=2).remove_dc_offset()
       # reduce volume as random data could damage speakers
       quieter = audio - 3.5
       play(quieter)

initiate_content_recovery()