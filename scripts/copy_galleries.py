import os
import tempfile

from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


# TODO have separate resize and upload scripts


input_dir = "/Users/jessamyn/Google Drive/roxanne/Website Photos/50 Ramsay House/19 Basement"
max_dimension = 1920

from_admin_url = "http://127.0.0.1:8000/django-admin"
# admin_username = 'admin'

to_admin_url = "https://roxy-the-renovator.herokuapp.com/django-admin"
admin_username = 'geekchick77+admin@gmail.com'

timeout = 3000
wait_increment = 100


def parse_exif_date(exif_data):
    exif_datetime = exif_data.get(306)
    if not exif_datetime:
        return None, None
    exif_date, exif_time = exif_datetime.split(' ')
    formatted_date = exif_date.replace(':', '-')
    return formatted_date, exif_time


def wait_for_page_load(driver, text):
    loaded = False
    waited = 0
    while not loaded:
        if waited > timeout:
            break
        if text in driver.page_source:
            loaded = True
        waited += wait_increment
    return loaded


def fill_form(driver, fields):
    input_field = None
    for field_name in fields:
        input_field = driver.find_element_by_name(field_name)
        input_field.clear()
        input_field.send_keys(fields[field_name])
    return input_field


def delete_all(driver):
    try:
        select_all = driver.find_element_by_id("action-toggle")
    except NoSuchElementException:
        return False
    select_all.click()
    select = Select(driver.find_element_by_name('action'))
    select.select_by_value('delete_selected')
    driver.find_element_by_name('index').submit()
    # Confirm deletion
    wait_for_page_load(driver, "Yes, I'm sure")
    driver.find_element_by_tag_name('form').submit()
    wait_for_page_load(driver, "Successfully deleted")
    return True


def login(driver, admin_url):
    driver.get("%s/login/" % admin_url)
    fields = {
        'username': admin_username,
        'password': os.environ.get('DJANGO_ADMIN_PASSWORD')
    }
    last_field = fill_form(driver, fields)
    last_field.submit()


def create_gallery(driver, gallery_name, gallery_exif, photo_names):
    driver.get("%s/photologue/gallery/add/" % to_admin_url)
    fields = {
        'title': gallery_name,
        'description': gallery_name,
    }
    if gallery_exif:
        gallery_date, gallery_time = parse_exif_date(gallery_exif)
        if gallery_date:
            fields['date_added_0'] = gallery_date
            fields['date_added_1'] = gallery_time

    last_field = fill_form(driver, fields)
    for photo_name in photo_names:
        try:
            label = driver.find_element_by_xpath('//*/text()[normalize-space(.)="%s"]/parent::*' %
                                                 photo_name)
            label.find_element_by_tag_name('input').click()
        except NoSuchElementException:
            print("Unable to find photo \"%s\" in gallery \"%s\"" % (photo_name, gallery_name))

    last_field.submit()
    wait_for_page_load(driver, "added successfully")


def create_photo(driver, photo_file_name, image_exif, img):
    driver.get("%s/photologue/photo/add/" % to_admin_url)
    photo_name, ext = os.path.splitext(photo_file_name)
    fields = {
        'title': photo_name,
        'caption': photo_name,
    }
    if image_exif:
        photo_date, photo_time = parse_exif_date(image_exif)
        if photo_date:
            fields['date_added_0'] = photo_date
            fields['date_added_1'] = photo_time
    file_input = driver.find_element_by_xpath("//input[@type='file']")
    _, temp_path = tempfile.mkstemp(suffix=ext)
    img.save(temp_path)
    file_input.send_keys(temp_path)
    last_field = fill_form(driver, fields)
    last_field.submit()
    wait_for_page_load(driver, "added successfully")
    return photo_name


def main():
    driver = webdriver.Firefox()
    login(driver, from_admin_url)

    to_driver = webdriver.Firefox()
    login(to_driver, to_admin_url)

    # # Delete existing galleries
    # driver.get("%s/photologue/gallery/?all=" % admin_url)
    # delete_all(driver)
    #
    # # Delete existing photos
    # driver.get("%s/photologue/photo/?all=" % admin_url)
    # delete_all(driver)

    for root, dirs, files in os.walk(input_dir):
        directory_name = None
        gallery_exif = None
        photo_names = []
        for file in files:
            try:
                with open(str(os.path.join(root, file)), 'rb') as f:
                    img = Image.open(f)
                    directory_name = os.path.split(root)[-1]
                    image_exif = img._getexif()
                    if not gallery_exif:
                        gallery_exif = image_exif
                    ratio = 1.0 * img.width / max_dimension
                    img = img.resize((max_dimension, int(round(img.height/ratio))), Image.ANTIALIAS)
                    photo_name = create_photo(driver, file, image_exif, img)
                    img.close()
                    photo_names.append(photo_name)
                    del img
            except (IOError, OSError):
                continue

        if directory_name and gallery_exif:
            create_gallery(driver, directory_name, gallery_exif, photo_names)

    driver.close()


if __name__ == "__main__":
    main()


# pg_dump roxy-the-renovator --data-only --table=photologue_gallery
#
#
#  \o (output to file) option that you can use with arbitrary SQL query. I'm suggesting using \a (switch to unaligned) and \t (show only tuples)
