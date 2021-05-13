import React from "react";

export default function TextArea(props) {
    return (
        <>
            <td className="border-b border-gray-200 bg-white">
                <textarea
                    className="ml-3 border-2 border-gray-200 rounded-md"
                    ref={props.register}
                    name={props.name}
                    rows={props.rows}
                    cols={props.cols}
                    required={props.required}
                />
            </td>
        </>
    );
}
