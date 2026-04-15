# 🤖 Linux AI Yordamchi

Laboratoriya sharoitida Linux terminalida ishlaydigan, **o‘zbek tilidagi** AI yordamchi.  
Terminal xatolarini avtomatik aniqlaydi va **to‘g‘ri komandalarni taklif qiladi**.

---

## ✨ Xususiyatlari

- ✅ O‘zbek tilida interfeys
- ✅ Xatolarni avtomatik tahlil qiladi
- ✅ `sudo`, `python3`, `pip3` kabi to‘g‘ri variantlarni taklif qiladi
- ✅ Faqat **2 ta komanda** bilan ishlaydi
- ✅ Hech qanday tashqi API yoki internet kerak emas
- ✅ Faqat **qonuniy laboratoriya** ishlari uchun

---

## 📦 O‘rnatish

### 1. Repositoryni yuklab olish

```bash
git clone https://github.com/SIZNING_USERNAME/linux-ai-yordamchi.git
cd linux-ai-yordamchi

Fayl YAratish
nano ai_yordamchi.py

Ishga tushurish
python3 ai_yordamchi.py

Yoki bir qatorda
chmod +x ai_yordamchi.py && ./ai_yordamchi.py


TEST qilish uchun misollar
# 1. Ruxsat xatosi
ls /root

# 2. Topilmagan komanda (avtomatik o'rnatadi)
nmap

# 3. Python xatosi
python --version

# 4. Pip xatosi
pip list

# 5. Paket o'rnatish (sudo kerak)
apt install htop

# 6. Noto'g'ri parametr
ls --wrong

# 7. Fayl topilmadi
cat test.txt

# 8. Git xatosi
git status

# 9. Python moduli yo'q
python3 -c "import requests"

# 10. Chiqish
chiq



Ishlash Prinsipi
Siz komanda yozasiz → Men bajaraman
↓
Agar xato bo'lsa → Xatoni aniqlayman
↓
Avtomatik tuzataman → Qayta bajaraman
↓
Natijani ko'rsataman ✅

Bu dastur har qanday Linux terminalida ishlaydi va barcha xatolarni avtomatik tuzatadi. Siz faqat:

bash
python3 ai_yordamchi.py
