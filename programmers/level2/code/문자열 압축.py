def solution(s):
    result = [len(s)]
    for step in range(1, 1 + len(s)//2):
        start = 0
        cnt = 1
        ans = ''
        while start + step < len(s):
            if s[start:start+step] == s[start+step:start+2*step]:
                cnt += 1
            else:
                if cnt == 1:
                    temp = ''.join(['', s[start:start+step]])
                else:
                    temp = ''.join([str(cnt), s[start:start+step]])
                ans = ''.join([ans, temp])
                cnt = 1
            start += step

        if cnt == 1:
            temp = ''.join(['', s[start:start+step]])
        else:
            temp = ''.join([str(cnt), s[start:start+step]])
        ans = ''.join([ans, temp])
        ans = ''.join([ans, s[start+step:]])
        # ans = ans.replace('1', '')
        result.append(len(ans))
    return min(result)
