import cadquery as cq

from components.auv_hull import hull
from components.auv_front_clamp import clamp as front_clamp
from components.auv_rear_clamp import clamp as rear_clamp
from components.auv_forward_bulkhead import bulkhead as forward_bulkhead
from components.auv_rear_bulkhead import bulkhead as rear_bulkhead
from components.auv_antenna_extension import extension_tube
from components.auv_cage import cage
from components.auv_depth_nipple import nipple
from components.auv_006_oring import oring
from components.auv_neoprene_gasket import gasket
from cq_annotate import explode_assembly


hull_length = 520.0  # mm
exploded = False

def build_auv_assembly():
    """Puts all the components of the assembly together in a CadQuery Assembly object"""

    # Define assembly colors to tell the components apart
    hull_color = cq.Color(0.75, 0.75, 0.75, 0.25)
    clamp_color = cq.Color(0.408, 0.278, 0.553, 1.0)
    cage_color = cq.Color(0.04, 0.5, 0.67, 1.0)
    bulkhead_color = cq.Color(0.565, 0.698, 0.278, 1.0)
    hardware_color = cq.Color(0.996, 0.867, 0.0, 1.0)
    seal_color = cq.Color(0.122, 0.125, 0.133, 1.0)

    # Components of the assembly
    auv_assy = cq.Assembly()

    # Add the body as the fixed, central component
    auv_assy.add(hull(), color=hull_color)

    # Add the forward bulkhead
    auv_assy.add(
        forward_bulkhead(),
        color=bulkhead_color,
        loc=cq.Location((12.0, 0.0, 0.0), (0, 0, 1), 180),
        metadata={"explode_loc": cq.Location((60, 0, 0))},
    )

    # Add the front clamp
    auv_assy.add(
        front_clamp(),
        color=clamp_color,
        loc=cq.Location((-4.0, 0.0, 0.0), (1, 0, 0), 90),
        metadata={"explode_loc": cq.Location((-84, 0, 0))},
    )

    # Add the antenna extension tube
    auv_assy.add(
        extension_tube(),
        color=hardware_color,
        loc=cq.Location((0.0, 26.0, 0.0), (0, 0, 1), 180),
        metadata={"explode_loc": cq.Location((100, 0, 0))},
    )

    # Add the rear bulkhead
    auv_assy.add(
        rear_bulkhead(),
        color=bulkhead_color,
        loc=cq.Location((hull_length - 12.0, 0.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((60, 0, 0))},
    )

    # Add the rear clamp
    auv_assy.add(
        rear_clamp().rotateAboutCenter((1, 0, 0), 30),
        color=clamp_color,
        loc=cq.Location((hull_length - 3.0, 0.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((80, 0, 0))},
    )

    # Add the cage
    auv_assy.add(
        cage(),
        color=cage_color,
        loc=cq.Location((hull_length + 2.0, 0.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((100, 0, 0))},
    )

    # Add the depth gauge nipple
    auv_assy.add(
        nipple(),
        color=hardware_color,
        loc=cq.Location((hull_length - 22.0, 9.6, -24.4), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((100, 0, 0))},
    )

    # Add the o-ring for the conductivity sensor
    auv_assy.add(
        oring(),
        color=seal_color,
        loc=cq.Location((hull_length - 13.0, -23.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((40, 0, 0))},
    )

    # Add the rear neoprene expansion gasket
    auv_assy.add(
        gasket(),
        color=seal_color,
        loc=cq.Location((hull_length - 6.0, 0.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((71, 0, 0))},
    )

    # Add the forward neoprene expansion gasket
    auv_assy.add(
        gasket(),
        color=seal_color,
        loc=cq.Location((0.0, 0.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((-75, 0, 0))},
    )

    # Explode the assembly if the user requested it
    if exploded:
        explode_assembly(auv_assy)

    return auv_assy


if "show_object" in globals() or __name__ == "__cqgi__":
    show_object(build_auv_assembly())
