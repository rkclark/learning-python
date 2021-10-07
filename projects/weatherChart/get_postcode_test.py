from get_postcode import get_postcode

valid_postcode = "SE6 0GF"
invalid_postcode = "NOT_A_POSTCODE"


class Test_GetPostcode:
  def test_requests_user_to_input_postcode(_, mocker):
    mocker.patch("builtins.input", return_value=valid_postcode)
    get_postcode()

    input.assert_called_once_with("Enter postcode:\n")

  def test_returns_postcode_when_valid(_, mocker):
    mocker.patch("builtins.input", return_value=valid_postcode)
    result = get_postcode()

    assert result == valid_postcode

  def test_requests_user_to_reinput_postcode_until_valid(_, mocker):
    mocker.patch(
      "builtins.input", side_effect=[invalid_postcode, invalid_postcode, valid_postcode]
    )
    result = get_postcode()

    assert input.call_count == 3
    for call in input.call_args_list:
      assert call == mocker.call("Enter postcode:\n")

    assert result == valid_postcode
