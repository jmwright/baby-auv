# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
straight_length = 25.0  # mm
barb_half_length = 5.0  # mm
tube_od = 4.0  # mm
tube_id = 2.0  # mm
barb_od = 4.9  # mm
barb_length = 5.0  # mm


def nipple():
    """Generates the nipple for the depth sensor tube."""

    # Main tube shape
    np = cq.Workplane("YZ").circle(tube_od / 2.0).extrude(straight_length)

    # Hose barb
    np = (
        np.faces(">X")
        .workplane()
        .circle(barb_od / 2.0)
        .extrude(barb_length, taper=-174.75)
    )

    # Post-barb tube
    np = np.faces(">X").workplane().circle(tube_od / 2.0).extrude(2.0)

    # Center hole
    np = np.faces(">X").workplane().circle(tube_id / 2.0).cutThruAll()

    return np


show_object(nipple())
