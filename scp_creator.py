likSCP = []
sites = []


class Scp:
    def __init__(self, scpNumSubfix, series, site: str, status: str, cont: str,
                 num: int, dan: str, baseLookRank: str):
        self.scpNum = num              # SCP NUMBER
        self.scpDan = dan              # SCP Tehlike Seviyesi
        self.cont = cont               # Containment Seviyesi
        self.status = status           # Status
        self.site = site               # Bulunduğu site
        self.scpNumSubfix = scpNumSubfix  # SubFix varsa yaz
        self.series = series           # Bulunduğu seri
        self.baseLookRank = baseLookRank
        likSCP.append(self)

    def fullNum(self):
        return f"SCP-{self.scpNum}{self.scpNumSubfix or ''}"

    def __str__(self):
        return (f"{self.fullNum()} | Seri: {self.series} | Site: {self.site} | "
                f"Durum: {self.status} | Containment: {self.cont} | "
                f"Tehlike: {self.scpDan} | Min. Rütbe: {self.baseLookRank}")


def addsite(nameS, rank):
    site = {
        "name": nameS,
        "baseRank": rank,
    }
    sites.append(site)
    return site


def findSite(nameS):
    for s in sites:
        if s["name"].lower() == nameS.lower():
            return s
    return None


def askNonEmpty(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Bu alan boş olamaz, tekrar deneyin.")


def creation():
    print("WARNING! THIS APP IS SPECIAL AND ONLY FOR likSCP \n\n\n"
          "Welcome! This is your lik-SCP creator! \n"
          "we are gonna ask you some questions. Please answer them correctly\n"
          "If you are not sure ASK your Boss! ")

    print("Firstly What is your rank key : \n")
    rankKEY = askNonEmpty("> ")

    site_name = askNonEmpty("\nHangi site için SCP oluşturuyorsun? : ")
    site = findSite(site_name)

    if site is None:
        print(f"'{site_name}' adında bir site bulunamadı, yeni site oluşturuluyor...")
        base_rank = askNonEmpty("Bu site için gereken minimum rütbe nedir? : ")
        site = addsite(site_name, base_rank)

    if rankKEY != site["baseRank"]:
        print(f"YETKİSİZ ERİŞİM! Bu site '{site['baseRank']}' rütbesi gerektiriyor. "
              "İşlem iptal edildi.")
        return None

    print("\nRütbe doğrulandı. SCP bilgilerini girin.\n")

    num_raw = askNonEmpty("SCP Numarası (örn: 173) : ")
    while not num_raw.isdigit():
        print("Lütfen sadece sayı girin.")
        num_raw = askNonEmpty("SCP Numarası (örn: 173) : ")
    num = int(num_raw)

    scpNumSubfix = input("SubFix varsa yazın (yoksa boş bırakın, örn: -J) : ").strip()
    series = askNonEmpty("Seri (örn: Series I) : ")
    status = askNonEmpty("Status (örn: Contained / Neutralized / Explained) : ")
    cont = askNonEmpty("Containment Seviyesi (örn: Safe / Euclid / Keter) : ")
    dan = askNonEmpty("Tehlike Seviyesi (örn: Low / Medium / High / Critical) : ")
    baseLookRank = askNonEmpty("Bu SCP'yi görüntülemek için gereken minimum rütbe : ")

    newScp = Scp(
        scpNumSubfix=scpNumSubfix,
        series=series,
        site=site["name"],
        status=status,
        cont=cont,
        num=num,
        dan=dan,
        baseLookRank=baseLookRank,
    )

    print("\nSCP başarıyla oluşturuldu! \n")
    print(newScp)
    return newScp


if __name__ == "__main__":
    addsite("Site-19", "Level 3")
    addsite("Site-17", "Level 4")

    while True:
        creation()
        again = input("\nBaşka bir SCP oluşturmak ister misin? (e/h) : ").strip().lower()
        if again != "e":
            break

    print(f"\nToplam kayıtlı SCP: {len(likSCP)}")
    for scp in likSCP:
        print(scp)
