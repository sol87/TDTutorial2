# coding=utf8
from random import randint

# 提示用户游戏开始
print "游戏开始"
# 生成一个随机整数作为谜底
result = randint(1, 100)
# 循环5次
answer_count = 5
while answer_count > 0:
    # 在一次循环内
    # 要求用户输入一个数字
    user_answer = input("请输入一个1-100的数字：")
    # 对比用户的数字和谜底
    # 如果大于谜底，则提示“数字过大”
    if user_answer > result:
        print "too big"
    # 如果小于谜底，则提示“数字过小”
    elif user_answer < result:
        print "too small"
    # 否则提示“回答正确”，并退出循环
    else:
        print "right"
        break
    answer_count -= 1

# 如果剩余次数大于0，则提示“恭喜过关”；否则提示GameOver
if answer_count > 0:
    print "恭喜通关"
    print "剩余次数为：", answer_count, "次"
else:
    print "Sorry, 你失败了。"
    print "Game Over."
