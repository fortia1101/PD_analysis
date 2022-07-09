import time, random, sys

def n_roop1(time_start, pred=None, char=[], target=None):
    for i in range(len(char)):
        pred = char[i]
        if (pred == target):
            print(f'あなたのパスワード：{pred}')
            time_end = time.time()
            time.sleep(1) # 時間計測終了
            print(f'解析にかかった時間：{time_end - time_start}')
            sys.exit()
        else:
            continue
    else:
        return

def n_roop2(time_start, pred=None, char=[], target=None):
    for i in range(len(char)):
        for j in range(len(char)):
            pred = char[i] + char[j]
            if (pred == target):
                print(f'あなたのパスワード：{pred}')
                time_end = time.time()
                time.sleep(1) # 時間計測終了
                print(f'解析にかかった時間：{time_end - time_start}')
                sys.exit()
            else:
                continue
        else:
            continue
    else:
        return

def n_roop3(time_start, pred=None, char=[], target=None):
    for i in range(len(char)):
        for j in range(len(char)):
            for k in range(len(char)):
                pred = char[i] + char[j] + char[k]
                if (pred == target):
                    print(f'あなたのパスワード：{pred}')
                    time_end = time.time()
                    time.sleep(1) # 時間計測終了
                    print(f'解析にかかった時間：{time_end - time_start}')
                    sys.exit()
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        return

def n_roop4(time_start, pred=None, char=[], target=None):
    for i in range(len(char)):
        for j in range(len(char)):
            for k in range(len(char)):
                for l in range(len(char)):
                    pred = char[i] + char[j] + char[k] + char[l]
                    if (pred == target):
                        print(f'あなたのパスワード：{pred}')
                        time_end = time.time()
                        time.sleep(1) # 時間計測終了
                        print(f'解析にかかった時間：{time_end - time_start}')
                        sys.exit()
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        return

def n_roop5(time_start, pred=None, char=[], target=None):
    for i in range(len(char)):
        for j in range(len(char)):
            for k in range(len(char)):
                for l in range(len(char)):
                    for m in range(len(char)):
                        pred = char[i] + char[j] + char[k] + char[l] + char[m]
                        if (pred == target):
                            print(f'あなたのパスワード：{pred}')
                            time_end = time.time()
                            time.sleep(1) # 時間計測終了
                            print(f'解析にかかった時間：{time_end - time_start}')
                            sys.exit()
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        return

def n_roop6(time_start, pred=None, char=[], target=None):
    for i in range(len(char)):
        for j in range(len(char)):
            for k in range(len(char)):
                for l in range(len(char)):
                    for m in range(len(char)):
                        for n in range(len(char)):
                            pred = char[i] + char[j] + char[k] + char[l] + char[m] + char[n]
                            if (pred == target):
                                print(f'あなたのパスワード：{pred}')
                                time_end = time.time()
                                time.sleep(1) # 時間計測終了
                                print(f'解析にかかった時間：{time_end - time_start}')
                                sys.exit()
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        return

def n_roop7(time_start, p=None, char=[], target=None):
    for i in range(len(char)):
        for j in range(len(char)):
            for k in range(len(char)):
                for l in range(len(char)):
                    for m in range(len(char)):
                        for n in range(len(char)):
                            for o in range(len(char)):
                                pred = char[i] + char[j] + char[k] + char[l] + char[m] + char[n] + char[o]
                                if (pred == target):
                                    print(f'あなたのパスワード：{pred}')
                                    time_end = time.time()
                                    time.sleep(1) # 時間計測終了
                                    print(f'解析にかかった時間：{time_end - time_start}')
                                    sys.exit()
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        return

def n_roop8(time_start, pred=None, char=[], target=None):
    for i in range(len(char)):
        for i in range(len(char)):
            for i in range(len(char)):
                for i in range(len(char)):
                    for i in range(len(char)):
                        for i in range(len(char)):
                            for i in range(len(char)):
                                for i in range(len(char)):
                                    pred = char[i] + char[j] + char[k] + char[l] + char[m] + char[n] + char[o] + char[p]
                                    if (pred == target):
                                        print(f'あなたのパスワード：{pred}')
                                        time_end = time.time()
                                        time.sleep(1) # 時間計測終了
                                        print(f'解析にかかった時間：{time_end - time_start}')
                                        sys.exit()
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        return


# 総当たりによるパスワード解析時間の計測
def PD_analysis():
    char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'r', 't', 'y', 'u', \
        'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', \
        'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', \
        'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    if (char == []):
        print('引数charが空です')
        exit(1) # エラーを示すexit

    # 本処理
    pred = None
    try:
        target = input('パスワードを入力してください(大小英数字のみ使用, 8文字まで) >> ') # Success Value
        if (len(target) > 8):
            print('8文字を超えています')
            exit(1)

        # random.shuffle(char) # 配列の要素をシャッフル

        time_start = time.time() # 時間計測開始
        
        n_roop1(time_start, pred, char, target)
        n_roop2(time_start, pred, char, target)
        n_roop3(time_start, pred, char, target)
        n_roop4(time_start, pred, char, target)
        n_roop5(time_start, pred, char, target)
        n_roop6(time_start, pred, char, target)
        n_roop7(time_start, pred, char, target)
        n_roop8(time_start, pred, char, target)

    except KeyboardInterrupt:
        print('KeyboardInterrupt例外が発生しました')


# 解析開始
if (__name__ == '__main__'):
    PD_analysis()
