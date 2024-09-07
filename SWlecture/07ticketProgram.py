# 티켓 예약 프로그램


# 아이디, 비번이 DB와 일치하면 로그인
db_id = "fe"
db_pass = "123"
flag = ""

userId = input("아이디: ")
password = input("비밀번호: ")

while userId != db_id or password != db_pass:
  if userId == db_id:
    print("비밀번호가 일치하지 않습니다")
  elif password == db_pass:
    print("아이디가 일치하지 않습니다")
  else:
    print("로그인 정보가 일치하지 않습니다")

  retry = input("다시 시도하시겠습니까? (y/n): ")
  if retry == "y":
    userId = input("아이디: ")
    password = input("비밀번호: ")
  else:
    print("로그인 종료")
    break

else:
  flag = "y"
  print("로그인에 성공했습니다")



# DB 저장된 영화, 잔여 좌석
db_movieInfo = {
  'In Bruige': 40,
  'Ailian' : 50
}
db_movieCurrent = {
  'In Bruige': 35,
  'Ailian' : 29
}
movieList = list(db_movieCurrent.keys())



# 티켓 예매하기
#  input 영화제목이 딕셔너리 키에 있는지 체크
while flag == "y":
  print("예약 가능한 영화는 ", movieList, "입니다")
  movie_name = input("어떤 영화를 예약할까요? ")

  if movie_name in db_movieInfo:
    seat = int(input("티켓 수량: "))
    remain_seat = int(db_movieInfo[movie_name] - db_movieCurrent[movie_name])
    
    if (remain_seat - seat < 0):
      print("잔여 좌석이 부족합니다")
      flag = input("예약을 계속하시겠습니까?(y/n) ")
    else:
      print("예약 가능한 좌석은 %d개 입니다"%remain_seat)
      print("좌석 선택 페이지로 이동합니다")
      break

  else:
    print("정확하지 않은 이름입니다")
    flag = input("예약을 계속하시겠습니까?(y/n) ")

else:
  print("예약을 종료합니다")
