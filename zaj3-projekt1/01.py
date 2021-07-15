print("Trafiłeś na rozgałęzienie. Chcesz iść w lewo czy w prawo? (w lewo/w prawo)")
decyzja1 = input()
if decyzja1 == "w lewo":
    print("Znajdujesz skrzynię. Co chcesz z nią zrobić? (otworzyc/zabrac/zostawic)")
    decyzja2 = input()
    if decyzja2 == "otworzyc":
        print("Nie masz klucza!")
    elif decyzja2 == "zabrac":
        print("Zabierasz skrzynkę i idziesz dalej! W którą stronę teraz, w lewo czy w prawo? (w lewo/w prawo)")
        decyzja3 = input()
        if decyzja3 == "w lewo":
            print("Przed sobą widzisz ogromnego smoka. Co robisz? (walcze/uciekam/udaje martwego)")
            decyzja4 = input()
            if decyzja4 == "walcze":
                print("Pokonujesz smoka i znajdujesz klucz do skrzynki! Otwierasz ją? (tak/nie)")
                decyzja5 = input()
                if decyzja5 == "tak":
                    print("Zdobywasz skarb!")
                elif decyzja5 == "nie":
                    print("Masz fajną skrzynkę!")
            elif decyzja4 == "uciekam":
                print("Niestety smok Cię dogonił!")
            elif decyzja4 == "udaje martwego":
                print("Smok nie dał się nabrać!")
        elif decyzja3 == "w prawo":
            print("Niestety nic tu nie ma!")
    elif decyzja2 == "zostawic":
        print("Zostawiasz fajną skrzynkę!")
elif decyzja1 == "w prawo":
    print("Ślepy zaułek!")
