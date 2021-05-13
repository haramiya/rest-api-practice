import React from "react";

export default function Checkbox(props) {
    return (
    <>
        <label className="inline-flex items-center ml-3 text-gray-700">
            <input
                type="checkbox"
                className="form-checkbox h-4 w-4"
                ref={props.register}
                name={props.name}
                value={props.value}
            ></input>
            <span className="ml-2 text-gray-700">{props.text}</span>
        </label>
    </>
    );
}
