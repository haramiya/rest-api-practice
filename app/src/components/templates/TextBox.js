import React from "react";

export default function TextBox(props) {
    return (
        <>
            <td className="border-b border-gray-200 bg-white">
                <input
                    type="text"
                    className="ml-3 border-2 border-gray-200 rounded-md"
                    ref={props.register}
                    name={props.name}
                    maxLength={props.maxLength}
                    minLength={props.minLength}
                    required={props.required}
                />
            </td>
        </>
    );
}
