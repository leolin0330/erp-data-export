
# ERP Data Export Automation
### Python + Selenium ERP 自動化資料匯出工具

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![Automation](https://img.shields.io/badge/ERP-Process%20Automation-orange)

---

## 專案介紹

此專案使用 **Python + Selenium** 建立 ERP 系統自動化工具，
可自動登入 ERP、匯出 Excel、下載資料並重新命名檔案。

主要目標是將原本需要人工操作 10~20 分鐘的流程，
縮短為 **約 1 分鐘自動完成**。

---

## 系統架構

![Architecture](architecture.png)

---

## 自動化流程

![Workflow](workflow.png)

---

## 技術亮點

- Selenium 瀏覽器自動化
- ERP 系統流程自動化
- Excel 下載監控機制
- 自動檔案命名與管理
- 支援多工廠資料下載

---

## 技術架構

| 技術 | 用途 |
|-----|-----|
| Python | 自動化程式 |
| Selenium | 瀏覽器自動化 |
| Edge WebDriver | 控制瀏覽器 |
| WebDriverWait | 動態等待 |
| glob | 下載監控 |
| os | 檔案處理 |

---

## 專案結構

ERP-Automation
│
├── README.md
├── architecture.png
├── workflow.png
├── demo.png
├── 鼎創Z交貨轉出.py
└── 鼎創收貨轉出.py

---

## 執行方式

```
pip install selenium webdriver-manager
python 鼎創收貨轉出.py
```

---

## 作者

Timmy  
ERP System Engineer  
Python Automation Developer
