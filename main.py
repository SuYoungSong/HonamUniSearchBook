from SerchBook import SearchLibraryBookPossession
from BorrowBookInfo import SerchBorrowInfo

# 도서관에서 책을 소장하고 있는지 검색
print("책 제목을 입력하세요: ",end='')
userInput = input()
i = 1
j = 1
bookSearchInfo = SearchLibraryBookPossession(userInput) # [0] 책 제목 ㅣ [1] 작가 ㅣ [2] 출판사 ㅣ [3] 책출판년도 ㅣ [4] 책관리번호

# 검색결과가 없을때
if bookSearchInfo== []:
  print("입력하신 책의 정보가 없습니다.")

# 검색결과 출력
else:
  print("\n■도서관 소장자료 검색 결과 입니다.\n")
  for serachResult in bookSearchInfo:
    print("["+str(i)+"]책 제목 : "+ serachResult[0] + "(" + str(serachResult[3]) + ")")
    print("["+str(i)+"]작가/출판사 : " + serachResult[1] + "/" + serachResult[2] )
    print("")
    i = i+1

  # 책 대출가능여부 및 상세정보 확인
  print("■도서 번호를 선택하세요: ",end='')
  bookNum = int(input())

  cno = bookSearchInfo[bookNum-1][4]
  borrowInfoData = SerchBorrowInfo(cno) # [0] 대출가능여부 ㅣ [1] 책위치(몇층인지) ㅣ [2] 책위치(번호) ㅣ [3] 대출자학번(가림) ㅣ [4] 대출자이름(가림) ㅣ [5] 도서 반납 예정일 ㅣ [6] 대출자학번 ㅣ [7] 대출자이름
  for borrow in borrowInfoData:
    # 책 상태가 대출가능일때 출력문
    if borrow[0] =="대출가능":
      print("["+str(j)+"]["+borrow[0]+"] 책위치: "+borrow[1]+"("+borrow[2]+")")
    # 책이 대출중일때
    else:
      print("["+str(j)+"]["+borrow[0]+"] 대출자: "+borrow[6]+"("+borrow[7]+") 반납 예정일: "+borrow[5] )
    j = j+1