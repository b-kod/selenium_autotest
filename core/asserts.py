class Asserts:
    @staticmethod
    def assert_equals(val1, val2, error_massage: str = ""):
        assert val1 == val2, f"Failed assertion that {val1} is equals {val2}. {error_massage}"

    @staticmethod
    def assert_code_status(response, expected_code: int, error_massage: str = ""):
        assert response.status_code == expected_code, \
            f'Expected status code {expected_code}, but got {response.status_code}. {error_massage}'

    @staticmethod
    def assert_elements_amount(els: list, expected_amount: int, error_massage: str = ""):
        assert len(els) == expected_amount or len(els) > expected_amount, f"Did not get expected amount of elements. Expected {expected_amount}, got {len(els)}, {error_massage}"

    @staticmethod
    def assert_element_has_text(element, expected_text: str, error_massage: str = ""):
        assert element.text == expected_text, f"Expect to get {expected_text}. but got {element.text}, {error_massage}"

    @staticmethod
    def assert_attribute_value(element, expected_text: str, error_massage: str = ""):
        assert element == expected_text, f"Expect to get {expected_text}. but got {element}, {error_massage}"

    @staticmethod
    def assert_element_has_one_of_texts(element, expected_texts: list, error_massage: str = ""):
        found = False
        for expected_text in expected_texts:
            if expected_text in element:
                found = True
                break

        assert found, f"None of the following texts '{', '.join(expected_texts)}' are found in element. Element has text: {element}, {error_massage}"