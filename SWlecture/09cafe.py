# 카페 매출 계산 프로그램

# 메뉴가격 - 재료가격으로 마진 계산
# * input 받은 판매수량

sales = []
menu_price = {
  'latte': 3500,
  'boba tea': 4200
}
material_price = {
  'latte': 1700,
  'boba tea': 3000
}


# 함수

def count_sales(item, count=0):
  # 아이템이 메뉴판에 있는지 확인
  if item in menu_price:
    sales.append((item, count))
    print("%s %d잔을 판매했습니다"%(item, count))
  else:
    print("존재하지 않는 메뉴입니다")


def add_total(flag=True):
  total = 0
  for item, count in sales:
    # flag 값으로 매출, 재료비 계산
    if flag:
      total += menu_price[item] * count
    # flag = False 이면 재료비를 더함
    else:
      total += material_price[item] * count
    return total
  
def display_sales():
  if not sales:
    print("매출이 없습니다")
  else:
    print("--------")
    print("<오늘의 매출>")
    for item, count in sales:
      print("%s %d잔을 판매했습니다"%(item, count))
    print("================")
    tot_sales = add_total()
    tot_materials = add_total(False)  # flag=Flase 사용해서 재료비 더하기
    print("총 매출액은 ", tot_sales, " 원")
    print("영업이익은 ", tot_sales - tot_materials, "원 입니다")


# 메인 프로그램

# 입력을 계속할 것인지 계산
end = True
print("오늘의 매출 계산하기")

while end:
  sales_menu = input("판매된 메뉴를 입력하세요")
  sales_count = int(input("몇 잔을 판매했나요?"))
  
  # 입력받은 정보를 count_sales(item, count) 에 저장
  count_sales(sales_menu, sales_count)

  if input("입력을 종료할까요?(y/n)") == 'y':
    end = False

display_sales()

