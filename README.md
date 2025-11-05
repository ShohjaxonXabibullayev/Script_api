🎯 Maqsadi

Ushbu loyiha test API (https://test.icorp.uz/interview.php) bilan ishlash orqali HTTP so‘rovlar (POST va GET) va webhook mexanizmini amalda ko‘rsatadi.

⚙️ Ishlash algoritmi

1️⃣ POST so‘rov yuboriladi:

Endpoint: https://test.icorp.uz/interview.php

JSON ma’lumot:

{
  "msg": "Salom, bu mening xabarim",
  "url": "https://webhook.site/your-unique-url"
}


Javobda part1 (1-qism kodi) olinadi.

2️⃣ Ko‘rsatilgan url (masalan, webhook.site) manziliga part2 (2-qism kodi) avtomatik yuboriladi.

3️⃣ Ikkala kod (part1 + part2) birlashtiriladi:

3e9e3c34-39e8-48b1-9106-2532b2cc1374


4️⃣ GET so‘rov yuboriladi:

https://test.icorp.uz/interview.php?code=3e9e3c34-39e8-48b1-9106-2532b2cc1374


5️⃣ Natijada server yuborilgan asl xabarni qaytaradi:

{"msg": "Salom, bu mening xabarim"}

🚀 Ishga tushirish

1️⃣ Python virtual muhit yaratish (ixtiyoriy):

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac


2️⃣ Kerakli kutubxona o‘rnatish:

pip install requests


3️⃣ Dastur faylini ishga tushirish:

python main.py


4️⃣ Terminalda ko‘rsatmalarga amal qiling:

1-qism kodi avtomatik chiqadi

Webhook sahifasidan part2 ni olib kiriting
