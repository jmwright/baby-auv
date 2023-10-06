# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
m3_tap_drill_size = 2.5  # mm - size to drill a hole to tap for an M3
pcd_rad = 33.0  # mm - Bulkhead hole pattern radius
hole_dia = 3.25  # mm - Bulkhead clearance hole diameter


def clamp():
    """Generates the rear clamp of the AUV"""

    # Outer and inner radii of the first step
    step_1_or = 82.5 / 2.0
    step_1_ir = 72.5 / 2.0

    # Outer and inner radii of the second step
    step_2_or = 88.0 / 2.0
    step_2_ir = 59.5 / 2.0

    # Outer and inner radii of the third step
    step_3_or = 84.0 / 2.0
    step_3_ir = 59.5 / 2.0

    # Outer and inner radii of the forth step
    step_4_or = 84.0 / 2.0
    step_4_ir = 76.0 / 2.0

    # First step of the rear clamp that slips inside the body tube
    rc = cq.Workplane("YZ").circle(step_1_or).circle(step_1_ir).extrude(3.0)

    # Second step of the rear clamp
    rc = rc.faces(">X").workplane().circle(step_2_or).circle(step_2_ir).extrude(2.0)

    # Third step of the rear clamp
    rc = rc.faces(">X").workplane().circle(step_3_or).circle(step_3_ir).extrude(1.0)

    # Forth step of the rear clamp
    rc = rc.faces(">X").workplane().circle(step_4_or).circle(step_4_ir).extrude(6.0)

    # Add the polar hole pattern
    rc = (
        rc.faces(">X")
        .workplane()
        .polarArray(pcd_rad, 60, 360, 6)
        .hole(hole_dia)
    )

    # Add the cage mounting hole pattern
    mounting_hole_or = m3_tap_drill_size / 2.0
    rc = (
        rc.workplane(
            centerOption="CenterOfBoundBox", offset=3.0 - mounting_hole_or / 2.0
        )
        .transformed(rotate=cq.Vector(90, 30, 0))
        .circle(mounting_hole_or)
        .cutThruAll()
    )
    rc = (
        rc.transformed(rotate=cq.Vector(0, 60, 0)).circle(mounting_hole_or).cutThruAll()
    )
    rc = (
        rc.transformed(rotate=cq.Vector(0, -120, 0))
        .circle(mounting_hole_or)
        .cutThruAll()
    )

    return rc


if "show_object" in globals() or __name__ == "__cqgi__":
    show_object(clamp())
