import unittest

from nli_python import encode_point

from .data import encode_decode_examples


class DecodeTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_results_returned(self):
		for example in encode_decode_examples:

			loc = example["location"]
			nli_code = example["nli_code"]

			code_res = encode_point(*loc)
			self.assertEqual(code_res, nli_code, f'Code for {loc}')


if __name__ == '__main__':
	unittest.main()
