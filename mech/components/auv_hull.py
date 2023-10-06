# All units are in mm unless otherwise stated

import cadquery as cq

hull_diameter = 88.9
hull_wall_thickness = 3.0
hull_length = 520.0


def hull():
    """Generates the main hull tube of the AUV"""

    # Convert diameter to radius
    hull_radius = hull_diameter / 2.0

    # The overall tube shape
    hl = (
        cq.Workplane("YZ")
        .circle(hull_radius)
        .circle(hull_radius - hull_wall_thickness)
        .extrude(hull_length)
    )

    # Tag edges for dimensioning
    hl.edges("%CIRCLE").edges(cq.selectors.RadiusNthSelector(1)).edges(">X").tag(
        "radius_1"
    )

    return hl

if "show_object" in globals() or __name__ == "__cqgi__":
    show_object(hull())
