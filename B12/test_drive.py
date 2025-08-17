# import class mp3
from mp3player import MP3Player
import time

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"


def test_drive():
    # khai bao
    mp3 = MP3Player()
    # input 1 danh sach nhac
    print(BLUE + "----------- Trình phát nhạc -----------" + RESET)
    song_list_len = 0
    while song_list_len == 0:
        try:
            song_list_len = int(input("Số lượng bài hát: "))
        except Exception as e:
            print(RED + "Lỗi: " + str(e) + RESET)
            song_list_len = 0

    for i in range(song_list_len):
        song = ""
        # nhap ten bai hat -> khong duoc rong
        while len(song) == 0:
            song = input("Nhập tên bài hát {}: ".format(i + 1)).strip()
        # them bai hat moi
        mp3.add_song(song)

    # hien thi danh sach bai hat
    print(BLUE + "----------- Danh sách bài hát -----------" + RESET)
    for index, value in enumerate(mp3.music_queue):
        print("{}. {}".format(index + 1, value))

    # chon hanh dong
    choices = """ LỰA CHỌN:
        1. Phát nhạc
        2. Bỏ qua bài hát hiện tại
        3. exit
    """
    choose = 0
    while choose != 3 or mp3.music_queue != []:
        print(BLUE + choices + RESET)
        try:
            choose = int(input())
        except Exception as e:
            print(RED + "Lỗi: " + str(e) + RESET)
            choose = 0

        # kiem tra tung hanh dong
        match choose:
            case 1:
                # phat nhac
                mp3.play_song()
            case 2:
                # bo qua bai hat
                mp3.skip_song()
            case 3:
                # exit
                print(
                    BLUE
                    + "----------- Cảm ơn bạn đã sử dụng chương trình! -----------"
                    + RESET
                )
                break
            
            case _:
                print(RED + "Lỗi: Lựa chọn không hợp lệ!" + RESET)

test_drive()
