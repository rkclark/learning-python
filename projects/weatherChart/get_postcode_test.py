from get_postcode import get_postcode

valid_postcode = "SE6 0GF"


class Test_GetPostcode:
  def test_requests_user_to_input_postcode(_, mocker):
    mocker.patch("builtins.input", return_value=valid_postcode)
    result = get_postcode()

    input.assert_called_once_with("Enter postcode:\n")
    assert result == valid_postcode
