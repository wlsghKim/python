def printList(dic, search_str=''):
    found = False
    for word, meaning in dic.items():
        if search_str in word:
            print(word, meaning)
            found = True
    if not found:
        print('단어를 검색할 수 없습니다.')
def printStats(dic):
    # 1. 저장된 단어의 갯수
    num_words = len(dic)
    print(f"저장된 단어의 갯수: {num_words}")

    # 2. 단어의 문자수가 가장 많은 단어
    max_word = max(dic.keys(), key=len)
    max_word_len = len(max_word)
    print(f"단어의 문자수가 가장 많은 단어: '{max_word}'")

    # 3. 단어 글자수 내림차순 출력
    sorted_words = sorted(dic.keys(), key=len, reverse=True)
    print("단어 글자수 내림차순:")
    for word in sorted_words:
        print(f"{word}")

## 파일->딕셔너리
# 파일에서 읽어오기
file = 'd:\javaedu10\project\python\dictionary.txt'
f = open(file, 'r', encoding='UTF8')
dic = {}
if f.readable() :
    for item in f.readlines() :
        list = item.split(':')
        dic[list[0].strip().lower()]=list[1][:-1] #문자열 슬라이싱
    f.close()

print('>> 영어 단어장 <<')
stop = False
count = 0
while not stop :
    print('메뉴 >> 1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료')
    choice = input('선택 >> ')

    if choice == '1':  # save
        if len(dic) >= 5:
            print('최대 5개 단어만 저장할 수 있습니다')
            continue
        word = input('단어 입력 > ')
        meaning = input('뜻 입력 > ')
        if word.lower() in dic:
          print('이미 등록되었습니다.')
        else:
          dic[word.lower()] = meaning
        count += 1

    elif choice == '2' : #검색
        term = input('단어 입력 > ').lower()
        printList(dic, term.lower())

    elif choice == '3':  # 수정
        word = input('단어 입력 > ').lower()
        if word.lower() in dic:
            print('뜻 : ', dic[word.lower()])
            new_meaning = input('새로운 뜻 입력 > ')
            dic[word.lower()] = new_meaning
            print('단어의 뜻을 수정 하였습니다.')
        else:
            print('단어를 검색할 수 없습니다.')

    elif choice == '4':  # 삭제
        word = input('삭제할 단어 입력 > ').lower()
        if word.lower() in dic:
            del dic[word.lower()]
            print('단어를 삭제 하였습니다.')
        else:
            print('단어를 검색할 수 없습니다.')
            
    elif choice == '5': # 목록
        print("선택:")
        print("1. 오름차순")
        print("2. 내림차순")
        sort_type = input('> ')
        sort_dict = {'1': False, '2': True}
        reverse_sort = sort_dict.get(sort_type)
        
        sorted_items = sorted(dic.items(), key=lambda x: x[0], reverse=reverse_sort)
        
        for item in sorted_items:
            print('{} : {}'.format(item[0], item[1]))
    elif choice == '6':  # 통계
      printStats(dic)

    elif choice == '7' : #종료
        stop = True
        ## 딕셔너리->파일
        if f.writable() :
          for item in dic :
            f.write('{}:{}\n'.format(item[0].strip(), item[1].strip()))
        f.close()
    else :
        print('선택한 메뉴가 없음')
        
        