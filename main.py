import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
vk = vk_api.VkApi(token='5686e34f6caf6804e545726b9afbf2054954d2eda3558176ed0948e12e85dc70abb100c879b189f5134a0')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk, 213666706)
give = vk.get_api()
import os.path
#from vk_maria import Vk, types
#from vk_maria.dispatcher import Dispatcher
#from vk_maria.dispatcher.filters import AbstractFilter

class txts:
	def ban_txt(id, user_id):
		if os.path.exists(str(id)):
			if os.path.isfile(str(id) + '\Ban' + str(user_id) + '.txt'):
				with open(str(id) + '\Ban' + str(user_id) + '.txt', 'w+') as f:
					f.write('0')
			else:
				with open(str(id) + '\Ban' + str(user_id) + '.txt', 'w+') as f:
					f.write('0')
		else:
			os.mkdir(str(id))
			with open(str(id) + '\Ban' + str(user_id) + '.txt', 'w+') as a:
				a.write('0')
	def status_txt(id, user_id):
		if user_id == '586400457':
			if os.path.exists(str(id)):
				if os.path.isfile(str(id) + '\Status' + str(user_id) + '.txt'):
					with open(str(id) + '\Status' + str(user_id) + '.txt', 'w+') as f:
						f.write('6')
				else:
					with open(str(id) + '\Status' + str(user_id) + '.txt', 'w+') as f:
						f.write('6')
			else:
				os.mkdir(str(id))
				with open(str(id) + '\Status' + str(user_id) + '.txt', 'w+') as a:
					a.write('6')
		else:
			if os.path.exists(str(id)):
				if os.path.isfile(str(id) + '\Status' + str(user_id) + '.txt'):
					with open(str(id) + '\Status' + str(user_id) + '.txt', 'w+') as f:
						f.write('1')
				else:
					with open(str(id) + '\Status' + str(user_id) + '.txt', 'w+') as f:
						f.write('1')
			else:
				os.mkdir(str(id))
				with open(str(id) + '\Status' + str(user_id) + '.txt', 'w+') as a:
					a.write('1')
	def create_all_folder(id, user_id):
		if os.path.exists(str(id) + '\Status' + str(user_id) + '.txt'):
			print('+')
		else:
			txts.ban_txt(id, user_id)
			txts.status_txt(id, user_id)
			print('-')
def send(id, text):
    vk.method('messages.send', {'chat_id' : id, 'key' : '398941b94cbc56aff55624d11a2bd13bc29618f7', 'server' : "https://lp.vk.com/wh213666706", 'ts' : '108', 'message' : text, 'random_id' : 0})
def msg_del(id, msg_id):
    vk.method('messages.delete', {'chat_id' : id, 'message_ids' : msg_id, 'delete_for_all' : 1})
def add_user(id, user_id):
    vk.method('messages.addChatUser', {'chat_id' : id, 'user_id' : user_id})
def edit_ChatName(id, text):
    vk.method('messages.editChat', {'chat_id' : id, 'title' : text})
def pin(id, msg_id):
    vk.method('messages.pin', {'chat_id' : id, 'message_ids' : msg_id})
def kick(id, idu):
    vk.method('messages.removeChatUser', {'chat_id' : id, 'user_id' : idu})
def get_msgID(id):
    vk.method('messages.getById', {'chat_id' : id, 'message_ids' : 10})
def userban(id, user_id):
	if os.path.exists(str(id)):
		if os.path.isfile(str(id) + '\Ban' + str(user_id) + '.txt'):
			with open(str(id) + '\Ban' + str(user_id) + '.txt', 'w+') as f:
				f.write('1')
			kick(id, user_id)
			send(id, 'Пользователь забанен.')
		else:
			with open(str(id) + '\Ban' + str(user_id) + '.txt', 'w+') as f:
				f.write('1')
			kick(id, user_id)
			send(id, 'Пользователь забанен.')
	else:
		os.mkdir(str(id))
		with open(str(id) + '\Ban' + str(user_id) + '.txt', 'w+') as a:
			a.write('1')
			kick(id, user_id)
			send(id, 'Пользователь забанен.')
def userunban(id, user_id):
	if os.path.exists(str(id)):
		if os.path.isfile(str(id) + '\Ban' + str(user_id) + '.txt'):
			with open(str(id) + '\Ban' + str(user_id) + '.txt', 'w+') as f:
				f.write('0')
			send(id, 'Пользователь разбанен.')
		else:
			with open(str(id) + '\Ban' + str(user_id) + '.txt', 'w+') as f:
				f.write('0')
			send(id, 'Пользователь разбанен.')
	else:
		os.mkdir(str(id))
		with open(str(id) + '\Ban' + str(user_id) + '.txt', 'w+') as a:
			a.write('0')
			send(id, 'Пользователь разбанен.')
def check_join_user(id, user_id):
    with open(str(id) + '\Ban' + str(user_id) + '.txt', 'r') as a:
        ban_status = a.read()
    if ban_status == '1':
        kick(id, user_id)
        send(id, 'Данный пользователь забанен в беседе. Пользователь исключён')
    else:
        send(id, 'Пользователь не имеет действующего бана в этой беседе.')


#class ChatInviteUser(AbstractFilter):
#    def check(self, event: types.MessageEvent):
#        if 'action' in event.message:
#            return event.message.action.type == "chat_invite_user"

	

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        msg = str(event.message.text)
        id = event.chat_id
        user_id = event.obj['message']['from_id']
        if "!кик " in msg:
            if event.from_chat:
                txts.create_all_folder(id, user_id)
                with open(str(id) + '\Status' + str(user_id) + '.txt', 'r') as f:
                    user_status = f.read()
                if int(user_status) > 1:
                    id_u = msg.replace("!кик ", "")
                    if "@" in id_u:
                        id_uu = id_u.split("|")[0]
                        id_u = id_uu.replace('[', '')
                        if "id" in id_u:
                            id_u = id_u.replace("id", "")
                    kick(id, int(id_u))
                    send(id, 'Пользователь кикнут. \n Пользователь который был кикнут: https://vk.com/id' + id_u)
                else:
                    send(id, 'Для этого действия вам необходим статус [2] Хелпер, сейчас ваш статус [1] Обычный смертный')
        if '!edit_name ' in msg:
            if event.from_chat:
                txts.create_all_folder(id, user_id)
                with open(str(id) + '\Status' + str(user_id) + '.txt', 'r') as f:
                    user_status = f.read()
                if int(user_status) > 2:
                    new_name = msg.replace("!edit_name ", "")
                    edit_ChatName(id, new_name)
                    send(id, 'Название беседы изменено.')
                elif int(user_status) == 2:
                    send(id, 'Для этого действия вам необходим статус [3] Модератор, сейчас ваш статус [2] Хелпер')
                else:
                    send(id, 'Для этого действия вам необходим статус [3] Модератор, сейчас ваш статус [1] Обычный смертный')
        if '!бан ' in msg:
            if event.from_chat:
                txts.create_all_folder(id, user_id)
                with open(str(id) + '\Status' + str(user_id) + '.txt', 'r') as f:
                    user_status = f.read()
                if int(user_status) > 2:
                    banid = msg.replace("!бан ", "")
                    id_uu = banid.split("|")[0]
                    id_u = id_uu.replace('[', '')
                    user_id = id_u.replace('id', '')
                    userban(id, int(user_id))
                elif int(user_status) == 2:
                    send(id, 'Для этого действия вам необходим статус [3] Модератор, сейчас ваш статус [2] Хелпер')
                else:
                    send(id, 'Для этого действия вам необходим статус [3] Модератор, сейчас ваш статус [1] Обычный смертный')
        if '!разбан ' in msg:
            if event.from_chat:
                txts.create_all_folder(id, user_id)
                with open(str(id) + '\Status' + str(user_id) + '.txt', 'r') as f:
                    user_status = f.read()
                if int(user_status) > 3:
                    banid = msg.replace("!разбан ", "")
                    id_uu = banid.split("|")[0]
                    id_u = id_uu.replace('[', '')
                    user_id = id_u.replace('id', '')
                    userunban(id, int(user_id))
                elif int(user_status) == 3:
                    send(id, 'Для этого действия вам необходим статус [4] Админ, сейчас ваш статус [3] Модератор')
                elif int(user_status) == 2:
                    send(id, 'Для этого действия вам необходим статус [4] Админ, сейчас ваш статус [2] Хелпер')
                else:
                    send(id, 'Для этого действия вам необходим статус [4] Админ, сейчас ваш статус [1] Обычный смертный')

#vk = Vk(access_token='5686e34f6caf6804e545726b9afbf2054954d2eda3558176ed0948e12e85dc70abb100c879b189f5134a0')
#dp = Dispatcher(vk)


#@dp.event_handler(types.EventType.MESSAGE_NEW, ChatInviteUser)
#def handle_chat_invite_user(event: types.MessageEvent):
#    event.answer(f"Добро пожаловать в беседу, {event.message.from_id=}")


#if __name__ == '__main__':
#    dp.start_polling(debug=True)
