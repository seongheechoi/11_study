def Equipment(name, number, date):
    return name, number, date

def print_info(equip):
    print("{:10} {:9} {:10}".format(equip[0], equip[1], equip[2]))

def set_equip():
    name = input("장비명: ")
    number = input("수량: ")
    date = input("생산일(예:1990-01-01): ")
    equip = Equipment(name, number, date)
    return equip

def print_menu():
    print("1. 입력")
    print("2. 출력")
    print("3. 검색")
    print("4. 종료")
    menu = input("메뉴를 선택하시오: ")
    return int(menu)

def print_equip(equip_list):
    for equip in equip_list:
        print_info(equip)

def search_equip(equip_list, name):
    a=[]
    for i in range(len(equip_list)):
        if name == equip_list[i][0]:
            print_info(equip_list[i])
            a.append(equip_list)
    if not a:
        print('검색한 장비가 없습니다.')

def store_equip(equip_list):
    f = open("equip_db.txt", "wt")
    for equip in equip_list:
        f.write(equip[0] + '\n')
        f.write(equip[1] + '\n')
        f.write(equip[2] + '\n')
    f.close()

def load_equip(equip_list):
    f = open("equip_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 3
    num = int(num)

    for i in range(num):
        name = lines[3*i].rstrip('\n')
        number = lines[3*i+1].rstrip('\n')
        date = lines[3*i+2].rstrip('\n')
        equip = Equipment(name, number, date)
        equip_list.append(equip)
    f.close()

def run():
    equip_list = []
    load_equip(equip_list)
    while True:
        menu = print_menu()
        if menu == 1:
            while True:
                equip = set_equip()
                equip_list.append(equip)
                ans = input('계속 입력하시겠습니까(y/n)?')
                if ans == 'y':
                    continue
                elif ans == 'n':
                    break

        elif menu == 2:
            print("--------------------------------")
            print("장비명      수량      생산일")
            print("--------------------------------")
            print_equip(equip_list)

        elif menu == 3:
            name1 = input("검색할 장비명을 입력하세요: ")
            print("--------------------------------")
            print("장비명      수량      생산일")
            print("--------------------------------")
            search_equip(equip_list, name1)

        elif menu == 4:
            ans = input('프로그램을 종료하시겠습니까(y/n)?')
            if ans == 'y':
                store_equip(equip_list)
                break
            elif ans == 'n':
                continue

#if __name__ == "__main__":
run()
