#!/usr/bin/env python
# coding: utf-8

# In[ ]:

metadata = {
    'apiLevel': '2.5',
    'protocolName': 'DDM_and_TimeTest'
}

def transfer_with_wash(pipette, volume, wells, reagent_wells, wash, waste_well, reservoir):
    for row in range(len(wells)):
        pipette.pick_up_tip()
        for well in range(len(wells[row])):
            pipette.aspirate(volume[row], reservoir[reagent_wells[row]])
            pipette.dispense(volume[row], wells[row][well])
            pipette.aspirate(volume[row], wash)
            pipette.dispense(volume[row], waste_well)
        pipette.drop_tip()
        
alpha_to_num={
    'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13',
    'n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}

def run(protocol):
    reservoir = protocol.load_labware('sarstedt_96_wellplate_310ul', '5')
    temp_mod = protocol.load_module('Temperature Module', '2')
    sample_plate = temp_mod.load_labware('corning_384_wellplate_50ul')

    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_10ul', '3')

    p10 = protocol.load_instrument('p10_single', 'left', tip_racks=[tiprack_1])

    all_wells = sample_plate.rows()
    rows = ['C','D','E','F']
    start_column = 2
    number_of_columns = 13
    target_wells_by_row = []

    for row in rows:
        row_num = int(alpha_to_num[row.lower()]) - 1
        next_column = start_column - 1
        temp_list = []
        for column in range(start_column, start_column + number_of_columns):
            temp_list.append(all_wells[row_num][next_column])
            next_column += 1
        target_wells_by_row.append(temp_list)

    temp_mod.set_temperature(4)

    transfer_with_wash(pipette=p10,
                   volume=[4,4,4,4],
                   wells=target_wells_by_row, 
                   reagent_wells=['A4','A4','A5','A5'],
                   wash=reservoir['A4'],
                   waste_well=reservoir['A5'],
                    reservoir = reservoir)
# this pipetting is taking ~8min

    temp_mod.set_temperature(25)



