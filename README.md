<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,100:00D4FF&height=200&section=header&text=TradeHub&fontSize=80&fontColor=ffffff&fontAlignY=38&desc=A%20Digital%20Marketplace%20Built%20with%20Flask&descAlignY=60&descSize=18&animation=fadeIn" width="100%"/>

<br/>

<!-- Badges -->
<!-- Language & Frontend -->

![Python](https://img.shields.io/badge/Python-3.11.0-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Templates-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Custom%20Styles-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-3.1.6-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

<!-- Backend & Database -->

![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?style=for-the-badge&logo=flask&logoColor=white)
![Werkzeug](https://img.shields.io/badge/Werkzeug-3.1.5-FF6600?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.46-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

<!-- Flask Extensions -->

![Flask--Login](https://img.shields.io/badge/Flask--Login-0.6.3-FF7043?style=for-the-badge&logo=flask&logoColor=white)
![Flask--Bcrypt](https://img.shields.io/badge/Flask--Bcrypt-1.0.1-4CAF50?style=for-the-badge&logo=flask&logoColor=white)
![Flask--WTF](https://img.shields.io/badge/Flask--WTF-1.2.2-00BCD4?style=for-the-badge&logo=flask&logoColor=white)

<!-- Meta -->

![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

<br/>

> **TradeHub** is a full-stack marketplace web app where users can register, log in, buy & sell items with real budget logic — if you own it, no one else can buy it until you sell it back.

<br/>

[✨ Features](#-features) • [🖼 Screenshots](#-screenshots) • [⚙ Tech Stack](#-tech-stack) • [🚀 Installation](#-installation) • [💡 How It Works](#-how-it-works) • [🔮 Roadmap](#-roadmap)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔐 Auth System

- ✅ User Registration
- ✅ Secure Login & Logout
- ✅ Session Management via Flask-Login
- ✅ Password hashing

</td>
<td width="50%">

### 🛒 Marketplace

- ✅ Browse all available items
- ✅ Buy items — instantly removed from market
- ✅ Sell items back — returns to market
- ✅ Real-time budget updates

</td>
</tr>
<tr>
<td width="50%">

### 💰 Budget Logic

- ✅ Every user starts with **$1,000** default balance
- ✅ Buying deducts from balance
- ✅ Selling adds back to balance
- ✅ Can't buy what you can't afford

</td>
<td width="50%">

### 🗑 Account Management

- ✅ Delete account with confirmation modal
- ✅ All owned items returned to market on deletion
- ✅ Instant session termination
- ✅ Flash notification system

</td>
</tr>
</table>

---

## 🎯 The Core Mechanic

```
User buys item  →  Item LOCKED to that user  →  No one else can buy it
User sells item →  Item RELEASED back to market →  Anyone can buy it again
```

> This creates a real ownership system. Items aren't infinite — supply is limited.

---

## 🖼 Screenshots

| Page              | Preview                                        |
| ----------------- | ---------------------------------------------- |
| 🏠 Home           | ![Home](screenshots/home.png)                  |
| 📝 Register       | ![Register](screenshots/register.png)          |
| 🔐 Login          | ![Login](screenshots/login.png)                |
| 🛒 Market         | ![Market](screenshots/market.png)              |
| 🔍 Item Details   | ![Details](screenshots/show_details_modal.png) |
| 💸 Buy Item       | ![Buy Modal](screenshots/buy_modal.png)        |
| 📦 Owned Items    | ![Owned Items](screenshots/owned_items.png)    |
| 💵 Sell Item      | ![Sell Modal](screenshots/sell_modal.png)      |
| ❌ Delete Account | ![Delete Modal](screenshots/delete_modal.png)  |

---

## 📂 Project Structure

```
tradehub/
│
├── app/
│   ├── static/
│   │   └── css/
│   │       └── style.css                   # Custom styles, glassmorphism, gradients
│   │
│   ├── templates/
│   │   ├── includes/
│   │   │   ├── market_items_modals.html    # Buy & details modals for each item
│   │   │   └── owned_items_modal.html      # Sell modals for owned items
│   │   │
│   │   ├── base.html                       # Base layout (navbar, flash messages)
│   │   ├── home.html                       # Landing page
│   │   ├── login.html                      # Login form
│   │   ├── register.html                   # Register form
│   │   └── market.html                     # Marketplace (buy/sell/owned items)
│   │
│   ├── __init__.py                         # App factory, DB init
│   ├── forms.py                            # WTForms (Register, Login, Market)
│   ├── models.py                           # User & Item models
│   └── routes.py                           # All application routes
│
├── config/
│   ├── .env                                # Secret keys (not committed)
│   └── .env.example                        # Template for environment setup
│
├── instance/
│   └── market.db                           # SQLite database (auto-generated)(not committed)
│
├── screenshots/                            # App screenshots for README
│   ├── home.png
│   ├── register.png
│   ├── login.png
│   ├── market.png
│   ├── show_details_modal.png
│   ├── buy_modal.png
│   ├── owned_items.png
│   ├── sell_modal.png
│   └── delete_modal.png
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── run.py                                  # Entry point
```

---

## ⚙ Tech Stack

| Layer         | Technology                             | Version        |
| ------------- | -------------------------------------- | -------------- |
| **Language**  | Python                                 | 3.11.0         |
| **Framework** | Flask                                  | 3.1.2          |
| **ORM**       | Flask-SQLAlchemy + SQLAlchemy          | 3.1.1 + 2.0.46 |
| **Auth**      | Flask-Login + Flask-Bcrypt             | 0.6.3 + 1.0.1  |
| **Forms**     | Flask-WTF + WTForms                    | 1.2.2 + 3.2.1  |
| **Config**    | python-dotenv                          | 1.2.1          |
| **Database**  | SQLite                                 | —              |
| **Frontend**  | Bootstrap 5 + Custom CSS               | 5.x            |
| **Icons**     | Bootstrap Icons                        | —              |
| **Styling**   | Glassmorphism + Gradients + Animations | —              |

---

## 💡 How It Works

### 💸 Buying an Item

```
1. User clicks "Purchase"
2. Modal pops up showing item name + price
3. Form submits to POST /market
4. Server checks: user.budget >= item.price
5. If affordable:
      item.owner = current_user.id
      current_user.budget -= item.price
      db.session.commit()
6. Item DISAPPEARS from the public market
7. Item APPEARS in user's owned items
```

### 💵 Selling an Item

```
1. User clicks "Sell" on owned item
2. Modal confirms the sale
3. Form submits to POST /market (sell action)
4. Server:
      item.owner = None
      current_user.budget += item.price
      db.session.commit()
5. Item REAPPEARS on public market
6. Budget INCREASES instantly
```

---

## 🚀 Installation

### 1. Clone the repo

```bash
git clone https://github.com/khaledelsayed2003/tradehub-marketplace.git
cd tradehub
```

### 2. Create & activate virtual environment

```bash
# Create
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp config/.env.example config/.env
# Then edit config/.env and add your SECRET_KEY
```

### 5. Run the app

```bash
python run.py
```

> 🌐 App will run at: `http://127.0.0.1:5000`

---

## 🧪 Try It Out

| Action                 | What Happens                               |
| ---------------------- | ------------------------------------------ |
| Register a new account | Get $1,000 starting budget                 |
| Buy an item            | It's removed from market, budget drops     |
| Check market           | That item is GONE for everyone             |
| Sell it back           | Item returns to market, you get money back |
| Delete account         | Everything wiped, session ends             |

---

## 🔮 Roadmap

- [ ] 🖼 Item images
- [ ] 📜 Transaction history
- [ ] 🔍 Search & filter market
- [ ] 📄 Pagination for large inventories
- [ ] 👤 User profile pages
- [ ] 🛡 Admin dashboard
- [ ] 🌙 Dark / Light theme toggle
- [ ] 💳 Stripe payment integration
- [ ] 🔗 REST API

---

## 🧑‍💻 Author

<div align="center">

**Khaled Elsayed**

[![GitHub](https://img.shields.io/badge/GitHub-khaledelsayed2003-181717?style=for-the-badge&logo=github)](https://github.com/khaledelsayed2003)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-khaledelsayed2003-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/khaledelsayed2003/)

</div>

---

<div align="center">

### ⭐ If you found this project useful, give it a star!

_It helps others discover the project and motivates continued development._

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,100:00D4FF&height=120&section=footer" width="100%"/>

</div>
