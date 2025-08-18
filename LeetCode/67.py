# Add Binary

def trim_leading_zeros(s: str):
    first_one =  s.find('1')
    return s[first_one:] if first_one != -1 else '0'

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # trim leading zeros
        a = trim_leading_zeros(a)
        b = trim_leading_zeros(b)

        m, n = len(a), len(b)
        if n > m:
            a, b = b, a
            m, n = n, m

        carry = 0
        result = []
        j = n - 1

        for i in range(m-1, -1, -1):
            bit1 = int(a[i])
            bit_sum = bit1 + carry

            if j >= 0:
                bit2 = int(b[j])
                bit_sum += bit2
                j -= 1
            
            # calculate the result bit and udpate carry
            bit = bit_sum % 2
            carry = bit_sum // 2

            # update the current bit in result
            result.append(str(bit))
        
        if carry > 0:
            result.append('1')

        return ''.join(result[::-1])

def main():
    solution = Solution()
    print(solution.addBinary('11', '1'))
    print(solution.addBinary('1010', '1011'))

if __name__ == '__main__':
    main()