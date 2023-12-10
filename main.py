from speedTest import SpeedTest
from x import Twitter

USER = 'mateuszkowalczyk7@gmail.com'
PASS = 'Selenium123!'
provider_x_account = "Orange_Polska"

download = 30
upload = 3

test = SpeedTest()

speeds = test.getSpeed()
actual_download = speeds['download speed']
actual_upload = speeds['upload speed']


if actual_download < download or actual_upload < upload:
    twitter = Twitter()

    twitter.log_in(USER, PASS)

    twitter.post_on_x(download, upload, actual_download, actual_upload, provider_x_account)





