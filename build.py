# -*- coding: utf-8 -*-
"""Toktaş Hukuk Bürosu — statik site üretici. `python3 build.py` çalıştırınca dist/ klasörünü doldurur."""
import os, shutil, datetime

SITE = "https://toktas.av.tr"
EMAIL = "sefa.toktas@toktas.av.tr"          # DOĞRULAYIN — mevcut sitede mstoktas@gmail.com yazıyordu
TEL1 = "0 224 451 42 62"
TEL2 = "0 224 451 42 63"
TEL1_HREF = "+902244514262"
ADDR1 = "Konak Mah., Çağlayan İş Merkezi, İzmir Yolu Cd. No:93 K:2 D:6"
ADDR2 = "16110 Nilüfer / Bursa"
MAPS = "https://www.google.com/maps/search/?api=1&query=" + "Çağlayan İş Merkezi İzmir Yolu Cd. No:93 Nilüfer Bursa".replace(" ", "+")
YEAR = datetime.date.today().year

NAV = [
    ("index.html", "Ana Sayfa"),
    ("hakkimizda.html", "Hakkımızda"),
    ("calisma-alanlari.html", "Çalışma Alanları"),
    ("ekibimiz.html", "Ekibimiz"),
    ("iletisim.html", "İletişim"),
]

AREAS = [
    ("ticaret-hukuku", "Ticaret ve Şirketler Hukuku",
     "Şirket kuruluşu, ortaklık ilişkileri, ticari sözleşmeler ve ticari alacaklar.",
     [
      "Şirket kuruluşu, ana sözleşme değişiklikleri, genel kurul ve ortaklar arası uyuşmazlıklar",
      "Bayilik, franchise, distribütörlük, tedarik ve hizmet sözleşmelerinin hazırlanması ve incelenmesi",
      "Ticari alacakların takibi; çek, senet ve fatura kaynaklı uyuşmazlıklar",
      "Haksız rekabet, ticari sır ve sözleşmeye aykırılık kaynaklı davalar",
      "Ticari uyuşmazlıklarda zorunlu arabuluculuk süreçlerinin yürütülmesi",
     ]),
    ("gayrimenkul-hukuku", "Gayrimenkul Hukuku",
     "Tapu, kira, kat mülkiyeti ve ortaklığın giderilmesine ilişkin iş ve davalar.",
     [
      "Tapu iptali ve tescil, el atmanın önlenmesi, ecrimisil ve sınır uyuşmazlıkları",
      "Konut ve çatılı işyeri kira sözleşmeleri; tahliye, kira tespiti ve kira uyarlama davaları",
      "Ortaklığın giderilmesi (izale-i şüyu) ve miras kaynaklı taşınmaz uyuşmazlıkları",
      "Kat mülkiyeti, arsa payı karşılığı inşaat ve gayrimenkul satış vaadi sözleşmeleri",
      "Kamulaştırma ve kamulaştırmasız el atma davaları",
     ]),
    ("is-hukuku", "İş ve Sosyal Güvenlik Hukuku",
     "İşçi ve işveren tarafında iş ilişkisinin kurulması, yürütülmesi ve sona ermesi.",
     [
      "İşe iade, kıdem ve ihbar tazminatı, fazla mesai ve diğer işçilik alacakları davaları",
      "İş sözleşmelerinin, işyeri yönetmeliklerinin ve rekabet yasağı hükümlerinin hazırlanması",
      "İş kazası ve meslek hastalığından kaynaklanan tazminat davaları",
      "Hizmet tespiti ve sosyal güvenlik uyuşmazlıkları",
      "İş uyuşmazlıklarında zorunlu arabuluculuk sürecinde temsil",
     ]),
    ("aile-hukuku", "Aile Hukuku",
     "Boşanma, velayet, nafaka ve mal rejimi konularında dava ve danışmanlık.",
     [
      "Anlaşmalı ve çekişmeli boşanma davaları",
      "Velayet, kişisel ilişki kurulması ve nafaka davaları",
      "Edinilmiş mallara katılma rejiminden doğan mal paylaşımı ve katkı payı davaları",
      "Aile konutu şerhi, evlilik sözleşmeleri ve nişan kaynaklı uyuşmazlıklar",
      "Yabancı unsurlu boşanma kararlarının tanınması ve tenfizi",
     ]),
    ("ceza-hukuku", "Ceza Hukuku",
     "Soruşturma ve kovuşturma aşamalarında müdafilik ve mağdur vekilliği.",
     [
      "Soruşturma aşamasında ifade ve sorgu işlemlerinde müdafilik",
      "Ağır ceza, asliye ceza ve sulh ceza hâkimliği nezdinde savunma",
      "Tutuklama, adli kontrol ve koruma tedbirlerine itiraz",
      "Suçtan zarar gören ve katılan sıfatıyla vekillik",
      "İstinaf ve temyiz kanun yolu başvuruları",
     ]),
    ("icra-iflas-hukuku", "İcra ve İflas Hukuku",
     "Alacakların tahsili ve borçlu tarafında hakların korunması.",
     [
      "İlamlı ve ilamsız icra takipleri; kambiyo senetlerine özgü takipler",
      "İtirazın iptali, itirazın kaldırılması, menfi tespit ve istirdat davaları",
      "Haciz, kıymet takdiri ve ihale işlemlerine karşı şikâyet ve itirazlar",
      "Konkordato ve iflas süreçlerinde alacaklı ve borçlu temsili",
      "Tasarrufun iptali davaları",
     ]),
]

TEAM = [
    ("dsc_3188_sb", "Av. Muhammet Sefa Toktaş", "Kurucu Avukat", "Bursa Barosu",
     "Büronun kurucusudur. Ticaret, gayrimenkul, iş ve aile hukuku ile ceza ve icra-iflas alanlarındaki dava ve danışmanlık işlerini yürütür."),
    ("dsc_3181_sb", "Av. Bilge Ece Toktaş", "Avukat", "Bursa Barosu",
     "Büronun dava ve danışmanlık işlerinde görev almaktadır."),
    ("dsc_3161_sb", "Av. Sefa Seçkin", "Avukat", "Bursa Barosu",
     "Büronun dava ve danışmanlık işlerinde görev almaktadır."),
]

def head(title, desc, path, extra=""):
    full = f"{title} | Toktaş Hukuk Bürosu" if path != "index.html" else "Toktaş Hukuk Bürosu | Bursa"
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{'' if path=='index.html' else path}">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="Toktaş Hukuk Bürosu">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{'' if path=='index.html' else path}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#6f1d2b">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Source+Sans+3:ital,wght@0,400;0,600;1,400&display=swap">
<link rel="stylesheet" href="style.css">
{extra}
</head>
<body>
"""

def header(path):
    cur = ' aria-current="page"'
    links = "".join(
        f'<a href="{h}"{cur if h==path else ""}>{t}</a>' for h, t in NAV)
    return f"""<a class="skip" href="#icerik">İçeriğe geç</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="index.html" aria-label="Toktaş Hukuk Bürosu ana sayfa">
      <span class="brand-name">TOKTAŞ</span><span class="brand-sep" aria-hidden="true">|</span><span class="brand-sub">HUKUK BÜROSU</span>
    </a>
    <nav class="nav" aria-label="Ana menü">{links}</nav>
  </div>
</header>
<main id="icerik">
"""

def footer():
    return f"""</main>
<footer class="site-footer">
  <div class="wrap foot-grid">
    <div>
      <p class="foot-brand">Toktaş Hukuk Bürosu</p>
      <p class="muted">Av. Muhammet Sefa Toktaş<br>Bursa Barosu</p>
    </div>
    <div>
      <p class="label">Adres</p>
      <p>{ADDR1}<br>{ADDR2}</p>
    </div>
    <div>
      <p class="label">İletişim</p>
      <p><a href="tel:{TEL1_HREF}">{TEL1}</a><br><a href="tel:+902244514263">{TEL2}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div>
      <p class="label">Bilgi</p>
      <p><a href="kvkk.html">KVKK Aydınlatma Metni</a><br><a href="https://www.bursabarosu.org.tr" rel="noopener" target="_blank">Bursa Barosu</a></p>
    </div>
  </div>
  <div class="wrap foot-note">
    <p>© {YEAR} Toktaş Hukuk Bürosu. Bu sitedeki bilgiler yalnızca genel bilgilendirme amacıyla sunulmuştur; hukuki tavsiye niteliği taşımaz ve avukat-müvekkil ilişkisi doğurmaz. Site, Türkiye Barolar Birliği Reklam Yasağı Yönetmeliği’ne uygun olarak hazırlanmıştır.</p>
  </div>
</footer>
</body>
</html>
"""

def page(path, title, desc, body, extra=""):
    return head(title, desc, path, extra) + header(path) + body + footer()

# ---------- Sayfa gövdeleri ----------

def areas_grid(short=True):
    items = []
    for slug, name, lead, _ in AREAS:
        items.append(f"""
      <a class="area" href="calisma-alanlari.html#{slug}">
        <h3>{name}</h3>
        <p>{lead}</p>
        <span class="more">Ayrıntı <span aria-hidden="true">→</span></span>
      </a>""")
    return "".join(items)

index_body = f"""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Bursa · Nilüfer</p>
    <h1>Ticari, gayrimenkul, iş ve aile hukuku uyuşmazlıklarında dava ve danışmanlık.</h1>
    <p class="lede">Toktaş Hukuk Bürosu, Bursa’da şirketlere ve bireylere hukuki süreçlerin her aşamasında vekillik ve danışmanlık hizmeti verir. Sözleşmelerin hazırlanmasından icra takiplerine, dava öncesi arabuluculuktan kanun yolu başvurularına kadar işi başından sonuna kadar aynı ekip yürütür.</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="tel:{TEL1_HREF}">{TEL1}</a>
      <a class="btn btn-ghost" href="iletisim.html">İletişim bilgileri</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Çalışma alanları</h2>
      <p class="muted">Büronun ağırlıklı olarak çalıştığı altı alan.</p>
    </div>
    <div class="area-grid">{areas_grid()}</div>
  </div>
</section>

<section class="section section-tint">
  <div class="wrap two-col">
    <div>
      <h2>Nasıl çalışıyoruz</h2>
      <p>Her dosya, ilk görüşmede yapılan bir değerlendirmeyle başlar. Bu görüşmede olayın hukuki niteliği, izlenebilecek yollar, süreler ve muhtemel maliyetler açıkça konuşulur. Dava açmanın en doğru yol olmadığı hâllerde bunu da aynı açıklıkla söyleriz.</p>
      <p>Süreç boyunca dosyanın hangi aşamada olduğunu, duruşma ve tebligat tarihlerini ve atılan her adımı müvekkile düzenli olarak bildiririz. Ücret, Türkiye Barolar Birliği Avukatlık Asgari Ücret Tarifesi esas alınarak işin başında yazılı olarak belirlenir.</p>
    </div>
    <dl class="facts">
      <div><dt>Görüşme</dt><dd>Randevu ile, büroda veya çevrim içi</dd></div>
      <div><dt>Yer</dt><dd>Nilüfer / Bursa; Bursa ve çevre illerde duruşma takibi</dd></div>
      <div><dt>Arabuluculuk</dt><dd>Ticari, iş ve kira uyuşmazlıklarında dava şartı arabuluculuk süreçlerinde temsil</dd></div>
      <div><dt>Ücret</dt><dd>İşin başında yazılı sözleşme ile belirlenir</dd></div>
    </dl>
  </div>
</section>

<section class="section">
  <div class="wrap contact-strip">
    <div>
      <h2>Randevu ve iletişim</h2>
      <p class="muted">Hafta içi 09.00–18.00 arasında telefonla; diğer saatlerde e-posta ile ulaşabilirsiniz.</p>
    </div>
    <div class="contact-cols">
      <p><span class="label">Telefon</span><a href="tel:{TEL1_HREF}">{TEL1}</a><a href="tel:+902244514263">{TEL2}</a></p>
      <p><span class="label">E-posta</span><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p><span class="label">Adres</span>{ADDR1}<br>{ADDR2}<br><a href="{MAPS}" target="_blank" rel="noopener">Haritada göster</a></p>
    </div>
  </div>
</section>
"""

hakkimizda_body = f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Hakkımızda</p>
    <h1>Bursa’da, dosyayı başından sonuna kadar aynı ekibin yürüttüğü bir hukuk bürosu.</h1>
  </div>
</section>
<section class="section">
  <div class="wrap prose">
    <p>Toktaş Hukuk Bürosu, Av. Muhammet Sefa Toktaş tarafından Bursa’da kurulmuştur. Büro, Nilüfer’deki ofisinden şirketlere ve bireylere ticaret, gayrimenkul, iş, aile, ceza ve icra-iflas hukuku alanlarında vekillik ve danışmanlık hizmeti vermektedir.</p>
    <p>Büronun çalışma anlayışı üç ilkeye dayanır. Birincisi, müvekkile durumun gerçekçi bir değerlendirmesini sunmak: bir yolun sonuç vermeyeceğini düşünüyorsak bunu işin başında söyleriz. İkincisi, dosyanın her aşamasında müvekkili bilgilendirmek: duruşma tarihleri, tebligatlar ve atılan adımlar müvekkile düzenli olarak aktarılır. Üçüncüsü, işi şahsen yürütmek: müvekkilin görüştüğü avukat, dosyayı takip eden avukattır.</p>
    <h2>Kimlere hizmet veriyoruz</h2>
    <p>Bursa ve çevresinde faaliyet gösteren üretici ve ticari işletmeler, gayrimenkul sahipleri ve kiracılar, işçiler ve işverenler ile aile hukuku ve ceza yargılamasında tarafı olan bireyler büronun başlıca müvekkil gruplarını oluşturur. Yurt dışında yerleşik olup Türkiye’de hukuki işi bulunan kişi ve şirketlere de danışmanlık verilmektedir.</p>
    <h2>Ücret ve vekâlet</h2>
    <p>Avukatlık ücreti, Türkiye Barolar Birliği Avukatlık Asgari Ücret Tarifesi ile Bursa Barosu tavsiye niteliğindeki ücret tarifesi esas alınarak, işin niteliğine göre işin başında yazılı avukatlık sözleşmesi ile belirlenir. Vekâletname, herhangi bir noterlikten büronun vekâlet bilgileriyle çıkarılabilir; bilgiler ilk görüşmede paylaşılır.</p>
    <p class="note">Bu sayfada yer alan bilgiler, 1136 sayılı Avukatlık Kanunu ve Türkiye Barolar Birliği Reklam Yasağı Yönetmeliği çerçevesinde yalnızca bilgilendirme amacıyla sunulmuştur.</p>
  </div>
</section>
"""

def areas_body():
    secs = []
    for slug, name, lead, bullets in AREAS:
        lis = "".join(f"<li>{b}</li>" for b in bullets)
        secs.append(f"""
  <section class="area-detail" id="{slug}">
    <div class="wrap two-col">
      <div>
        <h2>{name}</h2>
        <p class="lede-sm">{lead}</p>
      </div>
      <ul class="checklist">{lis}</ul>
    </div>
  </section>""")
    toc = "".join(f'<a href="#{slug}">{name}</a>' for slug, name, _, _ in AREAS)
    return f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Çalışma alanları</p>
    <h1>Büronun ağırlıklı olarak çalıştığı alanlar ve bu alanlarda yürütülen işler.</h1>
    <nav class="toc" aria-label="Alanlar">{toc}</nav>
  </div>
</section>
{''.join(secs)}
<section class="section">
  <div class="wrap prose">
    <p class="note">Listelenen işler örnek niteliğindedir; her dosya kendi koşulları içinde değerlendirilir. Bu alanlar dışındaki bir konuda ihtiyacınız varsa, işin büro tarafından üstlenilip üstlenilemeyeceği ilk görüşmede açıkça belirtilir.</p>
  </div>
</section>
"""

def team_body():
    cards = []
    for img, name, role, bar, bio in TEAM:
        cards.append(f"""
      <article class="person">
        <img src="images/{img}.jpg" alt="{name}" width="480" height="720" loading="lazy">
        <h2>{name}</h2>
        <p class="role">{role} · {bar}</p>
        <p>{bio}</p>
      </article>""")
    return f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Ekibimiz</p>
    <h1>Bursa Barosu’na kayıtlı üç avukat.</h1>
  </div>
</section>
<section class="section">
  <div class="wrap team-grid">{''.join(cards)}</div>
</section>
"""

iletisim_body = f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">İletişim</p>
    <h1>Randevu için arayabilir veya e-posta gönderebilirsiniz.</h1>
  </div>
</section>
<section class="section">
  <div class="wrap two-col">
    <div class="contact-block">
      <p class="label">Telefon</p>
      <p class="big"><a href="tel:{TEL1_HREF}">{TEL1}</a></p>
      <p class="big"><a href="tel:+902244514263">{TEL2}</a></p>
      <p class="label">E-posta</p>
      <p class="big"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p class="label">Çalışma saatleri</p>
      <p>Hafta içi 09.00–18.00<br>Görüşmeler randevu ile yapılır.</p>
    </div>
    <div class="contact-block">
      <p class="label">Adres</p>
      <p class="big">Çağlayan İş Merkezi</p>
      <p>{ADDR1}<br>{ADDR2}</p>
      <p><a class="btn btn-ghost" href="{MAPS}" target="_blank" rel="noopener">Haritada göster</a></p>
      <p class="label">Ulaşım</p>
      <p>İzmir Yolu üzerinde, Nilüfer merkezde. Bina önünde ve çevresinde araç park alanı bulunmaktadır.</p>
    </div>
  </div>
</section>
<section class="section section-tint">
  <div class="wrap prose">
    <h2>İlk görüşmeye gelirken</h2>
    <p>Konuyla ilgili elinizdeki sözleşme, tebligat, dava dilekçesi, icra ödeme emri, tapu kaydı, bordro veya yazışma gibi belgeleri yanınızda getirmeniz değerlendirmeyi hızlandırır. Tebligat aldıysanız tebliğ tarihini not etmeniz önemlidir; birçok işlemde süreler bu tarihten itibaren işler.</p>
    <p class="note">E-posta veya telefonla ilettiğiniz kişisel verileriniz yalnızca talebinizin değerlendirilmesi amacıyla işlenir. Ayrıntılar için <a href="kvkk.html">KVKK Aydınlatma Metni</a>’ne bakabilirsiniz.</p>
  </div>
</section>
"""

kvkk_body = f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">6698 sayılı Kanun</p>
    <h1>Kişisel Verilerin Korunması Hakkında Aydınlatma Metni</h1>
  </div>
</section>
<section class="section">
  <div class="wrap prose legal">
    <p>Bu aydınlatma metni, 6698 sayılı Kişisel Verilerin Korunması Kanunu’nun (“Kanun”) 10. maddesi ile Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ uyarınca, veri sorumlusu sıfatıyla <strong>Av. Muhammet Sefa Toktaş – Toktaş Hukuk Bürosu</strong> ({ADDR1}, {ADDR2}) tarafından hazırlanmıştır.</p>

    <h2>1. İşlenen kişisel veriler ve toplanma yöntemi</h2>
    <p>Büromuzla telefon, e-posta veya yüz yüze iletişime geçtiğinizde paylaştığınız ad-soyad, telefon numarası, e-posta adresi ve talebinizin içeriğinde yer alan bilgiler; vekâlet ilişkisi kurulması hâlinde ise kimlik, iletişim, adres ve dosya konusuyla sınırlı diğer veriler işlenmektedir. Veriler, sizin tarafınızdan sözlü, yazılı veya elektronik ortamda iletilmesi suretiyle toplanır.</p>
    <p>Bu internet sitesi çerez kullanmamakta ve ziyaretçi davranışlarını izleyen herhangi bir analitik araç içermemektedir. Sitenin barındırıldığı sunucu, güvenlik amacıyla erişim kayıtlarında IP adresi ve erişim zamanı gibi teknik bilgileri 5651 sayılı Kanun kapsamındaki süre boyunca tutabilir.</p>

    <h2>2. İşleme amaçları ve hukuki sebepler</h2>
    <p>Kişisel verileriniz; talebinizin değerlendirilmesi ve sizinle iletişim kurulması, avukatlık hizmetinin sunulması ve vekâlet ilişkisinin yürütülmesi, 1136 sayılı Avukatlık Kanunu ile Türkiye Barolar Birliği düzenlemelerinden doğan yükümlülüklerin yerine getirilmesi, ücret ve muhasebe kayıtlarının tutulması ve hukuki uyuşmazlıklarda hakların korunması amaçlarıyla; Kanun’un 5. maddesinin 2. fıkrasında düzenlenen “kanunlarda açıkça öngörülmesi”, “bir sözleşmenin kurulması veya ifasıyla doğrudan doğruya ilgili olması”, “veri sorumlusunun hukuki yükümlülüğünü yerine getirebilmesi için zorunlu olması”, “bir hakkın tesisi, kullanılması veya korunması için zorunlu olması” ve “veri sorumlusunun meşru menfaati” hukuki sebeplerine dayanılarak işlenmektedir. Özel nitelikli kişisel verileriniz, yalnızca Kanun’un 6. maddesindeki şartlar dâhilinde ve dosyanın gerektirdiği ölçüde işlenir.</p>

    <h2>3. Aktarım</h2>
    <p>Kişisel verileriniz; yalnızca dosyanın yürütülmesi için gerekli olduğu ölçüde mahkemeler, icra daireleri, savcılıklar, noterler, arabuluculuk büroları ve diğer resmî kurumlar ile, yasal yükümlülükler çerçevesinde talep hâlinde yetkili kamu kurum ve kuruluşlarına aktarılabilir. Bunun dışında üçüncü kişilerle paylaşılmaz. Avukatlık Kanunu’nun 36. maddesi uyarınca sır saklama yükümlülüğü, vekâlet ilişkisi sona erdikten sonra da devam eder.</p>

    <h2>4. Saklama süresi</h2>
    <p>Veriler, işleme amacının gerektirdiği süre boyunca ve her hâlde ilgili mevzuatta öngörülen zamanaşımı ve saklama süreleri (Avukatlık Kanunu m.39 uyarınca dosyaların iş sona erdikten itibaren üç yıl saklanması dâhil) sonuna kadar muhafaza edilir; sürenin dolmasıyla silinir, yok edilir veya anonim hâle getirilir.</p>

    <h2>5. Haklarınız</h2>
    <p>Kanun’un 11. maddesi uyarınca; kişisel verilerinizin işlenip işlenmediğini öğrenme, işlenmişse buna ilişkin bilgi talep etme, işlenme amacını ve amacına uygun kullanılıp kullanılmadığını öğrenme, yurt içinde veya yurt dışında aktarıldığı üçüncü kişileri bilme, eksik veya yanlış işlenmişse düzeltilmesini isteme, Kanun’un 7. maddesindeki şartlar çerçevesinde silinmesini veya yok edilmesini isteme, bu işlemlerin aktarıldığı üçüncü kişilere bildirilmesini isteme, münhasıran otomatik sistemlerle analiz edilmesi suretiyle aleyhinize bir sonucun ortaya çıkmasına itiraz etme ve kanuna aykırı işleme sebebiyle zarara uğramanız hâlinde zararın giderilmesini talep etme haklarına sahipsiniz.</p>

    <h2>6. Başvuru</h2>
    <p>Haklarınıza ilişkin taleplerinizi, Veri Sorumlusuna Başvuru Usul ve Esasları Hakkında Tebliğ’e uygun olarak, kimliğinizi tespit edici bilgi ve belgelerle birlikte yukarıdaki adrese yazılı olarak ya da <a href="mailto:{EMAIL}">{EMAIL}</a> adresine e-posta ile iletebilirsiniz. Başvurular, niteliğine göre en kısa sürede ve en geç otuz gün içinde sonuçlandırılır.</p>

    <p class="note">Son güncelleme: {datetime.date.today().strftime('%d.%m.%Y')}</p>
  </div>
</section>
"""

PAGES = {
    "index.html": ("Ana Sayfa", "Toktaş Hukuk Bürosu, Bursa Nilüfer’de ticaret, gayrimenkul, iş, aile, ceza ve icra-iflas hukuku alanlarında dava ve danışmanlık hizmeti verir.", index_body),
    "hakkimizda.html": ("Hakkımızda", "Toktaş Hukuk Bürosu’nun çalışma anlayışı, hizmet verdiği müvekkil grupları ve ücret esasları.", hakkimizda_body),
    "calisma-alanlari.html": ("Çalışma Alanları", "Ticaret ve şirketler, gayrimenkul, iş ve sosyal güvenlik, aile, ceza ile icra ve iflas hukuku alanlarında yürütülen işler.", areas_body()),
    "ekibimiz.html": ("Ekibimiz", "Toktaş Hukuk Bürosu’nda görev yapan, Bursa Barosu’na kayıtlı avukatlar.", team_body()),
    "iletisim.html": ("İletişim", "Toktaş Hukuk Bürosu telefon, e-posta ve adres bilgileri. Çağlayan İş Merkezi, İzmir Yolu Cd. No:93, Nilüfer / Bursa.", iletisim_body),
    "kvkk.html": ("KVKK Aydınlatma Metni", "Toktaş Hukuk Bürosu 6698 sayılı Kişisel Verilerin Korunması Kanunu aydınlatma metni.", kvkk_body),
}

def main():
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(os.path.join(out, "images"))
    src = os.path.dirname(os.path.abspath(__file__))
    for p, (t, d, b) in PAGES.items():
        with open(os.path.join(out, p), "w", encoding="utf-8") as f:
            f.write(page(p, t, d, b))
    # 404
    with open(os.path.join(out, "404.html"), "w", encoding="utf-8") as f:
        f.write(page("404.html", "Sayfa bulunamadı", "Aradığınız sayfa bulunamadı.",
                     '<section class="page-head"><div class="wrap"><p class="eyebrow">404</p><h1>Aradığınız sayfa bulunamadı.</h1><p class="lede"><a href="index.html">Ana sayfaya dönün</a> veya menüden devam edin.</p></div></section>'))
    for fn in ("style.css", "favicon.svg", ".htaccess", "robots.txt"):
        shutil.copy(os.path.join(src, fn), os.path.join(out, fn))
    for fn in os.listdir(os.path.join(src, "images")):
        if fn.endswith((".jpg", ".png", ".webp")):
            shutil.copy(os.path.join(src, "images", fn), os.path.join(out, "images", fn))
    today = datetime.date.today().isoformat()
    urls = "".join(f"  <url><loc>{SITE}/{'' if p=='index.html' else p}</loc><lastmod>{today}</lastmod></url>\n" for p in PAGES)
    with open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    print("dist/ hazır:", sorted(os.listdir(out)))

if __name__ == "__main__":
    main()
