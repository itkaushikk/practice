class Solution:
    def diagonalPrime(self, nums) -> int:
        def prime_number(number):
            is_prime = True
            if number == 1:
                is_prime = False
                return is_prime

            for r in range(2, int(number/2)):
                if number%r == 0:
                    is_prime = False
                    break
            return is_prime
            
        largest_prime_number = 0

        number_of_rows = len(nums)
        for i in range(number_of_rows):
            number = nums[i][i]

            if largest_prime_number < number:
                is_prime = prime_number(number)
                if is_prime:
                    largest_prime_number = number
            
            number = nums[i][number_of_rows-i-1]
            if largest_prime_number < number:
                is_prime = prime_number(number)
                if is_prime:
                    largest_prime_number = number
        
        return largest_prime_number