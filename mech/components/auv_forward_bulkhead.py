# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
pcd_rad = 33.0  # mm - Bulkhead hole pattern radius
hole_dia = 3.25  # mm - Bulkhead clearance hole diameter
major_dia = 82.5
minor_dia = 72.0
step_heights = 6.0
pcb_hole_dia = 2.5  # Circuit board mounting hole diameter


def bulkhead():
    """Generates the forward bulkhead of the AUV"""

    # First step of the shape
    major_rad = major_dia / 2.0
    bh = cq.Workplane("YZ").circle(major_rad).extrude(step_heights)

    # Second step of the shape
    minor_rad = minor_dia / 2.0
    bh = bh.faces(">X").workplane().circle(minor_rad).extrude(step_heights)

    # Add the polar hole pattern
    bh = (
        bh.faces(">X")
        .workplane()
        .polarArray(pcd_rad, 30, 360, 6)
        .hole(hole_dia, 8.0)
    )

    # Add the antenna hole
    bh = bh.faces(">X").workplane().center(-26.0, 0.0).hole(4.0)

    # Add circuit board mounting holes
    bh = (
        bh.faces("<X")
        .workplane(centerOption="CenterOfBoundBox")
        .rarray(18.5 * 2.0, 20.9 * 2.0, 2, 2)
        .hole(pcb_hole_dia, 3.0)
    )

    return bh


if "show_object" in globals() or __name__ == "__cqgi__":
    show_object(bulkhead())
