; All units are in mm unless otherwise stated

(import hy)
(import cadquery :as cq)

; Parameters
(setv major_dia 82.5)
(setv minor_dia 72.0)
(setv step_heights 6.0)
(setv pcb_hole_dia 2.5) ; Circuit board mounting hole diameter

(defn bulkhead [params]
    "Generates the forward bulkhead of the AUV"

    ; First step of the shape
    (setv major_rad (/ major_dia 2.0))
    (setv bh (.extrude (.circle (cq.Workplane "YZ") major_rad) step_heights))

    ; Second step of the shape
    (setv minor_rad (/ minor_dia 2.0))
    (setv bh (.extrude (.circle (.workplane (bh.faces ">X")) minor_rad) step_heights))

    ; Add the polar hole pattern
    (setv bh
        (.hole (.polarArray (.workplane (bh.faces ">X")) params.pcd_rad 30 360 6) params.hole_dia 8.0)
    )

    ; Add the antenna hole
    (setv bh
        (.hole (.center (.workplane (bh.faces ">X")) -26.0, 0.0) 4.0)
    )

    ; Add circuit board mounting holes
    (setv bh
        (.hole (.rarray (.workplane (bh.faces "<X") :centerOption "CenterOfBoundBox") (* 18.5 2.0) (* 20.9 2.0) 2 2) pcb_hole_dia 3.0)
    )

    (return bh)
)


(defn document [params]
    "Allows this model to be documented by itself or part of a larger system"

    ; Make sure that the helpers module can be found no matter how this is run
    (import os)
    (import sys)
    (import path)
    (setv directory (.abspath (path.Path __file__)))
    (sys.path.append directory.parent)

    (import helpers [get_docs_images_path get_manufacturing_files_path])

    (setv svg_line_color #(10 10 10))
    (setv svg_hidden_color #(127 127 127))
)


(defn main [args]
    (import helpers [append_sys_path])
    (append_sys_path ".")
    (import parameters :as params)

    (if (= args.document True)
        (document params)
        (do
            (import cadquery.vis [show])

            ; Generate the model and display it
            (setv bh (bulkhead params))
            (show bh)
        )
    )
)


(if (= __name__ "__main__")
    (do
        (import helpers [handle_args])
        (main (handle_args))
    )
    None
)
