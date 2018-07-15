#--- Yifan Xu ---
import itchat
import requests

# 登陆
itchat.auto_login(hotReload=True)

# 获取微信好友发的消息 根据消息回复
apiUrl = "http://www.tuling123.com/openapi/api"
def get_info(message):
    data = {
        'key': '2fd754128f0b4cdd8d83aa67945be352',
        'info': message,
        'userID': 'robot'
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        text = r['text']
        print("robot reply: %s" % text)
        return text

        pass
    except:
        return

# get_info("沐王府")
# <Response [200]> 200表示状态码，表示请求成功



# 发给相应好友
@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    defaultReply = '我知道了'
    # 搜索微信好友
    realFriend = itchat.search_friends(name='香菇Aimee')
    # 搜索真名
    realFriendName = realFriend[0]['UserName']
    # print(realFriendName)
    # 打印好友回复的信息
    print("message: %s"%msg['Text'])
    # 调用图灵接口
    reply = get_info(msg['Text'])
    if msg['FromUserName'] == realFriendName:
        itchat.send(reply,toUserName=realFriendName)

itchat.run()
