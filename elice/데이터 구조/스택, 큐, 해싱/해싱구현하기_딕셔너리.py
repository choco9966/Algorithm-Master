class myDatabase:
    '''
    해싱을 구현합니다
    '''

    def __init__(self, size) :
        '''
        dictionary를 이용합니다.

        이곳은 수정하지 마세요.
        '''
        self.myData = {}

    def put(self, key, value) :
        '''
        key에 해당하는 값 value 즉, (key, value)를 저장합니다.
        '''
        self.myData[key] = value 

    def get(self, key) :
        '''
        key에 해당하는 value를 반환합니다. 만약 key에 해당하는 value가 없다면 -1을 반환합니다.
        '''
        try:
            return self.myData[key] 
        except:
            return -1

def main():
    db = myDatabase(100)

    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    db.put(1, 3)
    db.put(2, 7)
    db.put(3, 8)
    db.put(403, 9)

    print(db.get(3))
    print(db.get(403))


if __name__ == "__main__":
    main()
