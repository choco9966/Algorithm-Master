# #이 붙은 음표는 소문자로 변경 
def changecode(music_): 
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')    
    return music_ 

def caltime(musicinfo_): 
    starttime = musicinfo_[0]
    endtime = musicinfo_[1]
    hour = 1 * (int(endtime.split(':')[0]) - int(starttime.split(':')[0]))
    if hour == 0: 
        total = int(endtime.split(':')[1]) - int(starttime.split(':')[1])
    else: 
        total = 60 * hour + int(endtime.split(':')[1]) - int(starttime.split(':')[1])
    
    return total

def solution(m, musicinfos):
    answer = []
    m = changecode(m)
    for idx, musicinfo in enumerate(musicinfos): 
        musicinfo = changecode(musicinfo)
        musicinfo = musicinfo.split(',')
        time = caltime(musicinfo)
        
        # 길이가 시간보다 더 긴 경우 
        if len(musicinfo[3]) >= time :
            melody = musicinfo[3][0:time]
        else:             
            # 시간을 계산해서 몫과 나머지로 계산 
            # 다른 사람 풀이 : q, r = divmod(time,len(musicinfo[3]))
            a = time // len(musicinfo[3])
            b = time % len(musicinfo[3])
            melody = musicinfo[3] * a + musicinfo[3][0:b]
        # 노래가 melody에 포함되면 정답후보에 저장 
        if m in melody: 
            answer.append([idx, time, musicinfo[2]])
    # 정답이 있는 경우 
    if len(answer) != 0: 
        # time -> index 기준으로 정렬 
        answer = sorted(answer, key = lambda x: (-x[1], x[0]))
        return answer[0][2]
    # 정답이 없는 경우
    return "(None)"