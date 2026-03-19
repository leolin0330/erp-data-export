from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time, os, glob

# === 下載資料夾設定 ===
download_dir = r"C:\Users\timmy\PycharmProjects\PythonProject\食品雲\上傳非追"
os.makedirs(download_dir, exist_ok=True)

# === EdgeDriver 設定 ===
edge_options = EdgeOptions()

prefs = {
    "download.default_directory": download_dir,
    "profile.default_content_settings.popups": 0,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True,
    "safebrowsing.disable_download_protection": True
}
edge_options.add_experimental_option("prefs", prefs)
service = Service(r"D:\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_options)

# 登入
driver.get("http://192.168.2.11/cfrme2020/DS00010/DS00010MF.aspx?caller=default")
driver.find_element(By.ID, "TxtUid").send_keys("07498")
driver.find_element(By.ID, "TxtPwd").send_keys("07498")
driver.find_element(By.ID, "BtnLogOn").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dropdown-toggle")))

# 等待下載完成函數
def wait_for_download_complete(download_path, timeout=30):
    print("等待檔案下載...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        if not glob.glob(os.path.join(download_path, "*.crdownload")):
            return True
            
        # 每秒檢查一次
        time.sleep(1)

    # 超過 timeout
    return False

# 匯出流程函數
def export_data():
    input_box = driver.find_element(By.ID, "MainContent_TxtPCount")
    input_box.clear()

    # 設定每頁顯示 500 筆
    input_box.send_keys("500")
    driver.find_element(By.ID, "MainContent_BtnToPage").click()

    # 勾選全選 checkbox
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Chka170All")))
        checkbox = driver.find_element(By.ID, "Chka170All")
        if not checkbox.is_selected():
            checkbox.click()
    except Exception as e:
        print(f"❌ 勾選 checkbox 發生錯誤：{e}")

    # 等待資料載入
    time.sleep(7)

    # 下載交貨
    driver.find_element(By.ID, "MainContent_Btn05").click()
    if wait_for_download_complete(download_dir):
        print("✅ 檔案下載完成！")
    else:
        print("⚠️ 檔案下載超時或遭封鎖，請檢查 Edge 設定。")

    # 下載退貨
    driver.find_element(By.ID, "MainContent_Btn04").click()
    if wait_for_download_complete(download_dir):
        print("✅ 檔案下載完成！")
    else:
        print("⚠️ 檔案下載超時或遭封鎖，請檢查 Edge 設定。")



# 第一次下載（預設廠）
driver.find_element(By.XPATH, "//a[@class='dropdown-toggle' and contains(text(), '交易資料模組')]").click()
driver.find_element(By.XPATH, "//a[contains(text(), '交貨資料(輸入)')]").click()
time.sleep(2)
export_data()
time.sleep(50)


# 結束
input("🔵 按 Enter 結束並關閉")
driver.quit()
