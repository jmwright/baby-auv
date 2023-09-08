import cadquery as cq
import parameters as params
from components.auv_hull import hull
from components.auv_rear_clamp import clamp as rear_clamp
from components.auv_forward_bulkhead import bulkhead as forward_bulkhead
from components.auv_antenna_extension import extension_tube
from components.helpers import append_sys_path, handle_args
from documenter import document


def build_auv_assembly():
    """Puts all the components of the assembly together in a CadQuery Assembly object"""

    # Define assembly colors to tell the components apart
    hull_color = cq.Color(0.75, 0.75, 0.75, 1.0)
    rear_clamp_color = cq.Color(0.04, 0.5, 0.67, 1.0)
    forward_bulkhead_color = cq.Color(0.565, 0.698, 0.278, 1.0)

    # Components of the assembly
    auv_assy = cq.Assembly()
    hull_model = hull(params)

    # Add the body as the fixed, central component
    auv_assy = auv_assy.add(hull_model, color=hull_color)

    # Add the rear clamp
    auv_assy = auv_assy.add(
        rear_clamp(params).rotateAboutCenter((1, 0, 0), 30),
        color=rear_clamp_color,
        loc=cq.Location((3.0, 0.0, 0.0), (0, 0, 1), 180),
    )

    # Add the forward bulkhead
    auv_assy = auv_assy.add(
        forward_bulkhead(params),
        color=forward_bulkhead_color,
        loc=cq.Location((12.0, 0.0, 0.0), (0, 0, 1), 180),
    )

    # Add the antenna extension tube
    auv_assy = auv_assy.add(
        extension_tube(params),
        color=forward_bulkhead_color,
        loc=cq.Location((-2.0, 26.0, 0.0), (0, 0, 1), 180),
    )

    return auv_assy


def main(args):
    """Main entry point to the app for command line users"""

    from cadquery.vis import show

    # Generate documentation
    if args.document == True:
        append_sys_path(".")
        document(".", None)
    # Display the assembly
    else:
        assy = build_auv_assembly()
        show(assy)


if __name__ == "__main__":
    main(handle_args())
