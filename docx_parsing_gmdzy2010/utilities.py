import math
import re


class Price2UpperChinese:
    """This class convert a normal price to chinese upper characters.
    As an example:
    
    1003456789.45
    
    this normal price with 2 decimal digits above are split to
    four sections:
    
    yi(亿): 10, wan(万): 345, yuan(元): 6789, decimal: 45
    
    that is:
    
    拾亿零叁佰肆拾伍万陆仟柒佰捌拾玖元零肆角伍分
    
    all of the number will be mapped to chinese in upper case.
    
    The key to solve the problem is to deal with each sections of the price,
    and follow the rule of adding zero(零) under each special case.
    """
    
    base_map = {
        1: "元", 10: "拾", 100: "佰", 1000: "仟", 10000: "万", 100000000: "亿"
    }
    char_map = {
        0: "零", 1: "壹", 2: "贰", 3: "叁", 4: "肆", 5: "伍", 6: "陆", 7: "柒",
        8: "捌", 9: "玖",
    }

    def __init__(self, price):
        base = 10000
        self.price = price
        self.decimal = round(math.modf(price)[0], 2)
        self.yi_wan_yuan = int(math.modf(price)[1])
        self.yuan = int(round(math.modf(self.yi_wan_yuan / base)[0] * base, 4))
        self.yi_wan = math.modf(self.yi_wan_yuan / base)[1]
        self.wan = int(round(math.modf(self.yi_wan / base)[0] * base, 4))
        self.yi = int(math.modf(self.yi_wan / base)[1])
    
    def _get_digit_char(self, number=None, base=1):
        """Each part of the final string should contain the unit, in spite of
        the unit_digit, which is no any chance mapping to "零"。"""
        digit = int((number / base) % 10)
        if base == 1:
            digit_char = self.char_map.get(digit) if digit else ""
        else:
            digit_unit = "{}{}".format(
                self.char_map.get(digit), self.base_map.get(base)
            )
            digit_char = digit_unit if digit else "零"
        return digit_char
    
    def _get_section_char(self, number=None, base=1):
        """This method should handle the state of the excessive "零" when any
        section number performs the operation of MOD."""
        thousand_char = self.get_thousand_char(number=number)
        hundred_char = self.get_hundred_char(number=number)
        ten_char = self.get_ten_char(number=number)
        unit_char = self.get_unit_char(number=number)
        if not number % 100:
            ten_char = re.sub(r'零', '', ten_char)
            hundred_char = re.sub(r'零', '', hundred_char)
            if number == 0:
                thousand_char = re.sub(r'零', '', thousand_char)
        chars = [thousand_char, hundred_char, ten_char, unit_char]
        suffix = self.base_map.get(base) if self.price > base else ""
        return "{}{}".format("".join(chars), suffix)
    
    def get_thousand_char(self, number=None):
        return self._get_digit_char(number=number, base=1000)
    
    def get_hundred_char(self, number=None):
        return self._get_digit_char(number=number, base=100)
    
    def get_ten_char(self, number=None):
        return self._get_digit_char(number=number, base=10)
    
    def get_unit_char(self, number=None):
        return self._get_digit_char(number=number, base=1)
    
    def get_section_char_decimal(self):
        """This method returns the chinese character of decimal part of the
        price."""
        hundredths, tenths = math.modf(self.decimal * 10)
        hundredths_num = int(round(hundredths, 1) * 10)
        tenths_num = int(round(tenths, 1))
        hund_char = self.char_map[hundredths_num]
        tent_char = self.char_map[tenths_num]
    
        # for the special case, string "零" should not be contained in the
        # decimal character when the self.integer is 0.
        zero = "零" if self.yi_wan_yuan else ""
        status_map = {
            (True, True): "{}{}角{}分".format(zero, tent_char, hund_char),
            (True, False): "{}{}角".format(zero, tent_char),
            (False, True): "{}{}分".format(zero, hund_char),
            (False, False): "整",
        }
        return status_map[(bool(tenths_num), bool(hundredths_num))]
    
    def get_section_char_yuan(self):
        return self._get_section_char(number=self.yuan)
    
    def get_section_char_wan(self):
        return self._get_section_char(number=self.wan, base=10000)
    
    def get_section_char_yi(self):
        return self._get_section_char(number=self.yi, base=100000000)
    
    @staticmethod
    def zero_check(char):
        """Multi-zero char will be filtered and those excessive zero char will
        be deleted."""
        char = re.sub(r'零零零', '零', char)
        char = re.sub(r'零零', '零', char)
        return char
    
    def _get_final_char(self):
        return "{}{}{}{}".format(
            self.zero_check(self.get_section_char_yi()),
            self.zero_check(self.get_section_char_wan()),
            self.zero_check(self.get_section_char_yuan()),
            self.zero_check(self.get_section_char_decimal()),
        )

    def __str__(self):
        final_char = re.sub(r'^零', '', self._get_final_char())
        final_char = re.sub(r'亿万', '亿零', final_char)
        return final_char
