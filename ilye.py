import vk_api
import schedule

vk_session = vk_api.VkApi(token='917abf87d531a4e9be65641d3b060af430b8fa97c94b58c423e89a8cf07be46c435076217997edf2b7c31')
vk = vk_session.get_api()
user_id = 456585601

def auto_date(vk):
    try:
        vk.messages.send(peer_id=user_id, random_id='1', message='С др кста')
    except Exception as er:
        print(er)

def msg():
    bot.send_message(message.chat.id, answer)

schedule.every().day.at("3:00").do(msg)
while True:
    schedule.run_pending()
    time.sleep(1)
