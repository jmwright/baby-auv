; All units are in mm unless otherwise stated

(import cadquery :as cq)

(defn body [params]
    "Generates the main body tube of the AUV"

    ; To shorten some of the equations
    (setv body_radius (/ params.body_diameter 2.0))

    ; The overall tube shape
    (setv bd
        (.extrude
            (.circle
                (.circle (cq.Workplane "YZ") body_radius)
                (- body_radius params.wall_thickness)
            )
            params.body_length
        )
    )

    ; Add dimension tags
    (.tag (.edges (.edges (bd.edges "%CIRCLE") (cq.selectors.RadiusNthSelector 1)) ">X") "radius_1")

    (return bd)
    )


(defn document [params]
    "Allows this model to be documented by itself or part of a larger system"

    (import os)
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
    (setv bd (body params))

    ; Export the end view of the body tube in SVG
    ; # bd = add_circular_dimensions(bd, arrow_scale_factor=0.25)
    (setv final_path (os.path.join docs_images_path "body_right_side_view.svg"))
    (cq.exporters.export
        bd
        final_path
        :opt opts
    )

    ; Export the end view of the body tube in DXF
    (setv final_path (os.path.join manufacturing_files_path "body_right_side_view.dxf"))
    (cq.exporters.export
        bd
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
            (setv bd (body params))
            (show bd)
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