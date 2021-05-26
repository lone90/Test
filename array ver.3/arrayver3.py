import random
import os
import keyboard

#함수 정의

def Mixsentence(sen):

    senlength = len(sen)
    index = list(range(senlength))
    mixed_sen = list(range(senlength))

    if (index == list(range(len(sen)))):
        random.shuffle((index))

    for i in range(senlength):
        mixed_sen[i] = sen[index[i]]
    return mixed_sen


def Test(sen, ans, Wrongsen):

    #문제 출력
    print(sen)

    #답 입력받기
    answer = input().split()
    #답 확인

    if answer == ans:
        return 1
    else :
        Wrongsen.append(ans)
        print('답을 보시려면 tab키를 눌러주시고 한번 더 하려면 아무키나 눌러주세요')
        if getkey('tab'):
            print(" ".join(ans))
            time.sleep(1)



def getkey(name):
        if keyboard.read_key() == name:
            return 1
        else :
            return 0



#시작


File = open("Text.txt", 'r')

Wrongsen = []

while(1):

    #문장 읽어서 답지 생성
    sentence = File.readline()

    Answer = sentence.split()

    Question = Mixsentence(Answer)

    #debug

    #문장 없을 시 오답

    if not sentence:
        print('틀린문제가', len(Wrongsen), '개 입니다', '\n틀린문제를 복습하시려면 R키를 눌러주세요')

        if getkey('r'):
            for i in range(0, len(Wrongsen)):
                sentence = Wrongsen[i]

                Answer = sentence.split()

                Question = Mixsentence(Answer)

                while (1):
                    if Test(Question, Answer, Wrongsen2):
                        break
                    os.system('cls')

    while(1):
        if Test(Question, Answer, Wrongsen):
            break
        os.system('cls')