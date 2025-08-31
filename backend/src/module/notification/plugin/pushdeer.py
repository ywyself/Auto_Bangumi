import logging

from module.models import Notification
from module.network import RequestContent

logger = logging.getLogger(__name__)


class PushDeerNotification(RequestContent):
    def __init__(self, token, **kwargs):
        super().__init__()
        self.token = token
        self.notification_url = "https://api2.pushdeer.com/message/push"

    def post_msg(self, notify: Notification) -> bool:
        text = f"🎉 第{notify.season}季第{notify.episode}集 {notify.official_title}"
        data = {"type": "text", "text": text, "desp": "AutoBangumi", "pushkey": self.token}
        resp = self.post_data(self.notification_url, data)
        logger.debug(f"PushDeer notification: {resp.status_code}")
        return resp.status_code == 200
