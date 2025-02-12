# Copyright (c) 2020 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


class BitUtils:
    """ Class container for bit utility functions. """

    @staticmethod
    def IsBitSet(value: int,
                 bit_num: int) -> bool:
        """ Get if the specified bit is set.

        Args:
            value (int): value
            bit_num (int): bit number to check

        Returns:
            bool: True if bit is set, false otherwise
        """
        return (value & (2 << bit_num)) != 0

    @staticmethod
    def SetBit(value: int,
               bit_num: int) -> int:
        """ Set the specified bit.

        Args:
            value (int): value
            bit_num (int): bit number to check

        Returns:
            int: value with the specified bit set
        """
        value = value | (2 << bit_num)
        return value

    @staticmethod
    def ResetBit(value: int,
                 bit_num: int) -> int:
        """ Reset the specified bit.

        Args:
            value (int): value
            bit_num (int): bit number to check

        Returns:
            int: value with the specified bit reset
        """
        value = value & ~(2 << bit_num)
        return value
