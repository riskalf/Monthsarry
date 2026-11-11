# Monthsary

Kejutan monthsary berbentuk aplikasi web kecil yang dibuat dengan [Streamlit](https://streamlit.io): surat yang tampil seperti diketik, timeline kenangan, galeri foto, playlist, kartu "buka kalau...", dan kupon.

## Struktur folder

```
Monthsarry/
├─ app.py                  # kode utama aplikasi
├─ requirements.txt        # daftar library untuk deploy
├─ .streamlit/
│  └─ config.toml          # tema terang
├─ foto/                   # taruh foto kalian di sini (jpg, png, webp)
├─ README.md
├─ .gitignore
└─ LICENSE
```

## Menjalankan di komputer

```bash
pip install -r requirements.txt
streamlit run app.py
```

Aplikasi akan terbuka di `http://localhost:8501`.

## Menyesuaikan isi

Semua teks ada di bagian paling atas `app.py`, di bawah judul "EDIT BAGIAN INI DULU":

- `NAMA_DIA`, `NAMA_KAMU`, `TANGGAL_JADIAN`
- `KENANGAN`, `SURAT`, `PERJALANAN`
- `LAGU`, `ALASAN`, `BUKA_KALAU`, `KUPON`
- `SPOTIFY_EMBED_URL` (opsional, untuk menampilkan player playlist)

Foto ditaruh di folder `foto/`. Nama file menjadi keterangan foto, misalnya `pantai_pertama.jpg` tampil sebagai "pantai pertama".

## Deploy

Deploy lewat [Streamlit Community Cloud](https://share.streamlit.io) dengan main file `app.py`.

> Repo ini berisi surat dan foto pribadi, jadi sebaiknya dibuat **private** di GitHub.
