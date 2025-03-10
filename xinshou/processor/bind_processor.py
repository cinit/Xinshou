from xinshou import wx
from .processor import Processor


class BindProcessor(Processor):
    def _process_event(self, m: wx.receive.Event) -> wx.reply.Msg:
        to_user = m.from_user_name
        from_user = m.to_user_name
        content = m.event_key
        res = wx.reply.TextMsg(to_user, from_user, content)
        return res
