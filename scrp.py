# @proh_gram_er

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('chromedriver')
driver.get('http://www.transwale.com/frm_ShowMemberByAgencyName.aspx')

count = len(WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located(
    (By.XPATH, "//*[@id='ctl00_ddl_location']/option"))))

# 51

for location in range(73, count + 1):
    df = pd.DataFrame(
        columns=[
            'Company Name', 'Landline No', 'Mobile Number', 'Contact Person', 'Mail', 'Website', 'Daily Servie'
        ])
    df_idx = 0

    location_name = driver.find_element(
        By.XPATH, f"//*[@id='ctl00_ddl_location']/option[{location + 1}]").text
    driver.find_element(By.XPATH,
                        f"//*[@id='ctl00_ddl_location']/option[{location + 1}]").click()
    driver.find_element(By.XPATH,
                        "//*[@id='ctl00_btn_Search']").click()

    WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_lbl_record_count']")))

    # total_records = int((int(driver.find_element(
    #     By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_lbl_record_count']").text))/2)

    total_records = int(driver.find_element(
        By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_lbl_record_count']").text)

    print(total_records)

    if total_records >= 1:
        for outer_idx in range(1, int(total_records/2) + 1):
            for inner_idx in range(1, 3):

                company_name = driver.find_element(
                    By.XPATH, f"// *[@id='ctl00_ContentPlaceHolder1_DataList1']/tbody/tr[{outer_idx}]/td[{inner_idx}]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/strong"
                ).text
                landline_no = driver.find_element(
                    By.XPATH, f"//*[@id = 'ctl00_ContentPlaceHolder1_DataList1']/tbody/tr[{outer_idx}]/td[{inner_idx}]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]"
                ).text
                mobile_number = driver.find_element(
                    By.XPATH, f"//*[@id='ctl00_ContentPlaceHolder1_DataList1']/tbody/tr[{outer_idx}]/td[{inner_idx}]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]"
                ).text
                contact_person = driver.find_element(
                    By.XPATH, f"//*[@id='ctl00_ContentPlaceHolder1_DataList1']/tbody/tr[{outer_idx}]/td[{inner_idx}]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td[2]"
                ).text
                mail = driver.find_element(
                    By.XPATH, f"//*[@id='ctl00_ContentPlaceHolder1_DataList1']/tbody/tr[{outer_idx}]/td[{inner_idx}]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[7]/td[2]"
                ).text
                website = driver.find_element(
                    By.XPATH, f"//*[@id='ctl00_ContentPlaceHolder1_DataList1']/tbody/tr[{outer_idx}]/td[{inner_idx}]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[8]/td[2]"
                ).text
                daily_servie = driver.find_element(
                    By.XPATH, f"//*[@id='ctl00_ContentPlaceHolder1_DataList1']/tbody/tr[{outer_idx}]/td[{inner_idx}]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[9]/td"
                ).text

                df.loc[df_idx] = [company_name] + [landline_no] + [mobile_number] + \
                    [contact_person] + [mail] + [website] + [daily_servie]
                df_idx += 1

    df.to_csv(f'{location_name}.csv')
    print(f'{location}> {location_name} is done!')

print('Scraping is done!')
driver.quit()
