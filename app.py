"""
Kejutan monthsary - jalankan dengan:  python -m streamlit run app.py
Versi: Burgundy Romance (luxury editorial). Isi: layar pembuka, hitung waktu, surat dalam amplop, pertanyaan terakhir.
"""
import html
import json
import random
from datetime import date

import streamlit as st
import streamlit.components.v1 as components

# =====================================================
# 1) EDIT BAGIAN INI DULU (semua teks bisa kamu ganti)
# =====================================================
NAMA_DIA = "Sayang"                  # panggilan untuk dia
NAMA_KAMU = "Fia"                    # nama kamu, jadi tanda tangan di pertanyaan terakhir
TANGGAL_JADIAN = date(2025, 10, 11)  # tahun, bulan, tanggal jadian kalian
TANGGAL_SURAT = "11 November 2026"   # tanggal yang tampil di kepala surat

# ---- ISI SURAT ----
SALAM = "Dear, Ravi Romario Nugroho"
JUDUL = "Selamat Tanggal 11!"

# Pisahkan paragraf dengan SATU BARIS KOSONG.
ISI = """Another month of us, another month of choosing each other, and another chapter of loving you.

Aku masih nda nyangka kita sudah sampai sejauh ini lho, sayang

Rasanya masih jelas banget di ingatan aku, setahun yang lalu waktu di hokben AXC ada seorang cowok yang tiba-tiba nyamperin lalu duduk di hadapan aku, ngajak ngobrol aku, terus dia juga follow ig aku. Dari situ, dia mulai sering chat dan ngabarin aku, suka curi-curi waktu buat ngajak aku ngobrol di sela-sela kerjaan 🤭, bahkan nyempetin teleponan dan minta buat sleepcall menjelang tidurrr hoho

And yap... somehow, the guy I never imagined I would even start a conversation with has become one of the people I love most in this world 😝✌️ 

Sayaaangg, aku mau kamu tahu kalau aku bersyukur banget bisa jadi pasangan kamu. Di tengah banyaknya hal yang harus kamu pikirkan, tanggung jawab yang perlu kamu selesaikan, dan hari-hari yang mungkin terasa melelahkan, kamu tetap berusaha melibatkan aku dalam keseharian kamu. Kamu juga konsisten nyempetin waktu buat ngabarin aku dan berbagi cerita tentang apa yang sedang kamu jalani. Aku seneng banget sayang. 

Aku juga liat bagaimana kamu terus berusaha, bagaimana kamu selalu punya keinginan untuk berkembang, dan bagaimana kamu sedang membangun sesuatu yang lebih baik untuk masa depanmu. I'm genuinely proud of you, babe.

Terima kasih ya, karena selama ini sudah berusaha menunjukkan seberapa besar kamu sayang sama aku. Terima kasih juga karena selalu sabar menghadapi aku, dengerin semua yapping an aku, perhatiin tiap hal-hal kecil tentang aku, dan berusaha memahami gimana aku ingin dicintai. Aku juga berterima kasih karena kamu nggak berhenti berusaha ketika ada hal-hal yang perlu kita perbaiki dalam hubungan ini. I appreciate every little effort you make, even the ones you might think I don't notice.

Aku sadar belum sepandai kamu dalam menunjukkan rasa sayang, belum sejago kamu dalam hal merespon, merangkai kata, atau menyemangati kamu ketika kamu lagi butuh dukungan verbal. Sometimes I struggle to find the right words, sometimes I overthink, and sometimes I just want to be babied a little more hehhehe. But I want you to know that I'm also learning. Aku mau terus belajar menjadi seseorang yang bisa kamu datangi ketika hari-harimu terasa berat, seseorang yang bisa kamu ajak berbagi cerita tanpa harus takut dihakimi, seseorang yang mau mendengarkan ketika kamu hanya ingin didengar, dan seseorang yang ikut merayakan setiap pencapaianmu, sekecil apa pun itu. I want to be your safe place, just as much as you are mine.

Aku harap kita bisa terus belajar menjadi pasangan yang lebih baik. Bukan pasangan yang nggak pernah punya masalah, tetapi dua orang yang tetap mau saling memahami dan memperbaiki keadaan ketika semuanya nggak berjalan sesuai keinginan. I want us to keep choosing each other, not only on our happiest days, but also on the days when loving each other requires a little more patience. 

Semoga kita nggak pernah kehilangan keinginan untuk saling mengenal, bahkan ketika kita sudah melewati banyak hal bersama yaa sayang ♡

And about that future you've been working so hard for, I hope you know how happy it makes me to be included in it. Aku nggak sabar melihat semua hal yang sedang kamu usahakan satu per satu menjadi kenyataan. I hope one day we get to look back at these days, remembering how we started with what we had, how we struggled, how we grew, and how we made it through together. Semoga nanti kita bisa tersenyum mengingat masa-masa ketika kita masih sama-sama berjuang untuk sampai ke kehidupan yang selama ini kita impikan.

For now, let's enjoy every little thing we have. More random conversations, more silly jokes, more dates, more hugs and kisses, more birthdays to celebrate, and hopefully countless more anniversaries. 

Aku mau menikmati setiap prosesnya sama kamu, days by days."""

ISI = [p.strip() for p in ISI.strip().split("\n\n") if p.strip()]

CINTA = "I love you, Rio. I love the person you are, the person you're becoming, and all the little things that make you uniquely you."
PENUTUP = "Happy 1 year and 1 month, sayangku"
TERIMA = "Thank you for being my favorite person to love. And if I could choose all over again, I'd still want to find my way back to you."
TTD_PRE = "Yours-"
TTD = "your girl. ♡"

# =====================================================
# 2) DESAIN: palet, font, dan CSS global
# =====================================================
# Palet: Deep Burgundy #4A101D | Dark Maroon #2B0B13 | Wine Red #651C2B | Muted Burgundy #813B49
#        Champagne Gold #C6A66B | Antique Gold #A98A55 | Warm Ivory #F5EFE6 | Soft Cream #E9DFD2
# Font:  Cormorant Garamond (display + isi surat), DM Sans (teks UI), Great Vibes (hanya tanda tangan)
FONT = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500'
        '&family=DM+Sans:wght@400;500&family=Great+Vibes&display=swap" rel="stylesheet">')
ROOT = (":root{--bu:#4A101D;--mr:#2B0B13;--wn:#651C2B;--mb:#813B49;--g:#C6A66B;--ag:#A98A55;--iv:#F5EFE6;--cr:#E9DFD2;"
        "--ch:#282124;--mu:rgba(233,223,210,.74);--hl:rgba(198,166,107,.3);--serif:'Cormorant Garamond',Georgia,serif;"
        "--sans:'DM Sans',system-ui,sans-serif}"
        "@keyframes up{from{opacity:0;transform:translateY(14px)}}"
        "@keyframes grow{from{transform:scaleX(0)}}"
        "@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}")

st.set_page_config(page_title="Untuk kamu", page_icon="♥", layout="centered")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=DM+Sans:wght@400;500&family=Great+Vibes&display=swap');
__ROOT__
@keyframes fade{from{opacity:0}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes drift{0%{transform:translate(0,0);opacity:0}15%{opacity:.5}85%{opacity:.22}100%{transform:translate(var(--x),-108vh);opacity:0}}
@keyframes shine{from{background-position:120% 0}to{background-position:-120% 0}}
@keyframes beat{0%,100%{transform:scale(1)}14%{transform:scale(1.35)}28%{transform:scale(1)}42%{transform:scale(1.22)}}
@keyframes breathe{50%{opacity:.45;transform:scale(1.08)}}

.stApp{background:radial-gradient(ellipse at 50% -12%,rgba(198,166,107,.13) 0,transparent 46%),radial-gradient(ellipse at 12% 0,rgba(101,28,43,.8) 0,transparent 55%),radial-gradient(ellipse at 100% 100%,rgba(74,16,29,.9) 0,transparent 55%),#2B0B13;background-attachment:fixed;font-family:var(--sans);animation:fade 1.4s ease both}
.stApp,.stApp p,.stApp span,.stApp label,.stApp li{color:var(--iv);font-family:var(--sans)}
#MainMenu,footer,[data-testid="stToolbar"],[data-testid="stDecoration"],[data-testid="stHeaderActionElements"]{display:none!important}
[data-testid="stHeader"]{background:transparent}
.block-container{max-width:860px;padding-top:2.5rem;position:relative;z-index:2}
[data-testid="stCaptionContainer"],[data-testid="stCaptionContainer"] p{color:var(--mu)!important;font:italic 400 1.05rem var(--serif)!important;letter-spacing:.03em;text-align:center}
h1,h2,h3{font-family:var(--serif)!important;font-weight:400!important;color:var(--iv)!important;letter-spacing:.01em}

/* latar: debu champagne dan hati kecil yang naik pelan, plus vignette */
.fx{position:fixed;inset:0;pointer-events:none;z-index:1;overflow:hidden}
.fx::before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(245,239,230,.014) 0 1px,transparent 1px 4px)}
.fx::after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 50%,rgba(0,0,0,.42) 100%)}
.mt{position:absolute;bottom:-10px;width:var(--s);height:var(--s);border-radius:50%;background:var(--g);opacity:0;animation:drift var(--d) linear infinite;animation-delay:var(--w)}
.ht{position:absolute;bottom:-20px;font-size:var(--s);line-height:1;color:rgba(198,166,107,.6);opacity:0;animation:drift var(--d) linear infinite;animation-delay:var(--w)}

/* layar pembuka */
.gate{text-align:center;margin:11vh 0 2.4rem}
.gate>*{animation:up 1.3s cubic-bezier(.2,.7,.2,1) both}
.gate>:nth-child(1){animation-delay:.15s}.gate>:nth-child(2){animation-delay:.55s}.gate>:nth-child(3){animation-delay:.95s}.gate .ring::before{content:"";position:absolute;inset:-12px;border:1px dashed rgba(198,166,107,.45);border-radius:50%;animation:spin 30s linear infinite}
.gate h1{font-size:clamp(46px,9vw,80px)!important;font-weight:300!important;font-style:italic;margin:.2rem 0;padding:0}
.gate h1 .sh{background:linear-gradient(100deg,#F5EFE6 0,#F5EFE6 38%,#F1DDA8 47%,#C6A66B 50%,#F1DDA8 53%,#F5EFE6 62%,#F5EFE6 100%);background-size:220% 100%;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:shine 7s linear infinite}
.gate p{color:var(--mu);letter-spacing:.06em}

/* tombol utama: emas, teks selalu gelap (tidak pernah berubah putih saat hover/klik/fokus) */
.stButton>button{border-radius:2px;border:1px solid var(--hl);background:transparent;color:var(--iv);padding:.75rem 1.6rem;letter-spacing:.12em;transition:background-position .6s,transform .35s,box-shadow .35s,border-color .35s}
.stButton>button p{color:inherit!important;font-size:.9rem;letter-spacing:.12em}
.stButton>button[kind="primary"],.stButton>button[data-testid="stBaseButton-primary"]{background:linear-gradient(105deg,#A98A55 0%,#E9D3A0 42%,#C6A66B 62%,#A98A55 100%)!important;background-size:240% 100%!important;background-position:0 0!important;border:1px solid #E9D3A0!important;color:#2B0B13!important;font-weight:500;box-shadow:0 10px 30px rgba(0,0,0,.35);animation:ring 2.6s ease-out infinite}
.stButton>button[kind="primary"]:hover,.stButton>button[kind="primary"]:focus,.stButton>button[kind="primary"]:focus:not(:active),.stButton>button[kind="primary"]:active,
.stButton>button[data-testid="stBaseButton-primary"]:hover,.stButton>button[data-testid="stBaseButton-primary"]:focus,.stButton>button[data-testid="stBaseButton-primary"]:focus:not(:active),.stButton>button[data-testid="stBaseButton-primary"]:active{background:linear-gradient(105deg,#A98A55 0%,#E9D3A0 42%,#C6A66B 62%,#A98A55 100%)!important;background-size:240% 100%!important;background-position:100% 0!important;border-color:#F3E3BC!important;color:#2B0B13!important;transform:translateY(-2px);box-shadow:0 14px 38px rgba(198,166,107,.38)}
.stButton>button[kind="primary"] *,.stButton>button[data-testid="stBaseButton-primary"] *{color:#2B0B13!important}
.stButton>button:focus-visible{outline:2px solid var(--g);outline-offset:3px}

/* hiasan pemisah */
.od{display:flex;align-items:center;gap:18px;margin:2.4rem auto 1.2rem;max-width:420px}
.od i{flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--g))}
.od i:last-child{background:linear-gradient(90deg,var(--g),transparent)}
.od span{color:var(--g);font-size:15px;animation:beat 2.4s ease-in-out infinite}
</style>
""".replace("__ROOT__", ROOT)
st.markdown(CSS, unsafe_allow_html=True)


def emb(tpl, tinggi, **v):
    """Tampilkan komponen HTML (iframe) dengan palet dan font yang sama."""
    for k, x in {"ROOT": ROOT, "FONT": FONT, **v}.items():
        tpl = tpl.replace(f"__{k}__", str(x))
    components.html(tpl, height=tinggi)


def efek_latar():
    r = random.Random(7)
    debu = "".join(
        f'<i class="mt" style="left:{r.randint(0,100)}%;--s:{r.choice([1,1,2,2,3])}px;--d:{r.randint(18,38)}s;'
        f'--w:-{r.randint(0,38)}s;--x:{r.randint(-40,40)}px"></i>'
        for _ in range(34))
    hati = "".join(
        f'<b class="ht" style="left:{r.randint(4,96)}%;--s:{r.randint(10,18)}px;--d:{r.randint(26,44)}s;'
        f'--w:-{r.randint(0,40)}s;--x:{r.randint(-60,60)}px">♥</b>'
        for _ in range(9))
    return f'<div class="fx">{debu}{hati}</div>'


for k, v in {"buka": False}.items():
    st.session_state.setdefault(k, v)

st.markdown(efek_latar(), unsafe_allow_html=True)

# =====================================================
# 3) LAYAR PEMBUKA
# =====================================================
if not st.session_state.buka:
    # tombol muncul terakhir, setelah teks selesai tampil
    st.markdown("<style>.stButton{animation:up 1.2s 1.4s cubic-bezier(.2,.7,.2,1) both}</style>", unsafe_allow_html=True)
    st.markdown(
        '<div class="gate">'
        f'<h1><span class="sh">Hai, {html.escape(NAMA_DIA)}</span></h1>'
        '<p>Aku punya sesuatu buat kamuu 👀 HEHHEHE</p></div>', unsafe_allow_html=True)
    _, tengah, _ = st.columns([1, 1.2, 1])
    if tengah.button("Click Click Click", type="primary", use_container_width=True):
        st.session_state.buka = True
        st.rerun()
    st.stop()

# =====================================================
# 4) HERO: hitung waktu berdetak langsung
# =====================================================
HERO = """<!doctype html><html><head><meta charset="utf-8">__FONT__
<style>__ROOT__
@keyframes shine{from{background-position:120% 0}to{background-position:-120% 0}}
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;background:transparent;color:var(--iv);font-family:var(--sans);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;overflow:hidden}
h1{font:italic 300 clamp(40px,9vw,84px)/1.04 var(--serif);margin:0 0 20px;letter-spacing:-.01em;background:linear-gradient(100deg,#F5EFE6 0,#F5EFE6 38%,#F1DDA8 47%,#C6A66B 50%,#F1DDA8 53%,#F5EFE6 62%,#F5EFE6 100%);background-size:220% 100%;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:up 1.4s .2s cubic-bezier(.2,.7,.2,1) both,shine 7s linear 1.8s infinite}
.ln{width:90px;height:1px;background:var(--g);margin-bottom:20px;animation:grow 1.3s .8s cubic-bezier(.2,.7,.2,1) both}
p{margin:0 0 32px;color:var(--mu);letter-spacing:.05em;font-size:15px;animation:up 1.2s 1s cubic-bezier(.2,.7,.2,1) both}
.g{display:flex;flex-wrap:wrap;justify-content:center;row-gap:18px;animation:up 1.2s 1.3s cubic-bezier(.2,.7,.2,1) both}
.c{padding:0 24px 0 0;margin-right:24px;border-right:1px solid var(--hl)}
.c:last-child{border:0;margin:0;padding:0}
.c b{display:block;font:300 clamp(34px,6.4vw,56px)/1 var(--serif);font-variant-numeric:lining-nums tabular-nums}
.c:last-child b{color:var(--g)}
.c span{display:block;margin-top:6px;font-size:12px;letter-spacing:.1em;color:var(--g)}
@media(max-width:520px){.c{padding:0 12px 0 0;margin-right:12px}.c span{font-size:11px}}
</style></head><body><h1>Happy 1 Year 1 Month, ioo</h1><div class="ln"></div><p>__SUB__</p><div class="g" id="g"></div>
<script>
const S=new Date(__Y__,__M__,__D__),U=["tahun","bulan","hari","jam","menit","detik"],g=document.getElementById("g");
function tick(){const n=new Date();let m=(n.getFullYear()-S.getFullYear())*12+n.getMonth()-S.getMonth();
let a=new Date(S.getFullYear(),S.getMonth()+m,S.getDate());if(a>n){m--;a=new Date(S.getFullYear(),S.getMonth()+m,S.getDate())}
const r=Math.floor((n-a)/1000),v=[Math.floor(m/12),m%12,Math.floor(r/86400),Math.floor(r%86400/3600),Math.floor(r%3600/60),r%60];
g.innerHTML=v.map((x,i)=>'<div class="c"><b>'+String(x).padStart(2,"0")+'</b><span>'+U[i]+'</span></div>').join("")}
tick();setInterval(tick,1000);
</script></body></html>"""

emb(HERO, 380,
    SUB="Counting more and more and more days with you! 🥰🫶",
    Y=TANGGAL_JADIAN.year, M=TANGGAL_JADIAN.month - 1, D=TANGGAL_JADIAN.day)

# =====================================================
# 5) SURAT DALAM AMPLOP
#    amplop melayang -> ketuk -> segel terbuka, hati-hati beterbangan -> kertas surat muncul,
#    kata-kata tertulis satu per satu saat digulir, tanda tangan "ditulis", hati meledak di akhir.
# =====================================================
AMPLOP = """<!doctype html><html><head><meta charset="utf-8">__FONT__
<style>__ROOT__
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;background:transparent;font-family:var(--sans);color:var(--iv);overflow:hidden;position:relative}
@keyframes rot{to{transform:rotate(360deg)}}
@keyframes fl{50%{transform:translateY(-9px) rotate(-.6deg)}}
@keyframes pu{50%{opacity:.35}}
@keyframes br{50%{opacity:.5;transform:scale(1.1)}}
@keyframes rip{from{transform:scale(1);opacity:.75}to{transform:scale(2.4);opacity:0}}
@keyframes shine{from{background-position:120% 0}to{background-position:-120% 0}}
@keyframes rise{from{opacity:0;transform:translateY(40px) scale(.96)}}
@keyframes bob{50%{transform:translate(-50%,6px)}}
@keyframes burst{0%{opacity:0;transform:translate(0,0) scale(.3) rotate(0)}12%{opacity:1}100%{opacity:0;transform:translate(var(--dx),var(--dy)) scale(1) rotate(var(--r))}}

/* ---------- panggung amplop ---------- */
.stage{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:opacity .7s,transform .7s}
.stage.x{opacity:0;transform:scale(.97)}
.glow{position:absolute;left:50%;top:50%;width:620px;height:620px;margin:-310px 0 0 -310px;background:radial-gradient(circle,rgba(198,166,107,.24),transparent 62%);animation:br 5s ease-in-out infinite;pointer-events:none}
.hl{position:absolute;left:50%;top:50%;width:var(--z);height:var(--z);margin:calc(var(--z)/-2) 0 0 calc(var(--z)/-2);border-radius:50%;pointer-events:none}
.ra{--z:min(580px,132vw);border:1px dashed rgba(198,166,107,.22);animation:rot 80s linear infinite}
.rb{--z:min(450px,106vw);border:1px solid rgba(198,166,107,.15);animation:rot 60s linear infinite reverse}
.cn{position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;text-align:center;padding:0 12px}
.tt{font:italic 300 clamp(32px,7vw,52px)/1.1 var(--serif);margin:0;background:linear-gradient(100deg,#F5EFE6 0,#F5EFE6 38%,#F1DDA8 47%,#C6A66B 50%,#F1DDA8 53%,#F5EFE6 62%,#F5EFE6 100%);background-size:220% 100%;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:shine 7s linear infinite}
.sb{margin:10px 0 0;font:italic 400 clamp(17px,3.6vw,21px)/1.4 var(--serif);color:var(--mu)}

#env{position:relative;width:min(420px,84vw);aspect-ratio:3/2;margin:42px 0 36px;cursor:pointer;outline:none;animation:fl 5s ease-in-out infinite;transition:filter .4s}
#env:hover,#env:focus-visible{filter:drop-shadow(0 0 26px rgba(198,166,107,.4))}
#env.o{animation-play-state:paused;cursor:default}
.bk{position:absolute;inset:0;background:linear-gradient(160deg,#7a2a3b,#561624);border:1px solid rgba(198,166,107,.42);border-radius:4px;box-shadow:0 30px 60px rgba(0,0,0,.6)}
.lt{position:absolute;left:6%;right:6%;top:9%;bottom:5%;background:var(--iv);border-radius:2px;z-index:2;transition:transform 1s cubic-bezier(.6,0,.2,1) .55s}
.lt::before{content:"♥";position:absolute;left:0;right:0;top:12%;text-align:center;color:var(--g);font-size:15px}
.lt::after{content:"";position:absolute;left:12%;right:12%;top:36%;bottom:12%;background:repeating-linear-gradient(transparent 0 13px,rgba(129,59,73,.22) 13px 14px)}
.ft{position:absolute;inset:0;background:linear-gradient(165deg,#8d4151,#6a2233);clip-path:polygon(0 0,50% 58%,100% 0,100% 100%,0 100%);z-index:3;border-radius:4px}
.vl{position:absolute;inset:0;width:100%;height:100%;z-index:3;pointer-events:none}
.ad{position:absolute;left:0;right:0;bottom:8%;text-align:center;z-index:3;font:400 clamp(21px,5.6vw,30px)/1 'Great Vibes',cursive;color:var(--g)}
.fp{position:absolute;inset:0;background:linear-gradient(180deg,#964858,#6d2535);clip-path:polygon(0 0,100% 0,50% 58%);transform-origin:top;transform:perspective(900px) rotateX(0);transition:transform .9s cubic-bezier(.6,0,.2,1);z-index:4}
.sl{position:absolute;left:50%;top:57%;width:15%;aspect-ratio:1;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle at 35% 30%,#F0DDAA,#C6A66B 55%,#8F7339);color:#4A101D;display:grid;place-items:center;font-size:clamp(14px,3.4vw,22px);z-index:5;box-shadow:0 6px 16px rgba(0,0,0,.5),inset 0 0 0 3px rgba(74,16,29,.2);transition:opacity .35s,transform .5s}
.sl::before,.sl::after{content:"";position:absolute;inset:0;border-radius:50%;border:1px solid var(--g);animation:rip 2.6s ease-out infinite}
.sl::after{animation-delay:1.3s}
#env.o .fp{transform:perspective(900px) rotateX(180deg);z-index:1}
#env.o .lt{transform:translateY(-44%)}
#env.o .sl{opacity:0;transform:translate(-50%,-50%) scale(.5)}
#env.o .sl::before,#env.o .sl::after{animation:none}
.hint{font:italic 400 19px var(--serif);color:var(--g);letter-spacing:.06em;animation:pu 2.4s ease-in-out infinite}

/* ---------- kertas surat ---------- */
.sheet{position:relative;display:none;width:min(660px,94vw);height:calc(100% - 36px);margin:18px auto 0;border:1px solid var(--g);background:radial-gradient(ellipse at 18% 0,rgba(198,166,107,.17),transparent 55%),radial-gradient(ellipse at 100% 100%,rgba(129,59,73,.1),transparent 55%),var(--iv);box-shadow:0 40px 90px rgba(0,0,0,.65),0 0 0 7px rgba(198,166,107,.08)}
.sheet.show{display:block;animation:rise 1.1s cubic-bezier(.2,.7,.2,1) both}
.sheet::before{content:"";position:absolute;inset:11px;border:1px solid rgba(169,138,85,.55);pointer-events:none;z-index:3}
.k{position:absolute;width:30px;height:30px;z-index:4;pointer-events:none}
.k::after{content:"";position:absolute;width:7px;height:7px;background:var(--g);transform:rotate(45deg)}
.k1{top:5px;left:5px;border-top:2px solid var(--g);border-left:2px solid var(--g)}.k1::after{top:-4px;left:-4px}
.k2{top:5px;right:5px;border-top:2px solid var(--g);border-right:2px solid var(--g)}.k2::after{top:-4px;right:-4px}
.k3{bottom:5px;left:5px;border-bottom:2px solid var(--g);border-left:2px solid var(--g)}.k3::after{bottom:-4px;left:-4px}
.k4{bottom:5px;right:5px;border-bottom:2px solid var(--g);border-right:2px solid var(--g)}.k4::after{bottom:-4px;right:-4px}
.pg{position:absolute;top:0;left:0;right:0;height:3px;z-index:5;background:rgba(169,138,85,.15)}
#bar{display:block;height:100%;width:0;background:linear-gradient(90deg,#A98A55,#C6A66B,#F0DDAA);box-shadow:0 0 8px rgba(198,166,107,.7)}
#sc{position:absolute;inset:0;overflow-y:auto;overflow-x:hidden;padding:58px clamp(28px,8vw,68px) 80px;scrollbar-width:thin;scrollbar-color:var(--g) transparent;-webkit-mask-image:linear-gradient(transparent 0,#000 34px,#000 calc(100% - 46px),transparent 100%);mask-image:linear-gradient(transparent 0,#000 34px,#000 calc(100% - 46px),transparent 100%)}
#sc::-webkit-scrollbar{width:5px}#sc::-webkit-scrollbar-thumb{background:var(--g);border-radius:3px}
#sh{position:absolute;bottom:20px;left:50%;transform:translateX(-50%);z-index:5;font:italic 500 17px var(--serif);color:var(--ag);animation:bob 1.8s ease-in-out infinite;transition:opacity .5s;pointer-events:none}
#sh.hd{opacity:0}

.lh{text-align:center}
.mono{position:relative;width:54px;height:54px;margin:0 auto 14px;border:1px solid var(--g);border-radius:50%;display:grid;place-items:center;color:var(--wn);font-size:20px}
.mono::after{content:"";position:absolute;inset:-7px;border:1px dashed rgba(169,138,85,.65);border-radius:50%;animation:rot 40s linear infinite}
.dt{font:italic 500 18px var(--serif);color:var(--ag);letter-spacing:.08em}
.to{font:italic 500 clamp(22px,4.4vw,27px)/1.3 var(--serif);color:var(--mb);margin:34px 0 8px;text-align:center}
.jd{font:italic 400 clamp(36px,8vw,56px)/1.08 var(--serif);color:var(--bu);text-align:center;margin:0 0 22px}
.sep{display:flex;align-items:center;gap:14px;color:var(--g);margin:0 auto 32px;max-width:230px;justify-content:center}
.sep i{flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--g))}
.sep i:last-child{background:linear-gradient(90deg,var(--g),transparent)}
.bd{font:500 clamp(19px,3.7vw,22px)/1.78 var(--serif);color:#3a0e18;margin:0 0 1.35em}
.bd.it{font-style:italic;text-align:center;margin-top:26px}
.lv{margin:46px 0 40px;padding:32px 6px;text-align:center;font:italic 500 clamp(24px,4.8vw,30px)/1.4 var(--serif);color:var(--bu);border-top:1px solid var(--g);border-bottom:1px solid var(--g)}
.cl{font:italic 400 clamp(26px,5.4vw,34px)/1.2 var(--serif);color:var(--wn);text-align:center;margin:0 0 6px}
.sg{text-align:center;margin-top:34px}
.ap{display:block;font:italic 500 22px var(--serif);color:var(--mb)}
.nm{display:inline-block;font:400 clamp(50px,11vw,68px)/1.25 'Great Vibes',cursive;color:var(--wn);padding:4px 26px 18px}
.end{text-align:center;color:var(--g);margin-top:14px;letter-spacing:.7em;padding-left:.7em}

/* kata muncul satu per satu: tinta emas yang mengering jadi tinta burgundy */
.w{display:inline-block;opacity:0;transform:translateY(9px);color:#C6A66B;transition:opacity .8s ease,transform .8s cubic-bezier(.2,.7,.2,1),color 1.8s ease;transition-delay:calc(var(--i)*30ms)}
.in .w{opacity:1;transform:none;color:inherit}
.wr{clip-path:inset(0 100% 0 0);transition:clip-path 2.4s cubic-bezier(.5,0,.2,1) .4s}
.wr.in{clip-path:inset(0 0 0 0)}

/* partikel hati & kilau */
#fx{position:fixed;inset:0;pointer-events:none;z-index:20;overflow:hidden}
.pt{position:absolute;left:var(--x);top:var(--y);font-size:var(--s);color:var(--c);opacity:0;animation:burst var(--t) cubic-bezier(.1,.7,.3,1) forwards}
</style></head><body>
<div class="stage" id="stage">
 <div class="glow"></div><div class="hl ra"></div><div class="hl rb"></div>
 <div class="cn">
  <h2 class="tt">Love letter for Ravi Romario <3</h2>
  <div id="env" tabindex="0" role="button" aria-label="Open!">
   <div class="bk"></div><div class="lt"></div><div class="ft"></div>
   <svg class="vl" viewBox="0 0 300 200" preserveAspectRatio="none"><path d="M0 0 L150 116 L300 0 M0 200 L112 98 M300 200 L188 98" fill="none" stroke="rgba(198,166,107,.4)" stroke-width="1" vector-effect="non-scaling-stroke"/></svg>
   </div><div class="sl">♥</div>
  </div>
  <div class="hint" id="hint">ketuk amplopnya ✦</div>
 </div>
</div>
<div class="sheet" id="sheet">
 <div class="pg"><i id="bar"></i></div>
 <b class="k k1"></b><b class="k k2"></b><b class="k k3"></b><b class="k k4"></b>
 <div id="sc"></div><div id="sh">scroll down</div>
</div>
<div id="fx"></div>
<script>
const D=__DATA__,COL=["#C6A66B","#E9DFD2","#813B49","#F0DDAA"];
const $=id=>document.getElementById(id);
const env=$("env"),stage=$("stage"),sheet=$("sheet"),sc=$("sc"),bar=$("bar"),sh=$("sh"),fx=$("fx");

/* susun isi surat; kata dibungkus supaya bisa muncul bertahap */
function el(tag,cls,txt,kata){const e=document.createElement(tag);e.className=cls;
 if(kata){txt.split(" ").forEach((w,i)=>{const s=document.createElement("span");s.className="w";s.style.setProperty("--i",i);s.textContent=w;e.appendChild(s);e.appendChild(document.createTextNode(" "))})}
 else e.textContent=txt;return e}
const L=document.createElement("div");
const hd=document.createElement("div");hd.className="lh";hd.innerHTML='<div class="mono">♥</div>';
const dt=document.createElement("div");dt.className="dt";dt.textContent=D.tanggal;hd.appendChild(dt);
const sp=document.createElement("div");sp.className="sep";sp.innerHTML="<i></i><span>✦</span><i></i>";
L.append(hd,el("p","to rv",D.salam,1),el("h2","jd rv",D.judul,1),sp);
D.isi.forEach(t=>L.append(el("p","bd rv",t,1)));
L.append(el("blockquote","lv rv",D.cinta,1),el("h3","cl rv",D.penutup,1),el("p","bd it rv",D.terima,1));
const sg=document.createElement("div");sg.className="sg";sg.append(el("span","ap rv",D.ttd_pre,1),el("span","nm rv wr",D.ttd,0));L.append(sg);
const end=document.createElement("div");end.className="end";end.textContent="♥ ♥ ♥";L.append(end);
sc.append(L);

/* ledakan hati dan kilau emas */
function burst(x,y,n){for(let k=0;k<n;k++){const e=document.createElement("i"),a=Math.random()*Math.PI*2,d=90+Math.random()*190;
 e.className="pt";e.textContent=Math.random()<.55?"♥":"✦";
 e.style.cssText="--x:"+x+"px;--y:"+y+"px;--dx:"+Math.cos(a)*d+"px;--dy:"+(Math.sin(a)*d-60)+"px;--r:"+((Math.random()-.5)*160)+"deg;--s:"+(10+Math.random()*16)+"px;--t:"+(1.4+Math.random()*1.2)+"s;--c:"+COL[k%4];
 fx.appendChild(e);setTimeout(()=>e.remove(),3000)}}

function mulai(){
 const io=new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){x.target.classList.add("in");io.unobserve(x.target)}}),{root:sc,threshold:.15,rootMargin:"0px 0px -6% 0px"});
 sc.querySelectorAll(".rv").forEach(n=>io.observe(n));
 const fin=new IntersectionObserver(es=>{if(es[0].isIntersecting){fin.disconnect();const b=sheet.getBoundingClientRect();burst(b.left+b.width/2,b.bottom-120,46)}},{root:sc,threshold:1});
 fin.observe(end);
 sc.onscroll=()=>{const m=sc.scrollHeight-sc.clientHeight;bar.style.width=(m>0?sc.scrollTop/m*100:0)+"%";sh.classList.toggle("hd",sc.scrollTop>40)};
}

function buka(){if(env.classList.contains("o"))return;env.classList.add("o");$("hint").style.visibility="hidden";
 const r=env.getBoundingClientRect();
 setTimeout(()=>burst(r.left+r.width/2,r.top+r.height*.45,38),700);
 setTimeout(()=>stage.classList.add("x"),1900);
 setTimeout(()=>{stage.style.display="none";sheet.classList.add("show");mulai()},2650)}
env.onclick=buka;
env.onkeydown=e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();buka()}};
</script></body></html>"""

DATA = json.dumps(
    dict(salam=SALAM, judul=JUDUL, isi=ISI, cinta=CINTA, penutup=PENUTUP, terima=TERIMA,
         ttd_pre=TTD_PRE, ttd=TTD, tanggal=TANGGAL_SURAT),
    ensure_ascii=False).replace("</", "<\\/")

st.markdown('<div class="od"><i></i><span>♥</span><i></i></div>', unsafe_allow_html=True)
emb(AMPLOP, 760, DATA=DATA)

# =====================================================
# 6) PERTANYAAN TERAKHIR (tombol "Pikir dulu" kabur)
# =====================================================
FINAL = """<!doctype html><html><head><meta charset="utf-8">__FONT__
<style>__ROOT__
body{margin:0;background:transparent;color:var(--iv);font-family:var(--sans);text-align:center}
#s{position:relative;height:320px;overflow:hidden;background:radial-gradient(ellipse at 50% 0,rgba(198,166,107,.16),transparent 60%),linear-gradient(#4A101D,#2B0B13);border:1px solid var(--g)}
#s::before{content:"";position:absolute;inset:9px;border:1px solid var(--hl);pointer-events:none}
h2{font:italic 300 clamp(32px,6vw,50px)/1.15 var(--serif);margin:48px 14px 34px}
button{font:500 14px var(--sans);letter-spacing:.1em;border-radius:2px;padding:14px 36px;cursor:pointer;margin:0 8px;transition:filter .35s,transform .35s,border-color .35s}
#y{background:linear-gradient(105deg,#A98A55,#E9D3A0 45%,#C6A66B);color:var(--mr);border:1px solid #E9D3A0}
#y:hover,#y:focus-visible{filter:brightness(1.1);transform:translateY(-2px);color:var(--mr)}
#n{background:transparent;color:var(--iv);border:1px solid var(--hl);transition:left .15s,top .15s}
#m{display:none;font:italic 400 clamp(24px,5vw,34px)/1.35 var(--serif);padding:56px 24px 0}
.sg{font:400 clamp(40px,8vw,56px)/1 'Great Vibes',cursive;color:var(--g);margin-top:22px}
.f{position:absolute;bottom:-40px;animation:fl linear forwards}
@keyframes fl{to{transform:translateY(-380px);opacity:0}}
</style></head><body><div id="s"><h2>Jadi kapan kita bertemu? AKU KANGEN!!!</h2>
<button id="y">Besok</button><button id="n">Liat nanti ya</button><div id="m">__PESAN__<div class="sg">__TTD__</div></div></div>
<script>
const s=document.getElementById("s"),y=document.getElementById("y"),n=document.getElementById("n"),m=document.getElementById("m");
function kabur(e){e.preventDefault();n.style.position="absolute";
n.style.left=Math.random()*(s.clientWidth-140)+"px";n.style.top=(120+Math.random()*(s.clientHeight-180))+"px"}
n.onmouseover=kabur;n.ontouchstart=kabur;n.onclick=kabur;
y.onclick=()=>{document.querySelector("h2").style.display="none";y.style.display=n.style.display="none";m.style.display="block";
for(let k=0;k<36;k++){const e=document.createElement("b");e.textContent="♥";e.className="f";
e.style.cssText="left:"+Math.random()*100+"%;font-size:"+(14+Math.random()*20)+"px;animation-duration:"+(4+Math.random()*3)+"s;animation-delay:"+Math.random()*1.8+"s;color:"+["#C6A66B","#E9DFD2","#813B49"][k%3];
s.appendChild(e)}};
</script></body></html>"""

st.markdown('<div class="od"><i></i><span>♥</span><i></i></div>', unsafe_allow_html=True)
emb(FINAL, 340,
    PESAN=html.escape(
        f"HAHHAHA bercanda sayaanggg.. Love you! >.<"),
    TTD=html.escape(NAMA_KAMU))
