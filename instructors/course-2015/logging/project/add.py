"""
A simple set of math methods that we can build our
logging infrastructure on top of.


"""
import lib.logger


def add_some_numbers(a, b):
    """ Adds the passed parameters and returns the result.

    """

    logger_name = 'add_some_numbers'
    logger = logging.getLogger(__name__).getChild(logger_name)

    result = a + b
    
    logger.info("Result of add_some_numbers: {}".format(result))

    return result


if __name__ == "__main__":
    """ Rudimentary tests, nothing should be returned. 

    In the event of a test failure, we get an AssertionError.
    """

    try:
        result = add_some_numbers(4,5)
        expected_result = 9
        assert result == expected_result
        add_logger.info("PASS: Add succeeded, {} == {}".format(result, expected_result))
    except AssertionError:
        add_logger.info("FAIL: Add failed, {} != {}".format(result, expected_result))
                
    try:
        result = add_some_numbers(5,5)
        expected_result = 9
        assert not (result == expected_result)
        add_logger.info("PASS: Add failed, {} != {}".format(result, expected_result))
    except AssertionError:
        add_logger.info("FAIL: Add succeeded, {} == {}".format(result, expected_result))






