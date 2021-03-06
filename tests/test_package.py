import imdir


def test_package():
    """
    tests that we can import package
    """
    im_dir = imdir.image_dir("./")
    assert im_dir.file_list == []


def test_files():
    """
    tests if file list is correct
    """
    im_dir = imdir.image_dir("./tests/images/")
    assert im_dir.file_list.sort() == ['./tests/images/2.jpg',
                                       './tests/images/1.jpg',
                                       './tests/images/5.jpg',
                                       './tests/images/4.jpg',
                                       './tests/images/6.jpg',
                                       './tests/images/3.jpg'].sort()


def test_corrupt_files():
    """
    tests if corrupt file list is correct
    """
    im_dir = imdir.image_dir("./tests/images/")
    assert im_dir.corrupt_file_list == ['./tests/images/text_file.jpg']


def test_samples():
    """
    tests if file list is correct
    """
    im_dir = imdir.image_dir("./tests/images/", sample_size=2)
    assert len(im_dir.file_list) + len(im_dir.corrupt_file_list) == 2


def test_width():
    """
    tests if width list is correct
    """
    im_dir = imdir.image_dir("./tests/images/")
    assert im_dir.width_list.sort() == [925, 925, 925, 925, 925, 925].sort()


def test_height():
    """
    tests if height list is correct
    """
    im_dir = imdir.image_dir("./tests/images/")
    assert im_dir.height_list.sort() == [693, 617, 693, 1387, 617, 617].sort()


def test_recursive_files():
    """
    tests if file list is correct
    """
    im_dir = imdir.image_dir("./tests/images/", recursive=True)
    im_dir.file_list.sort() == ['./tests/images/2.jpg',
                                './tests/images/1.jpg',
                                './tests/images/5.jpg',
                                './tests/images/4.jpg',
                                './tests/images/6.jpg',
                                './tests/images/3.jpg',
                                './tests/images/recursive/2.jpg'].sort()
