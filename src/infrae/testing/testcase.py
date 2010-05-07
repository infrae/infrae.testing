# Copyright (c) 2010 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from Acquisition import aq_base

import hashlib
import unittest


class TestCase(unittest.TestCase):
    """Add some usefull assert methods to the default Python TestCase.
    """

    def assertHashEqual(self, first, second, msg=None):
        """Assert the hash values of two strings are the same. It is
        commonly used to compare two large strings.
        """
        hash_first = hashlib.md5(first)
        hash_second = hashlib.md5(second)
        msg = msg or 'string hashes are different.'
        self.assertEquals(hash_first.hexdigest(), hash_second.hexdigest(), msg)

    def assertSame(self, first, second, msg=None):
        """Assert that first is the same same object than second,
        Acquisition wrapper removed. If the condition is not
        satisfied, the test will fail with the given msg if not None.
        """
        if msg is None:
            msg = u'%r is not %r' % (first, second)
        if aq_base(first) is not aq_base(second):
            raise self.failureException, msg

    def assertStringEqual(self, first, second, msg=None):
        """Assert two string are equals ignore extra white spaces
        around them.
        """
        self.assertEqual(first.strip(), second.strip(), msg)

    def assertListEqual(self, first, second, msg=None):
        """Assert that the list first and second contains the same
        object, without paying attention to the order of the
        elements. If the condition is not satisfied, the test will
        fail with the given msg if not None.
        """
        sorted_first = sorted(list(first))
        sorted_second = sorted(list(second))
        if msg is None:
            msg = u'%r != %s' % (sorted_first, sorted_second)
        if not sorted_first == sorted_second:
            raise self.failureException, msg
