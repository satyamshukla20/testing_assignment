from ParkingLot import ParkingLot

def test_create_parking_lot():
    p = ParkingLot()
    assert p.create_parking_lot(0) == 0
    assert p.create_parking_lot(6) == 6

def test_park_and_leave():
    p = ParkingLot()
    p.create_parking_lot(3)
    assert p.park('UP-10-X-1111', 'White') == 1
    assert p.park('UP-10-X-2222', 'White') == 2
    assert p.park('UP-10-X-0000', 'Black') == 3
    assert p.leave_slot(2) == True
    assert p.leave_slot(1) != False
    assert p.get_empty_slot()==0
    assert p.park('UP-10-X-1111', 'White') == 1
    assert p.park('UP-10-X-2222', 'White') == 2
    assert p.park('UP-10-X-4444', 'White') == -1
    assert p.leave_slot(2) == True
    assert p.get_empty_slot() == 1
    assert p.get_empty_slot() != 2





def test_getters():
    p = ParkingLot()
    q= ParkingLot()
    p.create_parking_lot(4)
    
    assert q.show_data('create_parking_lot 4') == None
    assert p.get_empty_slot() == 0
    p.park('UP-10-X-1111', 'White')
    p.park('UP-10-X-2222', 'White')
    p.park('UP-10-X-4444', 'Black')
    assert p.get_empty_slot() == 3

    assert p.get_slotno_from_regno('UP-10-X-1111') == 1
    assert p.get_slotno_from_regno('UP-10-X-2222') == 2
    assert p.get_slotno_from_regno('UP-10-X-4444') != 2

    assert p.get_slotno_from_color('White') == ['1', '2']
    assert p.get_slotno_from_color('Black') == ['3']
    assert p.get_slotno_from_color('BLack') != ['4']

    assert p.get_regno_from_color('White') == ['UP-10-X-1111', 'UP-10-X-2222']
    assert p.get_regno_from_color('Black') != ['UP-10-X-1111', 'UP-10-X-2222']

    
