from common.utility import *

def test_download_and_extract_zip():
    res = download_zipfile("https://ganguoroshi.jp/client_info/KAWADAONLINE/view/userweb/images/KOLList.zip?timestamp=1625216694000", "test.zip")
    assert res

    assert extract_zipfile("test.zip","temp_zip")