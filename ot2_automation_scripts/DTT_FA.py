#!/usr/bin/env python
# coding: utf-8

# In[ ]:


metadata = {
    'apiLevel': '2.5',
    'protocolName': 'DTT-FA'
}

def transfer_with_wash(pipette, volume, wells, reagent_wells, wash, waste_well, reservoir):
    for row in range(len(wells)):
        pipette.pick_up_tip()
        for well in range(len(wells[row])):
            pipette.aspirate(volume[row], reservoir[reagent_wells[row]])
            pipette.dispense(volume[row], wells[row][well])
            pipette.aspirate(volume[row], wash[row])
            pipette.dispense(volume[row], waste_well[row])
        pipette.drop_tip()

alpha_to_num = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11',
    'l': '12', 'm': '13',
    'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23',
    'x': '24', 'y': '25', 'z': '26'}

def run(protocol):
    reservoir = protocol.load_labware('sarstedt_96_wellplate_310ul', '5')
    temp_mod = protocol.load_module('Temperature Module', '2')
    sample_plate = temp_mod.load_labware('corning_384_wellplate_50ul')
    wash_1 = protocol.load_labware('sarstedt_96_wellplate_310ul', '8')
    wash_2 = protocol.load_labware('sarstedt_96_wellplate_310ul', '4')

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

    temp_mod.set_temperature(25)

#DDM
    transfer_with_wash(pipette=p10,
                   volume=[1,1,1,1],
                   wells=target_wells_by_row,
                   reagent_wells=['B2','B3','B4','B5'],
                   wash=[wash_1['A3'],wash_1['A5'],wash_1['A7'],wash_1['A9']],
                   waste_well= [wash_1['A4'],wash_1['A6'],wash_1['A8'],wash_1['A10']],
                    reservoir = reservoir)

    temp_mod.set_temperature(70)

#70 C incubation
    #15min
    protocol.delay(minutes=7)
    transfer_with_wash(pipette=p10,
                   volume=[2,2,2,2],
                   wells=target_wells_by_row,
                   reagent_wells=['B7','B8','B9','B10'],
                   wash=[wash_1['B3'],wash_1['B5'],wash_1['B7'],wash_1['B9']],
                   waste_well= [wash_1['B4'],wash_1['B6'],wash_1['B8'],wash_1['B10']],
                    reservoir = reservoir)
    #30 min
    protocol.delay(minutes=7)
    transfer_with_wash(pipette=p10,
                   volume=[2,2,2,2],
                   wells=target_wells_by_row,
                   reagent_wells=['C2','C3','C4','C5'],
                   wash=[wash_1['C3'],wash_1['C5'],wash_1['C7'],wash_1['C9']],
                   waste_well= [wash_1['C4'],wash_1['C6'],wash_1['C8'],wash_1['C10']],
                    reservoir = reservoir)
    #45 min
    protocol.delay(minutes=7)
    transfer_with_wash(pipette=p10,
                   volume=[2,2,2,2],
                   wells=target_wells_by_row,
                   reagent_wells=['C7','C8','C9','C10'],
                   wash=[wash_1['D3'],wash_1['D5'],wash_1['D7'],wash_1['D9']],
                   waste_well= [wash_1['D4'],wash_1['D6'],wash_1['D8'],wash_1['D10']],
                    reservoir = reservoir)
    #60 min
    protocol.delay(minutes=7)
    transfer_with_wash(pipette=p10,
                   volume=[2,2,2,2],
                   wells=target_wells_by_row,
                   reagent_wells=['D2','D3','D4','D5'],
                   wash=[wash_1['E3'],wash_1['E5'],wash_1['E7'],wash_1['E9']],
                   waste_well= [wash_1['E4'],wash_1['E6'],wash_1['E8'],wash_1['E10']],
                    reservoir = reservoir)

    temp_mod.set_temperature(25)
#IAA
    transfer_with_wash(pipette=p10,
                   volume=[1,1,1,1],
                   wells=target_wells_by_row,
                   reagent_wells=['D7','D8','D9','D10'],
                   wash=[wash_1['F3'],wash_1['F5'],wash_1['F7'],wash_1['F9']],
                   waste_well= [wash_1['F4'],wash_1['F6'],wash_1['F8'],wash_1['F10']],
                    reservoir = reservoir)
    protocol.delay(minutes=30)
#LYS-C
    transfer_with_wash(pipette=p10,
                   volume=[1,1,1,1],
                   wells=target_wells_by_row,
                   reagent_wells=['E2','E3','E4','E5'],
                   wash=[wash_1['G3'],wash_1['G5'],wash_1['G7'],wash_1['G9']],
                   waste_well= [wash_1['G4'],wash_1['G6'],wash_1['G8'],wash_1['G10']],
                    reservoir = reservoir)
    temp_mod.set_temperature(37)
    protocol.delay(minutes=172)
# Trypsin
    transfer_with_wash(pipette=p10,
                   volume=[1,1,1,1],
                   wells=target_wells_by_row,
                   reagent_wells=['E7','E8','E9','E10'],
                   wash=[wash_1['H3'],wash_1['H5'],wash_1['H7'],wash_1['H9']],
                   waste_well= [wash_1['H4'],wash_1['H6'],wash_1['H8'],wash_1['H10']],
                    reservoir = reservoir)
    protocol.delay(minutes=172)
#3H
    transfer_with_wash(pipette=p10,
                   volume=[2,2,2,2],
                   wells=target_wells_by_row,
                   reagent_wells=['F2','F3','F4','F5'],
                   wash=[wash_2['A3'],wash_2['A5'],wash_2['A7'],wash_2['A9']],
                   waste_well= [wash_2['A4'],wash_2['A6'],wash_2['A8'],wash_2['A10']],
                    reservoir = reservoir)
    protocol.delay(minutes=172)
#6H
    transfer_with_wash(pipette=p10,
                   volume=[2,2,2,2],
                   wells=target_wells_by_row,
                   reagent_wells=['F7','F8','F9','F10'],
                   wash=[wash_2['B3'],wash_2['B5'],wash_2['B7'],wash_2['B9']],
                   waste_well= [wash_2['B4'],wash_2['B6'],wash_2['B8'],wash_2['B10']],
                    reservoir = reservoir)
    protocol.delay(minutes=172)
#9H
    transfer_with_wash(pipette=p10,
                   volume=[2,2,2,2],
                   wells=target_wells_by_row,
                   reagent_wells=['G2','G3','G4','G5'],
                   wash=[wash_2['C3'],wash_2['C5'],wash_2['C7'],wash_2['C9']],
                   waste_well= [wash_2['C4'],wash_2['C6'],wash_2['C8'],wash_2['C10']],
                    reservoir = reservoir)
    protocol.delay(minutes=172)
#12H
    transfer_with_wash(pipette=p10,
                   volume=[1,1,1,1],
                   wells=target_wells_by_row,
                   reagent_wells=['G7','G8','G9','G10'],
                   wash=[wash_2['D3'],wash_2['D5'],wash_2['D7'],wash_2['D9']],
                   waste_well= [wash_2['D4'],wash_2['D6'],wash_2['D8'],wash_2['D10']],
                    reservoir = reservoir)

#FA
    temp_mod.set_temperature(25)
    transfer_with_wash(pipette=p10,
                   volume=[1,1,1,1],
                   wells=target_wells_by_row,
                   reagent_wells=['H2','H3','H4','H5'],
                   wash=[wash_2['E3'],wash_2['E5'],wash_2['E7'],wash_2['E9']],
                   waste_well= [wash_2['E4'],wash_2['E6'],wash_2['E8'],wash_2['E10']],
                    reservoir = reservoir)
    protocol.delay(minutes=52)
