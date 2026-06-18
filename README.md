# 🚀 Advanced MTProto Proxy Scraper & Manager

[![Update MTProto Proxies](https://github.com/darkvibez456/mtproto-enhanced/actions/workflows/update_proxies.yml/badge.svg)](https://github.com/darkvibez456/mtproto-enhanced/actions/workflows/update_proxies.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/darkvibez456/mtproto-enhanced?style=social)](https://github.com/darkvibez456/mtproto-enhanced/stargazers)

This project is a highly efficient, automated solution for gathering, verifying, and distributing **Telegram MTProto Proxies**. It goes beyond simple list-hosting by providing a robust automation engine that ensures you always have access to fast and working proxies.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| **Multi-Source Scraping** | Automatically fetches proxies from multiple high-quality GitHub repositories and public sources. |
| **Automated Verification** | A built-in Python engine filters out dead links and verifies proxy parameters. |
| **GitHub Actions Integration** | The list is updated automatically every 12 hours without any manual intervention. |
| **Developer Friendly** | Provides both a raw text list (`proxies.txt`) and a structured JSON format (`proxies.json`) for API integration. |
| **One-Click Connect** | All proxies are formatted as standard `tg://proxy` links for instant connection. |

---

## 🛠️ How to Use

### 1. Direct Connection
Simply open the [`proxies.txt`](proxies.txt) file, copy any link, and paste it into your browser or directly into Telegram.

### 2. For Developers (API)
You can use the `proxies.json` file as a static API endpoint for your own applications:
```json
[
    {
        "url": "tg://proxy?server=...",
        "server": "...",
        "port": "...",
        "secret": "...",
        "verified": true,
        "latency": "N/A"
    }
]
```

---

## ⚙️ Setup & Customization

If you want to host your own version of this scraper:

1.  **Fork this repository.**
2.  **Enable GitHub Actions:** Go to the `Actions` tab and enable workflows.
3.  **Customize Sources:** Edit `scripts/scraper.py` to add or remove proxy sources.

### Local Development
To run the scraper locally:
```bash
# Clone the repo
git clone https://github.com/darkvibez456/mtproto-enhanced.git
cd mtproto-enhanced

# Install dependencies
pip install requests

# Run the scraper
python scripts/scraper.py
```

---

## 📊 Project Structure

```text
.
├── .github/workflows/
│   └── update_proxies.yml    # Automation engine
├── scripts/
│   └── scraper.py            # Core scraping logic
├── proxies.txt           # Clean list of proxies
├── proxies.json              # Structured data for apps
└── README.md                 # Documentation
```

---

## 🤝 Contributing
Contributions are welcome! If you have a reliable proxy source or want to improve the verification logic, feel free to open a Pull Request.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
**Created with ❤️ by [darkvibez456](https://github.com/darkvibez456)**
