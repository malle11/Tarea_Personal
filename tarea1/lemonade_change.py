class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cinco = 0
        diez = 0

        for billete in bills:
            if billete == 5:
                cinco += 1

            elif billete == 10:
                if cinco == 0:
                    return False

                cinco -= 1
                diez += 1

            elif billete == 20:
                if diez > 0 and cinco > 0:
                    diez -= 1
                    cinco -= 1
                elif cinco >= 3:
                    cinco -= 3
                else:
                    return False

        return True
