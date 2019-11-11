import unittest
from collections.abc import Iterable
from typing import Callable, List


def run_sub_tests(test_case: unittest.TestCase, func: Callable,
                  input_values: List, solutions: List, apply_to_out: Callable = None) -> None:
    """For a given callable (func), run sub-tests for each [input_values <-> solutions] pair.
    Sub-tests make it easy to have all your tests run through even if some tests fail in the mean time.
    This function makes it convenient to test multiple inputs (input_values list) against multiple expected outputs
    (solutions list).

    Example usage
    -------------
    def test_square_variants(self):
        input_values = [1, 2, 3, 4]
        expected_outputs = [1, 4, 9, 16]
        for func in [square_variant_1, square_variant_2]:
            run_sub_tests(self, func, input_values, expected_outputs)  # self is the instance of a unittest.TestCase

    Arguments
    --------
        test_case:      An instance of unittest.TestCase (i.e. 'self' when used within a TestCase test function).
        func:           A callable which represents the function you want to test.
        input_values:   A list of input test cases. Might be a list of iterables if func takes in multiple arguments,
                        those will be unrolled automatically via asterix operator.
        solutions:      Expected solutions matching the cases in input_values.
        apply_to_out:   Callable which will transform the output of the test function
                        before asserting equality with solution.
    """
    for idx, (input_args, expected_solution) in enumerate(zip(input_values, solutions)):
        with test_case.subTest(test_case=f'Func: {func.__name__}, test: {idx}.'):
            if isinstance(input_args, Iterable):
                result = apply_to_out(func(*input_args)) if apply_to_out else func(*input_args)
            else:
                result = apply_to_out(func(input_args)) if apply_to_out else func(input_args)
            test_case.assertEqual(expected_solution, result,
                                  f'Sub test nr. {idx} failed. {func.__name__}({input_args}) '
                                  f'should be {expected_solution}.')