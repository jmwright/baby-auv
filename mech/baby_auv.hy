#!/usr/bin/env hy

(import cadquery :as cq)
(import parameters :as params)
(import components.auv_hull [hull])
(import components.auv_rear_clamp [clamp :as rear_clamp])
(import components.auv_forward_bulkhead [bulkhead :as forward_bulkhead])
(import components.helpers [append_sys_path handle_args])
(import documenter [document])


(defn build_auv_assembly []
    "Puts all the components of the assembly together in a CadQuery Assembly object"

    ; Define assembly colors to tell the components apart
    (setv hull_color (cq.Color 0.75 0.75 0.75 1.0))
    (setv rear_clamp_color (cq.Color 0.04 0.5 0.67 1.0))
    (setv forward_bulkhead_color (cq.Color 0.565 0.698 0.278 1.0))

    ; Components of the assembly
    (setv auv_assy (cq.Assembly))
    (setv hull_model (hull params))

    ; Add the body as the fixed, central component
    (setv auv_assy
        (auv_assy.add hull_model :color hull_color))

    ; Add the rear clamp
    (setv auv_assy
        (auv_assy.add (.rotateAboutCenter (rear_clamp params) #(1, 0, 0) 30) :color rear_clamp_color :loc (cq.Location #(3.0 0.0 0.0) #(0, 0, 1) 180))
    )

    ; Add the forward bulkhead
    (setv auv_assy
        (auv_assy.add (forward_bulkhead params) :color forward_bulkhead_color :loc (cq.Location #(12.0 0.0 0.0) #(0, 0, 1) 180))
    )

    (return auv_assy)
)


(defn main [args]
    "Main entry point to the app for command line users"

    (import cadquery.vis [show])

    (if (= args.document True)
        (do
            (append_sys_path ".")

            (document "." None)
        ) ; generate documentation
        (do
            (setv assy (build_auv_assembly))
            (show assy)
        ) ; generate and show the assembly
    )
)


(if (= __name__ "__main__")
    (main (handle_args))
    None)
