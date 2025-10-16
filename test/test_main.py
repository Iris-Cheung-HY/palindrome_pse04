from main.main import check_palindrome

def test_nominal_trus():
    # ^rename with meaningful test name
    # and complete test implementation below
    # arrange
    word = "noon"

    # act
    result = check_palindrome(word)
    # assert
    assert result == True

def test_with_space():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    word = "hello world"

    # act
    result = check_palindrome(word)
    # assert
    assert result == False

def test_with_capital():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    word = "Kayak"

    # act
    result = check_palindrome(word)
    # assert
    assert result == True


def test_with_punctation():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    word = "noon!"

    # act
    result = check_palindrome(word)

    # assert
    assert result == False



def test_with_front_back_punctation():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    word = "!noon!"

    # act
    result = check_palindrome(word)

    # assert
    assert result == True



def test_with_number_punctation():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    word = "4noon!"

    # act
    result = check_palindrome(word)

    # assert
    assert result == False


def test_with_number():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    word = "4noon4"

    # act
    result = check_palindrome(word)

    # assert
    assert result == True


def test_with_space_and_cap():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    word = "hello world I am iris"

    # act
    result = check_palindrome(word)

    # assert
    assert result == False
