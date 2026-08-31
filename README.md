<div align="center">

# 🛒 Shopping API

**A clean e-commerce REST API built with Django REST Framework — categories, products, and order placement**

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/DRF-A30000?style=flat-square&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" />
</p>

<p>
  <a href="https://github.com/Raximboy7/shopingApi/stargazers"><img src="https://img.shields.io/github/stars/Raximboy7/shopingApi?style=flat-square&color=8B5CF6&labelColor=0D1117" alt="stars" /></a>
  <a href="https://github.com/Raximboy7/shopingApi/commits"><img src="https://img.shields.io/github/last-commit/Raximboy7/shopingApi?style=flat-square&color=8B5CF6&labelColor=0D1117" alt="last commit" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-8B5CF6?style=flat-square&labelColor=0D1117" alt="license" /></a>
</p>

</div>

---

## 📖 Overview

A compact but complete shopping backend. It exposes a browsable REST API for a product catalogue
and lets a customer place an order for a product with a phone number — no account required for
reading, staff-only for writing.

The project is intentionally small so the DRF building blocks stay visible: **ModelSerializer**
for shaping payloads, **ModelViewSet + DefaultRouter** for CRUD, a custom **`@action`** for nested
resources, and a custom **permission class** for the read/write split.

---

## ✨ Features

- 🗂 **Category catalogue** with slug, name and image
- 📦 **Products** linked to a category, with price, description and stock quantity
- 🔗 **Nested route** — fetch every product inside one category in a single request
- 🛍 **Order placement** — `POST` a quantity and phone number against a product
- 📜 **Purchase history** endpoint
- 🔐 **`IsAdminOrReadOnly`** — anyone can read, only staff can create / update / delete
- 🧭 **Browsable API** — explore and test every endpoint from the browser
- 🖼 **Image uploads** for category artwork via `ImageField`

---

## 🧩 Data model

```
Category ──1───────∞── Product ──1───────∞── Buy
  slug                   title                quantity
  name                   price                phone
  img                    description          product (FK)
                         quantity
```

---

## 🔌 API Reference

Base URL: `http://127.0.0.1:8000/`

| Method | Endpoint | Description | Auth |
|---|---|---|:-:|
| `GET` | `/categories/` | List all categories | — |
| `POST` | `/categories/` | Create a category | 🔑 staff |
| `GET` | `/categories/{id}/` | Retrieve one category | — |
| `PUT` `PATCH` | `/categories/{id}/` | Update a category | 🔑 staff |
| `DELETE` | `/categories/{id}/` | Delete a category | 🔑 staff |
| `GET` | `/categories/{id}/products/` | All products in that category | — |
| `GET` | `/products/` | List all products | — |
| `POST` | `/products/` | Create a product | 🔑 staff |
| `GET` | `/products/{id}/` | Retrieve one product | — |
| `GET` | `/products/{id}/buy/` | Product details for the order form | — |
| `POST` | `/products/{id}/buy/` | Place an order | — |
| `GET` | `/purchase_history/` | List placed orders | — |
| `GET` | `/admin/` | Django admin panel | 🔑 staff |

### Example — list products

```bash
curl http://127.0.0.1:8000/products/
```

```json
[
  {
    "slug": { "slug": "phones", "name": "Smartphones", "img": "/media/phones.jpg" },
    "title": "Redmi Note 13",
    "price": 2400000,
    "description": "6.67\" AMOLED, 108 MP camera, 5000 mAh",
    "quantity": 12
  }
]
```

### Example — place an order

```bash
curl -X POST http://127.0.0.1:8000/products/1/buy/ \
  -H "Content-Type: application/json" \
  -d '{"quantity": 2, "phone": "+998901234567", "product": 1}'
```

---

## 🚀 Getting Started

```bash
# 1 — clone
git clone https://github.com/Raximboy7/shopingApi.git
cd shopingApi

# 2 — virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3 — dependencies
pip install -r requirements.txt

# 4 — environment variables
cp .env.example .env              # then edit .env

# 5 — database
python manage.py migrate
python manage.py createsuperuser

# 6 — run
python manage.py runserver
```

Open <http://127.0.0.1:8000/> for the browsable API.

---

## 🔧 Configuration

Create a `.env` file next to `manage.py` (start from `.env.example`):

| Variable | Description | Default |
|---|---|---|
| `SECRET_KEY` | Django secret key — **never commit the real value** | — |
| `DEBUG` | `True` in development, `False` in production | `False` |
| `ALLOWED_HOSTS` | Comma-separated host list | `127.0.0.1,localhost` |

---

## 📁 Project Structure

```
shopingApi/
├── config/              # project settings, root urls, wsgi/asgi
│   ├── settings.py
│   └── urls.py
├── API/                 # the application
│   ├── models.py        # Category, Product, Buy
│   ├── serializers.py   # ModelSerializers (+ nested category)
│   ├── views.py         # ViewSets + BuyOrder generic view
│   ├── permissions.py   # IsAdminOrReadOnly
│   ├── urls.py          # DefaultRouter registration
│   └── admin.py
├── media/               # uploaded category images
├── requirements.txt
├── .env.example
└── manage.py
```

---

## 🗓 Roadmap

- [ ] Return `201 Created` with the order payload instead of redirecting after `POST /buy/`
- [ ] Decrease `Product.quantity` inside a transaction when an order is placed
- [ ] Rename `Product.slug` → `Product.category` (the field is a FK, not a slug)
- [ ] Use `DecimalField` for `price` instead of `IntegerField`
- [ ] Token / JWT authentication and per-user purchase history
- [ ] Pagination, search and ordering filters
- [ ] OpenAPI schema with `drf-spectacular`
- [ ] Tests with `APITestCase`

---

<details>
<summary><b>🇺🇿 &nbsp;O'zbekcha tavsif</b></summary>

<br/>

## 📖 Loyiha haqi

**Django REST Framework** asosida yozilgan onlayn do'kon backend'i. Mahsulot katalogi uchun
brauzerdan ko'rish mumkin bo'lgan REST API beradi va mijozga telefon raqami orqali buyurtma
berish imkonini yaratadi — o'qish hamma uchun ochiq, yozish faqat admin uchun.

Loyiha ataylab kichik qilingan: DRF'ning asosiy qismlari yaqqol ko'rinib tursin —
**ModelSerializer**, **ModelViewSet + DefaultRouter**, ichki resurs uchun **`@action`**,
va o'qish/yozish huquqlarini ajratuvchi maxsus **permission** klassi.

## ✨ Imkoniyatlar

- 🗂 Kategoriyalar (nom, slug, rasm)
- 📦 Mahsulotlar (narx, tavsif, ombordagi soni)
- 🔗 Bitta so'rov bilan kategoriya ichidagi barcha mahsulotlar
- 🛍 Buyurtma berish (soni + telefon raqami)
- 📜 Buyurtmalar tarixi
- 🔐 `IsAdminOrReadOnly` — o'qish hammaga, o'zgartirish faqat adminga
- 🧭 Brauzerdan API'ni sinab ko'rish

## 🚀 Ishga tushirish

```bash
git clone https://github.com/Raximboy7/shopingApi.git
cd shopingApi

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env              # va .env ni to'ldiring

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Brauzerda <http://127.0.0.1:8000/> ni oching.

## ⚠️ Muhim

`SECRET_KEY` va boshqa maxfiy qiymatlar `.env` faylida saqlanadi va **hech qachon git'ga
qo'shilmaydi**. `.env.example` — bu faqat namuna, unda haqiqiy kalit bo'lmasligi kerak.

</details>

---

## 🤝 Contributing

Issue va Pull Request'lar ochiq. Katta o'zgarishdan oldin issue orqali muhokama qiling.

## 📄 License

MIT — batafsil [`LICENSE`](LICENSE) faylida.

## 👤 Author

**Raximboy Ibrohimov** — Backend &amp; Mobile Developer, Tashkent 🇺🇿

[![Portfolio](https://img.shields.io/badge/Portfolio-8B5CF6?style=flat-square&logo=googlechrome&logoColor=white)](https://ibrohimov-dev.uz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raximboy-ibroximov-a75855268/)
[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/Raximboy7)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:raximboy4200@gmail.com)

<div align="center"><sub>⭐ Foydali bo'lsa, yulduzcha qoldiring!</sub></div>
