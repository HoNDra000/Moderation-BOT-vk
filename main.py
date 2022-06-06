import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
vk = vk_api.VkApi(token='5686e34f6caf6804e545726b9afbf2054954d2eda3558176ed0948e12e85dc70abb100c879b189f5134a0')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk, 213666706)
give = vk.get_api()
import os.path

def send(id, text):
	vk.method('messages.send', {'chat_id' : id, 'key' : '398941b94cbc56aff55624d11a2bd13bc29618f7', 'server' : "https://lp.vk.com/wh213666706", 'ts' : '108', 'message' : text, 'random_id' : get_random_id()})
def msg_del(id, msg_id):
    vk.method('messages.delete', {'chat_id' : id, 'message_ids' : msg_id, 'delete_for_all' : 1})
def add_user(id, user_id):
    vk.method('messages.addChatUser', {'chat_id' : id, 'user_id' : user_id})
def edit_ChatName(id, text):
    vk.method('messages.editChat', {'chat_id' : id, 'title' : text})
def pin(id, msg_id):
    vk.method('messages.pin', {'chat_id' : id, 'message_ids' : msg_id})
def kick(id, user_id):
    vk.method('messages.removeChatUser', {'chat_id' : id, 'user_id' : user_id})
def get_msgID(id):
    vk.method('messages.getById', {'chat_id' : id, 'message_ids' : 10})

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        id = event.chat_id
        a = str(652064171)#str(get_random_id())
        if 'check server stable' in str(event):
            if event.from_chat:
                kick(id, a)
                send(id, 'Server stable.')
