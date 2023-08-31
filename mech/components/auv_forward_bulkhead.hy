; All units are in mm unless otherwise stated

(import hy)
(import cadquery :as cq)

(defn bulkhead [params]
    "Generates the forward bulkhead of the AUV"

    ; Dimensions of the first step
    (setv step_1_or (/ 82.5 2.0))
    (setv step_1_ir (/ 72.5 2.0))

    ; First step of the bulkhead that slips inside the body tube
    (setv bh
        (.extrude (.circle (.circle (cq.Workplane "YZ") step_1_or) step_1_ir) 3.0)
    )

    ; Dimensions of the second step
    (setv step_2_or (/ 88.0 2.0))
    (setv step_2_ir (/ 59.5 2.0))

    ; Second step of the bulkhead
    (setv bh
        (.extrude (.circle (.circle (.workplane (bh.faces ">X")) step_2_or) step_2_ir) 2.0)
    )

    ; Dimensions of the third step
    (setv step_3_or (/ 84.0 2.0))
    (setv step_3_ir (/ 59.5 2.0))

    ; Third step of the bulkhead
    (setv bh
        (.extrude (.circle (.circle (.workplane (bh.faces ">X")) step_3_or) step_3_ir) 1.0)
    )

    ; Dimensions of the forth step
    (setv step_4_or (/ 84.0 2.0))
    (setv step_4_ir (/ 76.0 2.0))

    ; Forth step of the bulkhead
    (setv bh
        (.extrude (.circle (.circle (.workplane (bh.faces ">X")) step_4_or) step_4_ir) 6.0)
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

    (setv
        opts
        {
            "width" 800
            "height" None
            "marginLeft" 10
            "marginTop" 10
            "showAxes" False
            "projectionDir" #(1.0 0.0 0.0)
            "strokeWidth" 0.5
            "strokeColor" svg_line_color
            "hiddenColor" svg_hidden_color
            "showHidden" False
        }
    )
    ; Get the path to the documentation images and manufacturing output files
    (setv docs_images_path (get_docs_images_path __file__))
    (setv manufacturing_files_path (get_manufacturing_files_path __file__))

    ; Generate the model so it can be exported
    (setv bh (bulkhead params))

    ; Export the end view of the body tube in SVG
    ; # bh = add_circular_dimensions(bh, arrow_scale_factor=0.25)
    (setv final_path ((. os path join) docs_images_path "forward_bulkhead_right_side_view.svg"))
    (cq.exporters.export
        bh
        final_path
        :opt opts
    )

    ; Export the end view of the body tube in DXF
    (setv final_path ((. os path join) manufacturing_files_path "forward_bulkhead_right_side_view.dxf"))
    (cq.exporters.export
        bh
        final_path
    )
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