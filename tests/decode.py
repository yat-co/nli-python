import unittest

from nli_python import decode_point

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
			lat, long, elev, elev_type = decode_point(nli_code)
			self.assertEqual(lat, loc[0], f'Latitude for {nli_code}')
			self.assertEqual(long, loc[1], f'Longitude for {nli_code}')
			self.assertEqual(elev, loc[2], f'Elevation for {nli_code}')
			self.assertEqual(elev_type, loc[3], f'Elevation Type for {nli_code}')


if __name__ == '__main__':
	unittest.main()
