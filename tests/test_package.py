import imdir


def test_package():
    im_dir = imdir.image_dir('./')
    assert im_dir.file_list == []
