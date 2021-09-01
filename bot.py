import telepot
import time
from telepot.loop import MessageLoop
import pybithumb
# 코인을 입력하면 현재가, 24시간 동안의 저가/고가/평균가/거래량을 출력하는 자동화 봇

TOKEN = '' #빈칸처리

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == "text":
        user_input = msg["text"]
        #현재가 출력
        cur_price = pybithumb.get_current_price(user_input)
        message=user_input+"의 현재 가격은 "+str(cur_price)+"원 입니다."
        bot.sendMessage(chat_id, message)

        #24시간 동안의 저가, 고가, 평균가, 현재가, 거래량 튜플로 받기
        detail = pybithumb.get_market_detail(user_input)

        message2="24시간 동안 "+user_input+"의"

        # detail 4번째 인덱스가 현재가라 lst의 4번째 원소는 임의로 만들어줌
        lst = ["저가", "고가", "평균거래 금액", "empty", "거래량"]

        # for문을 통해 message2 병합
        for a in range(5):
            #detail 4번째 인덱스가 현재가라 a=3이면 continue
            if a == 3:
                continue
            else:
                message2 = message2 + "\n" + lst[a] + " : " + str(detail[a])
        #2번째 메세지 출력
        bot.sendMessage(chat_id, message2+"\n입니다.")

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)
