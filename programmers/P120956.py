# 옹알이(1)
def solution(babbling):
    vocas = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for bab in babbling:
        for voca in vocas:
            if bab.__contains__(voca):
                bab = bab.replace(voca, ' ');
        
        bab = bab.strip()
        if bab == "":
            answer += 1
            
        # 잘못 접근했던 풀이
        # idxs = [i for i, x in enumerate(vocas) if x in bab]
        # for idx in idxs:
        #    bab = bab.replace(vocas[idx], "")
        # voca를 갖는 해당 인덱스를 찾아서 인덱스 위치의 단어를 지워주고 count하려 했으나,
        # 해당 인덱스 단어를 제거했을 때 남은 글자들이 붙어서 vocas의 원소가 되는 예외가 있음(반례)
        # 이 경우를 커버하기 위해 공백을 넣어준 뒤 strip 하면서 다음 단어로 넘어감
        
    return answer

if __name__ == "__main__":
    result = solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])
    print(result)