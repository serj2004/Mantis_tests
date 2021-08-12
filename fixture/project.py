import random
from random import choice
from string import ascii_uppercase

from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def add_new_project(self, project_name):
        wd = self.app.wd
        self.open_manage_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project_name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'%s')]" % name).click()
        wd.find_element_by_xpath("//div[@class='border center']//form[@method='post']//input[@type='submit']").click()
        wd.find_element_by_xpath("//div[@align='center']//form[@method='post']//input[@type='submit']").click()

    def open_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'Manage')]").click()
        wd.find_element_by_xpath("//a[contains(text(),'Manage Projects')]").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_page()
        lst = []
        for row in wd.find_elements_by_xpath("//body/table[@class='width100']/tbody/tr")[3:]:
            cells = row.find_elements_by_tag_name("td")
            id = cells[0].find_element_by_tag_name("a").get_attribute("href").split('=')[-1]
            name = cells[0].text
            lst.append(Project(id=id, name=name))
        return list(lst)

    def name_generator(self):
        name = ''.join(choice(ascii_uppercase) for i in range(random.randrange(15)))
        return str(name)
