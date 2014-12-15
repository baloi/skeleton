def test_transfers():
    transfer = Transfer()
    assert transfer.has_assist() == False

    # transfer has "extensivity"

    # transfer may or may need AD (assistive device)

    # transfer may need assistance or not

def test_resident_transfer_status():
    resident = create_resident_with_transfer() 
    assert resident.transfer.assist == '1A'
    assert resident.transfer.ad == 'RW'
    assert resident.transfer.extensivity == 'mod'
    assert resident.transfer.get_status() == 'modx1A_RW'
    

def create_resident_with_transfer():
    resident = MockResident()
    transfer = Transfer()

    transfer.assist = '1A'
    transfer.extensivity = 'mod'
    transfer.ad = 'RW'

    resident.transfer = transfer

    return resident
    

class MockResident:
    def __init__(self):
        self.transfer = Transfer()
    #    self.transfer = Transfer()

    def needs_assist():
        return False

class Transfer:

    def __init__(self):
        self.extensivity = None
        self.ad          = None
        self.assist      = None

    def has_assist(self):
        if self.assist != None:
            return True
        else:
            return False

    def get_status(self):
        return self.extensivity + 'x' + self.assist + '_' + self.ad
