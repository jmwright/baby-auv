# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
id = 72  # mm
rect_cross_section = 6  # mm


def gasket():
    """Generates the neoprene expansion gasket"""

    gskt = (
        cq.Workplane("YZ")
        .circle(id / 2.0 + rect_cross_section)
        .circle(id / 2.0)
        .extrude(rect_cross_section)
    )

    return gskt


if "show_object" in globals() or __name__ == "__cqgi__":
    show_object(gasket())
