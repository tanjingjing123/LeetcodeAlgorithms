class solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        w_unit = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
                  'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        w_ten = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        unit = num % 10
        ten = (num // 10) % 10
        hundred = (num // 100) % 10
        thousand = (num // 1000) % 1000
        million = (num // 10 ** 6) % 1000
        billion = (num // 10 ** 9) % 1000

        word = w_unit[ten * 10 + unit] if ten == 1 else w_unit[unit]
        if ten > 1:
            word = w_ten[ten] + ' ' + word
        if hundred: word = w_unit[hundred] + ' Hundred ' + word
        if thousand: word = self.numberToWords(thousand) + ' Thousand ' + word
        if million: word = self.numberToWords(million) + ' Million ' + word
        if billion: word = self.numberToWords(billion) + ' Billion ' + word
        return word.strip()

obj = solution()
num = 1234567891
print(obj.numberToWords(num))