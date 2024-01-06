from instapy import InstaPy
from dotenv import load_dotenv
import os

load_dotenv()
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

def like_ari_stuff():
    session = InstaPy(username=USER_NAME, password=PASSWORD, headless_browser=True, want_check_browser=False)
    session.set_quota_supervisor(enabled=True, peak_comments_daily=10, peak_comments_hourly=1)
    session.login()
    session.set_do_follow(enabled=True, percentage=100)
    session.set_do_like(True, percentage=100)
    session.interact_by_users(['badgirlaririfromthebronx'])
    session.end()
    
like_ari_stuff()