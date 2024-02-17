from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# ヘッドレスモードの設定
options = Options()
options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


def wait_for_page_load(driver, timeout=10):
    try:
        # document.readyStateがcompleteになるのを待つ
        page_loaded = WebDriverWait(driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState;") == "complete"
        )
    except TimeoutException:
        print("Timed out waiting for page to load.")
        return False
    return True

def get_last_page(url):
    """最終ページ番号を取得する"""
    driver.get(url)
    if wait_for_page_load(driver):
        try:
            script = "return document.querySelector('.m-last-page.m-page-link').textContent;"
            last_page_number = driver.execute_script(script)
            return int(last_page_number)
        except ValueError:
            print("Could not convert page number to integer.")
            return None
    else:
        return None


def get_li_elements_from_page(page_number):
    """指定ページからdata-card-id属性を持つ<li>要素を取得する"""
    specific_url = f'https://aws.amazon.com/jp/free/?awsm.page-all-free-tier={page_number}'
    driver.get(specific_url)
    return driver.find_elements(By.CSS_SELECTOR, 'li[data-card-id]')


def get_text_or_na(element, selector, by=By.CLASS_NAME):
    """指定されたセレクタに対するテキストを取得、もしくは'N/A'を返す"""
    try:
        return element.find_element(by, selector).text
    except Exception:
        return 'N/A'


def extract_li_content(li_elements, file_path):
    """<li>要素から指定されたクラスごとにテキストを抽出し、ファイルに保存する"""
    with open(file_path, 'a', encoding='utf-8') as file:
        for li in li_elements:
            content = {
                'Expertise': get_text_or_na(li, 'm-expertise'),
                'Service': get_text_or_na(li, '.m-headline.m-truncate', By.CSS_SELECTOR),
                'Limit': f"{get_text_or_na(li, 'm-headline-callout')} {get_text_or_na(li, '.m-subheadline.m-truncate', By.CSS_SELECTOR)}",
                'Description': get_text_or_na(li, 'm-desc'),
                'Description Extra': get_text_or_na(li, 'm-desc-extra')
            }
            for key, value in content.items():
                print(f"{key}: {value}\n")
                file.write(f"{key}: {value}\n")
            file.write("--------------------------------------------------\n")


def get_all_free_items(last_page_number, url):
    """すべてのページをループして、<li>要素の内容を取得し、ファイルに保存する"""
    file_path = 'aws_services.txt'
    for page in range(1, last_page_number + 1):
        li_elements = get_li_elements_from_page(page)
        extract_li_content(li_elements, file_path)


# メイン処理
if __name__ == '__main__':
    try:
        url = 'https://aws.amazon.com/jp/free/?awsm.page-all-free-tier=1'
        last_page = get_last_page(url)
        get_all_free_items(last_page, url)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
