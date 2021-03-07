"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.
"""


import introcs
import currency


def test_before_space():
    """Test procedure for before_space"""

    print("Testing before_space")

    # Add the test cases
    # Test case 1
    result = currency.before_space("1000 USD")
    introcs.assert_equals("1000", result)

    # Test case 2
    result = currency.before_space(" 2000 EUR")
    introcs.assert_equals("", result)

    # Test case 3
    result = currency.before_space("Millions 156000 USD")
    introcs.assert_equals("Millions", result)

    # Test case 4
    result = currency.before_space("2500EUR ")
    introcs.assert_equals("2500EUR", result)

    # Test case 5
    result = currency.before_space("1500AUD and  words ")
    introcs.assert_equals("1500AUD", result)

    # Test case 6
    result = currency.before_space("2454AZN  2600EUR")
    introcs.assert_equals("2454AZN", result)

    # Test case 7
    result = currency.before_space(" ")
    introcs.assert_equals("", result)


def test_after_space():
    """Test procedure for after_space"""

    print("Testing after_space")

    # Add the test cases
    # Test case 1
    result = currency.after_space("1000 USD")
    introcs.assert_equals("USD", result)

    # Test case 2
    result = currency.after_space(" 2000 EUR")
    introcs.assert_equals("2000 EUR", result)

    # Test case 3
    result = currency.after_space("Millions 156000 USD")
    introcs.assert_equals("156000 USD", result)

    # Test case 4
    result = currency.after_space("2500EUR ")
    introcs.assert_equals("", result)

    # Test case 5
    result = currency.after_space("1500AUD and  words ")
    introcs.assert_equals("and  words ", result)

    # Test case 6
    result = currency.after_space("2454AZN  2600EUR")
    introcs.assert_equals(" 2600EUR", result)

    # Test case 7
    result = currency.after_space(" ")
    introcs.assert_equals("", result)


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""

    print("Testing first_inside_quotes")

    # Add the test cases
    # Test case 1
    result = currency.first_inside_quotes('"2454AZN  2600EUR"')
    introcs.assert_equals("2454AZN  2600EUR", result)

    # Test case 2
    result = currency.first_inside_quotes('"2454AZN 2600EUR"')
    introcs.assert_equals("2454AZN 2600EUR", result)

    # Test case 3
    result = currency.first_inside_quotes('"2454"')
    introcs.assert_equals("2454", result)

    # Test case 4
    result = currency.first_inside_quotes('"2454AZN""2600EUR"')
    introcs.assert_equals("2454AZN", result)

    # Test case 5
    result = currency.first_inside_quotes('"2454USD" "2600EUR"')
    introcs.assert_equals("2454USD", result)

    # Test case 6
    result = currency.first_inside_quotes(
        '""2454USD"" "2600EUR" tacos po"tat"o')
    introcs.assert_equals("", result)

    # Test case 7
    result = currency.first_inside_quotes('" 2454USD "2600EUR" tacos po"tat"o')
    introcs.assert_equals(" 2454USD ", result)

    # Test case 8
    result = currency.first_inside_quotes('A"B"')
    introcs.assert_equals("B", result)


def test_get_src():
    """Test procedure for get_src"""

    print("Testing get_src")

    # Add the test cases
    # Test case 1
    result = currency.get_src(
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 '
        'Euros", "error": ""}'
    )
    introcs.assert_equals("2 United States Dollars", result)

    # Test case 2
    result = currency.get_src(
        '{"success":false,"src":"","dst":"","error":"Source currency code is '
        'invalid."}'
    )
    introcs.assert_equals("", result)

    # Test case 3
    result = currency.get_src(
        '{"success": true, "src":"3EUR", "dst": "1.772814 Euros", "error": ""}'
    )
    introcs.assert_equals("3EUR", result)

    # Test case 4
    result = currency.get_src(
        '{"success": true, "src": "4USD ", "dst": "1.772814 Euros", "error": '
        '""}'
    )
    introcs.assert_equals("4USD ", result)

    # Test case 5
    result = currency.get_src(
        '{"success":false,"src": "","dst":"","error":"Source currency code is '
        'invalid."}'
    )
    introcs.assert_equals("", result)


def test_get_dst():
    """Test procedure for get_dst"""

    print("Testing get_dst")

    # Add the test cases
    # Test case 1
    result = currency.get_dst(
        '{"success": true, "src": "2 United States Dollars", "dst": "3 CAN", '
        '"error": ""}'
    )
    introcs.assert_equals("3 CAN", result)

    # Test case 2
    result = currency.get_dst(
        '{"success":false,"src":"","dst":"","error":"Source currency code is '
        'invalid."}'
    )
    introcs.assert_equals("", result)

    # Test case 3
    result = currency.get_dst(
        '{"success": true, "src":"3EUR", "dst":"1.772814 Euros", "error": ""}'
    )
    introcs.assert_equals("1.772814 Euros", result)

    # Test case 4
    result = currency.get_dst(
        '{"success": true, "src": "4USD ", "dst":  "5 AU", "error": ""}'
    )
    introcs.assert_equals("5 AU", result)

    # Test case 5
    result = currency.get_dst(
        '{"success":false,"src":"","dst": "","error":"Source currency code is '
        'invalid."}'
    )
    introcs.assert_equals("", result)


def test_has_error():
    """Test procedure for has_error"""

    print("Testing has_error")

    # Add the test cases
    # Test case 1
    result = currency.has_error(
        '{"success":false,"src":"","dst":"","error": "Source currency code is '
        'invalid."}'
    )
    introcs.assert_equals(True, result)

    # Test case 2
    result = currency.has_error(
        '{"success":false,"src":"","dst":"","error":"Source currency code is '
        'invalid."}'
    )
    introcs.assert_equals(True, result)

    # Test case 3
    result = currency.has_error(
        '{"success": true, "src":"3EUR", "dst":"1.772814 Euros", "error": ""}'
    )
    introcs.assert_equals(False, result)

    # Test case 4
    result = currency.has_error(
        '{"success":true, "src": "4USD ", "dst":  "5 AU", "error":""}'
    )
    introcs.assert_equals(False, result)


def test_service_response():
    """Test procedure for service_response"""

    print("Testing service_response")

    # Add the test cases
    # Test case 1
    result = currency.service_response("USD", "EUR", 2.5)
    introcs.assert_equals(
        '{"success": true, "src": "2.5 United States Dollars", "dst": '
        '"2.2160175 Euros", "error": ""}',
        result,
    )

    # Test case 2
    result = currency.service_response("EUR", "BAM", 2.5)
    introcs.assert_equals(
        '{"success": true, "src": "2.5 Euros", "dst": "4.899995148955277 '
        'Bosnia-Herzegovina Convertible Marks", "error": ""}',
        result,
    )

    # Test case 3
    result = currency.service_response("ZOO", "BAM", 2.5)
    introcs.assert_equals(
        '{"success": false, "src": "", "dst": "", "error": "The rate for '
        'currency ZOO is not present."}',
        result,
    )

    # Test case 4
    result = currency.service_response("USD", "EUR", -3.5)
    introcs.assert_equals(
        '{"success": true, "src": "-3.5 United States Dollars", "dst": '
        '"-3.1024244999999997 Euros", "error": ""}',
        result,
    )

    # Test case 5
    result = currency.service_response("USD", "ZOO", 4.5)
    introcs.assert_equals(
        '{"success": false, "src": "", "dst": "", "error": "The rate for '
        'currency ZOO is not present."}',
        result,
    )


def test_iscurrency():
    """Test procedure for iscurrency"""

    print("Testing iscurrency")

    # Add the test cases
    # Test case 1
    result = currency.iscurrency("USD")
    introcs.assert_equals(True, result)

    # Test case 2
    result = currency.iscurrency("USDD")
    introcs.assert_equals(False, result)


def test_exchange():
    """Test procedure for exchange"""

    print("Testing exchange")

    # Add the test cases
    # Test case 1
    result = currency.exchange("USD", "EUR", 2.5)
    introcs.assert_floats_equal(2.2160175, result)

    # Test case 2
    result = currency.exchange("USD", "EUR", -2)
    introcs.assert_floats_equal(-1.772814, result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()

print("All tests completed successfully.")
