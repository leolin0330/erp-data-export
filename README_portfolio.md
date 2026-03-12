# ERP Data Export Automation

### Python + Selenium ERP 自動化資料匯出工具

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![Automation](https://img.shields.io/badge/ERP-Process%20Automation-orange)

------------------------------------------------------------------------

# 專案介紹

此專案為一套 **ERP 系統自動化工具**，使用 **Python + Selenium** 開發，\
用來自動登入公司 ERP 系統並批次匯出資料。

透過瀏覽器自動化技術，模擬使用者操作流程，自動完成：

-   ERP 系統登入
-   進入交易資料模組
-   勾選資料
-   匯出 Excel
-   自動下載檔案
-   下載完成檢測
-   檔案重新命名
-   切換工廠資料

此工具可將原本 **10\~20 分鐘的人工操作縮短至約 1 分鐘完成**。

------------------------------------------------------------------------

# 系統架構

    Python Script
          │
          │ Selenium
          ▼
    Browser Automation
          │
          ▼
    ERP Web System
          │
          ▼
    Download Excel
          │
          ▼
    File Processing
          │
          ▼
    Local Storage

------------------------------------------------------------------------

# 自動化流程

    啟動瀏覽器
         ↓
    登入 ERP 系統
         ↓
    進入交易資料模組
         ↓
    設定每頁資料筆數
         ↓
    勾選全部資料
         ↓
    匯出 Excel
         ↓
    監控下載完成
         ↓
    重新命名檔案
         ↓
    切換工廠
         ↓
    再次下載

------------------------------------------------------------------------

# 專案功能

## 1. 自動登入 ERP

``` python
driver.get("http://xxx.xxx.xxx")
driver.find_element(By.ID,"TxtUid").send_keys("帳號")
driver.find_element(By.ID,"TxtPwd").send_keys("密碼")
driver.find_element(By.ID,"BtnLogOn").click()
```

------------------------------------------------------------------------

## 2. 自動匯出 Excel

透過 Selenium 自動點擊 ERP 匯出按鈕下載 Excel。

------------------------------------------------------------------------

## 3. 下載完成偵測

``` python
while time.time() - start_time < timeout:
    if not glob.glob(os.path.join(download_path, "*.crdownload")):
        return True
```

------------------------------------------------------------------------

## 4. 檔案自動重新命名

    T收貨.xls
    U收貨.xls

------------------------------------------------------------------------

## 5. 多工廠資料下載

``` python
select_element = Select(driver.find_element(By.ID,"MainContent_Cbo1"))
select_element.select_by_value("99687850")
```

------------------------------------------------------------------------

# 技術亮點

✔ Selenium 瀏覽器自動化\
✔ ERP 系統流程自動化\
✔ 檔案下載完成偵測機制\
✔ 自動檔案管理\
✔ 支援多工廠資料匯出

------------------------------------------------------------------------

# 技術架構

  技術             用途
  ---------------- --------------
  Python           自動化程式
  Selenium         瀏覽器自動化
  Edge WebDriver   控制瀏覽器
  WebDriverWait    動態等待
  glob             下載監控
  os               檔案處理

------------------------------------------------------------------------

# 專案結構

    ERP-Automation
    │
    ├── 鼎創Z交貨轉出.py
    ├── 鼎創收貨轉出.py
    └── README.md

------------------------------------------------------------------------

# 執行環境

Python

    Python 3.10+

安裝套件

    pip install selenium
    pip install webdriver-manager

------------------------------------------------------------------------

# 執行方式

    python 鼎創收貨轉出.py

或

    python 鼎創Z交貨轉出.py

------------------------------------------------------------------------

# 使用情境

本專案適用於：

-   ERP 系統自動化
-   報表自動匯出
-   Excel 批次下載
-   重複性工作自動化

------------------------------------------------------------------------

# 未來優化

-   自動排程執行
-   Log 紀錄系統
-   Email 自動寄送報表
-   GUI 版本
-   Docker 自動部署

------------------------------------------------------------------------

# 作者

Timmy

ERP System Engineer\
Python Automation Developer
