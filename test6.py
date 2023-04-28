import os

def readFromDictFile(file) :
  '''
    파일에서 데이터를 읽고 dict객체에 저장 후 반환
  '''
  dict = {}
  if os.path.exists(file) :  # 파일존재여부 체크

    #파일이 존재하면 단어장을 읽어와 딕셔너리에 저장
    f = open(file,'r',encoding='UTF8')
    if f.readable() :
      for line in f.readlines() :
        list = line.split(':')
        dict[list[0].strip()] = list[1].strip()
        
      f.close()
  return dict

def writeToDict(dic, file, mode) :
  '''1
    딕셔너리객체 내용을 파일에 쓰기
  '''
  # 키 오름차순 저장
  sortedDict = sorted(dic.items())
  f = open(file,mode,encoding='UTF8')
  if f.writable() :
    for item in sortedDict :
      f.write('{}:{}\n'.format(item[0].strip(),item[1].strip()))
    f.close()
    print('파일에 저장완료!')

def dupChkOfWord(dic, word) :
  '''
    딕셔너리객체에서 단어 중복 체크, 중복하면 True 반환
  '''
  if dic.get(word,-1) == -1 :
    return False
  else :
    return True  

def printList(dic) :
  '''
    딕셔너리객체 모든요소 출력하기
  '''
  for ele in dic.keys() :
    print('{:15} : {}'.format(ele,dictionary.get(ele)))

PATH = r'd:\javaedu9\project\python\dictionary.txt'
dictionary = readFromDictFile(PATH)

MAX_WORD = 5  # 저장할수 있는 최대 단어수
word, meaning = None, None  # 단어,뜻
stop = False
print('>> 단어장 << ')
while not stop :
  print('메뉴 >> 1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료(x) 8.사전파일삭제')
  menu = input('선택 >> ')

  if menu == '1' :      # 저장
    word = input('단어 입력 > ')

    if dupChkOfWord(dictionary,word) :
      print('이미 등록되었습니다.')
      continue 

    if len(dictionary) >= 5 :
      print('최대 5개 단어만 저장할 수 있습니다')
      continue

    meaning = input('뜻 입력 > ')
    dictionary[word] =  meaning
    print('저장완료!')

  elif menu == '2' :    # 검색
    word = input('단어 입력 > ')
    print(dictionary.get(word,'단어를 검색할 수 없습니다'))

  elif menu == '3' :    # 수정
    word = input('단어 입력 > ')

    if not dupChkOfWord(dictionary,word) :  
      print('단어를 검색할 수 없습니다.')
      continue

    meaning = input('뜻 입력 > ')
    dictionary[word] = meaning
    print('수정완료!')

  elif menu == '4' :  # 삭제
    word = input('단어 입력 > ')

    if not dupChkOfWord(dictionary,word) :  
      print('단어를 검색할 수 없습니다.')
      continue

    if input(r'삭제하시겠습니까?(y/n) ').upper() == 'Y' :  
      del dictionary[word]
      print('삭제완료!')  

  elif menu == '5' :  # 목록
    if dictionary :
      printList(dictionary)
    else :
      print('저장된 단어가 없습니다')  

  elif menu == '6' :  # 통계
    print('서브메뉴 >> 1.저장된 단어 갯수 2. 단어의 문자수가 가장 많은 단어 3.단어 글자수 내림차순 출력')
    subMenu = input('선택 >> ')

    if subMenu == '1' :
      print('저장된 단어 갯수 : {} 개'.format(len(dictionary)))

    elif subMenu == '2' :
      if dictionary :
        reversedList = sorted(dictionary.keys(),key=lambda x: len(x),reverse=True)
        maxLength = len(reversedList[0])
        print('단어의 문자수가 가장 많은 단어 : ')
        for item in reversedList :
          if len(item) == maxLength :
            print('{}'.format(item))
          else :
            break;  
      else :
        print('저장된 단어가 없습니다')          

    elif subMenu == '3' :      
      if dictionary :
        # 문자열 길이 역순
        reversedList = sorted(dictionary.keys(),key=lambda x: len(x),reverse=True)

        for item in reversedList :
          print('{:15} : {}'.format(item,dictionary.get(item)))        
      else :
        print('저장된 단어가 없습니다')    

  elif menu == '7' :  # 종료
    stop = True
    writeToDict(dictionary, PATH, 'w')
    print('프로그램 종료!')
    break

  elif menu == '8' :  # 사전파일 삭제 
    if os.path.exists(PATH) :
      if input(r'삭제하시겠습니까?(y/n)' ).upper() == 'Y' :  
        dictionary.clear()
        os.remove(PATH)
        print('사전파일 삭제완료!')
    else :
      print('파일이 존재하지 않습니다')    