from collections import namedtuple
from conn_molex_global_params import generate_footprint_name


Params = namedtuple("Params",[
    'series_name',
    'part_name',
    'file_name',
    'num_pins',
    'pin_pitch'
])


def generate_params(num_pins, series_name, part_name, pin_pitch):

    return Params(
        series_name=series_name,
        part_name=part_name,
        file_name=generate_footprint_name(series_name, part_name, num_pins, pin_pitch),
        num_pins=num_pins,
        pin_pitch=pin_pitch
    )


all_params = {
    'molex_54722_02x08_0.5mm' : generate_params(16, '54722', '0164', 0.5),								
    'molex_54722_02x40_0.5mm' : generate_params(80, '54722', '0804', 0.5)								
}


class seriesParams():

# UPDATED

    pin_inside_distance = 1.05 + 0.5				# Distance between centre of end pin and end of body
    pocket_inside_distance = (10.1 - (8.95 + 0.5)) / 2.0 	# Distance between end of pocket and end of body
    island_inside_distance = (10.1 - 8.0) / 2.0         	# Distance between end of island and end of body

    body_width = 5.0
    body_height = 1.15				
    body_fillet_radius = 0.15
    body_chamfer = 0.1

    pocket_width = 2.8
    pocket_base_thickness = 0.2
    pocket_fillet_radius = 0.05

    island_width = 1.65

    hole_width = 0.3
    hole_length = 0.3
    hole_offset = (body_width + pocket_width) / 4.0
    # hole_depth = 1.3

    rib_width = 0.25
    rib_depth = 2.0 * body_chamfer

    slot_height = body_height - 0.05
    slot_depth = 0.3

    notch_width = 1.2
    notch_depth = 0.1
    
    pin_width = 0.15
    pin_thickness = 0.075




calcDim = namedtuple( 'calcDim', ['pin_group_width', 'length', 'pocket_length', 'island_length', 'rib_group_outer_width', 'slot_width'])


def dimensions(params):
    pin_group_width = ((params.num_pins / 2) - 1) * params.pin_pitch
    length =  pin_group_width + 2 * seriesParams.pin_inside_distance
    pocket_length = length - 2.0 * seriesParams.pocket_inside_distance
    island_length = length - 2.0 * seriesParams.island_inside_distance
    rib_group_outer_width = pin_group_width + params.pin_pitch + seriesParams.rib_width
    slot_width = params.pin_pitch - seriesParams.rib_width
  # length = 
    # slot_length = ((params.num_pins / 2) - 1) * params.pin_pitch + 2 * seriesParams.slot_outside_pin
    # bottom_void_width = 2 * (params.pin_y_pitch + seriesParams.pin_thickness/2.0)
    # ramp_height = 11.7 - seriesParams.body_height
    # if params.num_pins > seriesParams.ramp_split_breakpoint:
        # ramp_width = params.pin_pitch * 2
        # ramp_offset = params.pin_pitch * (params.num_pins -5) / 2
    # else:
        # ramp_width = (params.num_pins - 1) * params.pin_pitch / 2
        # ramp_offset = 0
    return calcDim(pin_group_width=pin_group_width, length = length, pocket_length=pocket_length, island_length = island_length, rib_group_outer_width=rib_group_outer_width, slot_width=slot_width)


"""
    pin_width = 0.7
    pin_chamfer_long = 0.1
    pin_chamfer_short = 0.1
    pin_height = 5
    pin_thickness = 0.3


    foot_height = 1.5
    foot_width = 1.7
    foot_length = 7.62
    foot_inside_distance = 0.5 				# Distance between outside edge of foot and end of body

    marker_x_inside = pin_inside_distance - 1
    marker_y_inside = 1.2
    marker_size = 1.0
    marker_depth = 0.5

    slot_outside_pin = 1.27
    slot_width = 1.9
    slot_depth = 7.62
    slot_chamfer = 0.5

    top_void_depth = 4.0
    top_void_width = 6.5

    recess_depth = pin_inside_distance - 1.27 - 1.28
    recess_large_width = 4
    recess_small_width = 3
    recess_height = 11.43



    pin_depth = 3.56					# DIMENSION F depth below bottom surface of base

    body_channel_depth = 0.6
    body_channel_width = 1.5
    body_cutout_length = 1.2
    body_cutout_width = 0.6

    ramp_split_breakpoint = 6				# Above this number of pins, the tab is split into two parts
    ramp_chamfer_x = 0.3
    ramp_chamfer_y = 0.7
"""
