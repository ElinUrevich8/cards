class HandFactory:
    @staticmethod
    def three_of_a_kind() -> Hand:
        return Hand.from_string("Ah As Ac Jh Th")
    
    @staticmethod
    def pair() -> Hand:
        return Hand.from_string("Ah As Jh Th Qh")
    
    @staticmethod
    def high_card_kicker_ace() -> Hand:
        return Hand.from_string("Ah 2s Jh Th Qh")
    
