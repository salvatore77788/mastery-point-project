import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_champion_points(table_row_str, debug=False):

    """
        Gets Champion Name And Points From Table Row Web Element.

    Args:
        table_row_str: The Table Row That Contains User Specific Champion Mastery Points.
        debug: (bool) If The Program Should Be Executed In Debug Mode.

    Returns:
        The Champion Name And Mastery Points On Said Champion Respectively.

    Alternate Returns:
        Returns None, None If The Table Row Provided Is Invalid Or Does Not Exist During Cleaning.
    """

    # Relies On Assumption That No Champion Has Numbers Or '/' In Their Name
    row_contains_date_champion_mastered = table_row_str.count(r"/") == 2
    row_contains_date_champion_not_mastered = table_row_str.count(r"/") == 3 and r'N/A' in table_row_str

    if row_contains_date_champion_mastered or row_contains_date_champion_not_mastered:
        # Rek'Sai 7 332,211 5/13/22, 10:58 PM Mastered N/A
        start_with_month_str = table_row_str[:table_row_str.index(r'/')][::-1]     # Rek'Sai 7 332,211 5

        if ' ' in start_with_month_str:

            month_size = 2 if start_with_month_str.index(' ') == 1 else 3
            str_left_of_date = table_row_str[:table_row_str.index(r'/')-month_size]  # Rek'Sai 7 332,211

            points_str = str_left_of_date[::-1]
            points_str = points_str[:points_str.index(" ")][::-1]  # 332,211

            if points_str:
                points_int = int(points_str.replace(',', '')) if  ',' in points_str else int(points_str)    # 332211

                # The First Index With A Nonzero Digit Is Always The Mastery Level Of The Champion
                temp = str_left_of_date + ''.join([str(i) for i in range(1,10)])    # Rek'Sai 7 332,211123456789
                mastery_level_index = min([temp.index(str(i)) for i in range(1, 10)])   # 7

                champion_str = str_left_of_date[:mastery_level_index-1] # Rek'Sai

                return (champion_str, points_int)

    return None, None


def get_mastery_point_dict(user, debug=False):

    options = Options()
    options.headless = False
    driver = webdriver.Chrome()

    start_url = f"https://championmastery.gg/summoner?summoner={user}&region=NA"
    driver.get(start_url)
    driver.implicitly_wait(10)

    results = driver.find_elements_by_xpath(r'//tr')
    time.sleep(2)
    results_dict = dict()

    for result in results:
        result = result.text
        print(result)
        champion_str, points_int = get_champion_points(result)

        if champion_str and points_int:
            results_dict[champion_str] = points_int

    driver.close()

    return results_dict
