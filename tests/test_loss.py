import unittest

import numpy as np

from transformer_tts.model.losses import new_scaled_crossentropy, masked_crossentropy


class TestCharTokenizer(unittest.TestCase):

    def test_crossentropy(self):
        scaled_crossentropy = new_scaled_crossentropy(index=2, scaling=5)

        targets = np.array([[0, 1, 2]])
        logits = np.array([[[.3, .2, .1], [.3, .2, .1], [.3, .2, .1]]])

        loss = scaled_crossentropy(targets, logits)
        self.assertAlmostEqual(2.3705523014068604, float(loss), places=6)

        scaled_crossentropy = new_scaled_crossentropy(index=2, scaling=1)
        loss = scaled_crossentropy(targets, logits)
        self.assertAlmostEqual(0.7679619193077087, float(loss), places=6)

        loss = masked_crossentropy(targets, logits)
        self.assertAlmostEqual(0.7679619193077087, float(loss), places=6)
