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
edge_options.use_chromium = True
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

# 等待下載完成並重新命名
def wait_for_download_complete(download_path, timeout=30, new_filename=None):
    print("⏳ 等待檔案下載...")

    before_files = set(glob.glob(os.path.join(download_path, "*.xls")) + glob.glob(os.path.join(download_path, "*.xlsx")))
    start_time = time.time()

    while time.time() - start_time < timeout:
        if not glob.glob(os.path.join(download_path, "*.crdownload")):
            after_files = set(glob.glob(os.path.join(download_path, "*.xls")) + glob.glob(os.path.join(download_path, "*.xlsx")))
            new_files = list(after_files - before_files)
            if new_files:
                latest = max(new_files, key=os.path.getctime)
                basename = os.path.basename(latest)
                print(f"✅ 檔案下載完成：{basename}")
                if new_filename:
                    new_path = os.path.join(download_path, new_filename)
                    os.rename(latest, new_path)
                    print(f"✏️ 已重新命名為：{new_filename}")
                return True
        time.sleep(1)
    print("⚠️ 下載超時或未成功。")
    return False

# 勾選 checkbox
def check_checkbox(checkbox_id):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, checkbox_id)))
        for _ in range(3):
            try:
                checkbox = driver.find_element(By.ID, checkbox_id)
                if not checkbox.is_selected():
                    checkbox.click()
                break
            except Exception:
                time.sleep(1)
    except Exception as e:
        print(f"❌ 勾選 checkbox 發生錯誤：{e}")

# 匯出資料流程
def export_data(rename_to=None):
    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "MainContent_TxtPCount"))
    )
    input_box.clear()
    input_box.send_keys("5000")
    driver.find_element(By.ID, "MainContent_BtnToPage").click()

    check_checkbox("Chka90All")
    time.sleep(7)
    driver.find_element(By.ID, "MainContent_Btn06").click()

    if wait_for_download_complete(download_dir, timeout=60, new_filename=rename_to):
        print("✅ 檔案已成功下載並命名。")
    else:
        print("⚠️ 檔案下載失敗")

# 切換工廠
def switch_factory(value, factory_name):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "MainContent_Cbo1")))
        select_element = Select(driver.find_element(By.ID, "MainContent_Cbo1"))
        select_element.select_by_value(value)
        print(f"✅ 成功切換工廠至：{value}_{factory_name}")
        time.sleep(2)
    except Exception as e:
        print(f"❌ 切換工廠失敗：{e}")

# 點選模組 & 功能進入頁面
driver.find_element(By.XPATH, "//a[@class='dropdown-toggle' and contains(text(), '交易資料模組')]").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '收貨資料')]"))).click()
time.sleep(2)

# 第一次下載（預設廠）
export_data("T收貨.xls")

# 第二次下載（切換為 99687850_觀音二廠）
switch_factory("99687850", "觀音二廠")
export_data("U收貨.xls")

# 結束
input("🔵 按 Enter 結束並關閉")
driver.quit()
