#from maps.GakushokuSample import GakushokuSample
from maps.GakushokuToshi import GakushokuToshi
from maps.GakushokuWkatu import GakushokuWkatu
from maps.iwataOsusume import iwataOsusume
from maps.K25031Osusume import K25031Osusume
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [
    #GakushokuSample(),
    GakushokuToshi(),
    GakushokuWkatu(),
    iwataOsusume(),
    K25031Osusume(),
    ]
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()