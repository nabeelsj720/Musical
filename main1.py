from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

class Musical_auto:

    def __init__(self, data):
        """Parameter initialization"""
        self.url = data['url']
        self.instrument_category = data['Instrument Category']
        self.instrument_type = data['Instrument Type']
        self.value = data['Value']
        self.cover = data['Cover']
        self.title = data['Title']
        self.surname = data['Surname']
        self.email_address = data['Email address']
        self.telephone_number = data['Telephone number']
        self.cover_start_day = data['Cover start day']
        self.cover_start_month = data['Cover start month']
        self.cover_start_year = data['Cover start year']
        self.plpa = data['PLPA']
        self.forename = data['Forename']
        self.day_of_birth = data['Day of Birth']
        self.month_of_birth = data['Month of Birth']
        self.year_of_birth = data['Year of Birth']
        self.postcode = data['Postcode']
        self.make_model = data['Make and model']
        self.serial_number = data['Serial number']
        self.instrument_address_provided = data['Instrument kept in address provided']
        self.driver = webdriver.Chrome(data['driver_path'])

    def first_page(self):

        # go to the first page
        self.driver.get(self.url)

        # accept cokkies
        cokies = self.driver.find_element_by_xpath('//*[@id="center-tile-banner-popup"]/div[2]/div[2]/div[3]/div[1]/div/button')
        cokies.send_keys(Keys.RETURN)
        time.sleep(2)
        #instrument details
        instrument_category = self.driver.find_element_by_xpath('//*[@id="instForm:instrumentPanel:instrumentCatSubview:inst-cat"]')
        instrument_category.send_keys(self.instrument_category)
        time.sleep(4)
        instrument_type = self.driver.find_element_by_xpath('//*[@id="instForm:instrumentPanel:instrumentTypeSubview:inst-type"]')
        instrument_type.send_keys(self.instrument_type)
        time.sleep(2)
        value = self.driver.find_element_by_xpath('//*[@id="instForm:instrumentPanel:instrumentValueSubview:inst-val"]')
        value.clear()
        value.send_keys(self.value)
        cover = self.driver.find_element_by_xpath('//*[@id="instForm:instrumentPanel:typeCoverPanel:instrumentCoverSubview:type-of-cover1:' + self.cover + '"]').click()
        add_instrument=self.driver.find_element_by_xpath('//*[@id="instForm:instrumentPanel:addButton"]')
        add_instrument.send_keys(Keys.RETURN)
        time.sleep(2)
        title = self.driver.find_element_by_xpath('//*[@id="instForm:titleSelect:iqSOM"]')
        title.send_keys(self.title)
        time.sleep(1)
        surname = self.driver.find_element_by_xpath('//*[@id="instForm:surnameInput:iqIT"]')
        surname.send_keys(self.surname)
        time.sleep(1.5)
        email_address = self.driver.find_element_by_xpath('//*[@id="instForm:emailInput:iqIT"]')
        email_address.send_keys(self.email_address)
        time.sleep(1.5)
        telephone_number = self.driver.find_element_by_xpath('//*[@id="instForm:phoneNoInput:iqIT"]')
        telephone_number.send_keys(self.telephone_number)
        time.sleep(1.5)
        cover_start_day = self.driver.find_element_by_xpath('//*[@id="instForm:csdInput:iqSOMDay"]')
        cover_start_day.send_keys(self.cover_start_day)
        time.sleep(2)
        cover_start_month = self.driver.find_element_by_xpath('//*[@id="instForm:csdInput:iqSOMMonth"]')
        cover_start_month.send_keys(self.cover_start_month)
        time.sleep(2)
        cover_start_year = self.driver.find_element_by_xpath('//*[@id="instForm:csdInput:iqIT"]')
        cover_start_year.clear()
        cover_start_year.send_keys(self.cover_start_year)     
        time.sleep(2)
        submit1 = self.driver.find_element_by_xpath('//*[@id="instForm:amiForm_buttonProceed"]')
        submit1.send_keys(Keys.RETURN)
        
    def second_page(self):
        plpa = self.driver.find_element_by_xpath('//*[@id="instQuoteForm:accidentCoverSelect:radio"]/tbody/tr[' + self.plpa + ']/td/label/input').click()
        submit2 = self.driver.find_element_by_xpath('//*[@id="instQuoteForm:continueButton1"]')
        submit2.send_keys(Keys.RETURN)

    def third_page(self):
        forename = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:forename:iqIT"]')
        forename.send_keys(self.forename)
        day_of_birth = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:dateofbirth:iqSOMDay"]')
        day_of_birth.send_keys(self.day_of_birth)
        month_of_birth = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:dateofbirth:iqSOMMonth"]')
        month_of_birth.send_keys(self.month_of_birth)
        year_of_birth = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:dateofbirth:iqIT"]')
        year_of_birth.send_keys(self.year_of_birth)
        postcode = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:instrumentAddressSubview:selectedPostcode:iqIT"]')
        postcode.send_keys(self.postcode)
        find_postcode = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:instrumentAddressSubview:selectedPostcode:cmdLnkFindPanel0"]')
        find_postcode.send_keys(Keys.RETURN)
        time.sleep(5)
        address = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:instrumentAddressSubview:addressSelect:iqSOM"]')
        address.send_keys(Keys.RETURN)
        time.sleep(3)
        for i in range(8):
            #time.sleep(0.3)
            address.send_keys(Keys.DOWN)
        address.send_keys(Keys.RETURN)
        time.sleep(3)
        hear_about_us = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:hearAboutUs:iqSOM"]')
        hear_about_us.send_keys(Keys.RETURN)
        #time.sleep(3)
        for j in range(4):
            hear_about_us.send_keys(Keys.DOWN)
            #time.sleep(1.5)
        hear_about_us.send_keys(Keys.RETURN)
        make_model = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:instrumentPanel:instlst:0:descriptionTxt"]')
        make_model.send_keys(self.make_model)
        serial_number = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:instrumentPanel:instlst:0:serialNoTxt"]')
        serial_number.send_keys(self.serial_number)
        instrument_address_provided = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:keptAtAddress:radio"]/tbody/tr/td[' + self.instrument_address_provided + ']/label/input').click()
        submit3 = self.driver.find_element_by_xpath('//*[@id="instAdditionalDetailsForm:amiForm_buttonProceed"]')
        submit3.send_keys(Keys.RETURN)

    def fourth_page(self):
        uw1 = self.driver.find_element_by_xpath('//*[@id="instSecurityQuestionsForm:isInGoodCondition:radio"]/tbody/tr/td[1]/label/input').click()
        time.sleep(1.5)
        uw2 = self.driver.find_element_by_xpath('//*[@id="instSecurityQuestionsForm:underwriterEverDeclined:radio1"]/tbody/tr/td[2]/label/input').click()
        time.sleep(1.5)
        uw3 = self.driver.find_element_by_xpath('//*[@id="instSecurityQuestionsForm:underwriterEverDeclined:radiob"]/tbody/tr/td[2]/label/input').click()
        time.sleep(1.5)
        uw4 = self.driver.find_element_by_xpath('//*[@id="instSecurityQuestionsForm:resideOutsideOfUK:radio"]/tbody/tr/td[2]/label/input').click()
        time.sleep(1.5)
        uw4 = self.driver.find_element_by_xpath('//*[@id="instSecurityQuestionsForm:convictedOffence:radio"]/tbody/tr/td[2]/label/input').click()
        time.sleep(1.5)
        confirm1 = self.driver.find_element_by_xpath('//*[@id="instSecurityQuestionsForm:interestChkBox:uwConfirm"]').click()
        time.sleep(1.5)
        confirm2 = self.driver.find_element_by_xpath('//*[@id="instSecurityQuestionsForm:ackChkBox:uwConfirm"]').click()
        time.sleep(1.5)
        submit4 = self.driver.find_element_by_xpath('//*[@id="instSecurityQuestionsForm:amiForm_buttonProceed"]')
        submit4.send_keys(Keys.RETURN)

    def fifth_page(self):
        pass
               
    def close_session(self):
        """This function closes the actual session"""
        
        print('End of the session, see you later, quote number:')
        self.driver.close()

    def apply(self):
        self.driver.maximize_window()
        self.first_page()
        time.sleep(2)
        self.second_page()
        time.sleep(2)
        self.third_page()
        time.sleep(2)
        self.fourth_page()
        time.sleep(2)
        self.fifth_page()
        #self.close_session()


if __name__ == '__main__':

    with open('config1.json') as config_file:
        data = json.load(config_file)

    bot = Musical_auto(data)
    bot.apply()
