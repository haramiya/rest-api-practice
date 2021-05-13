import React from "react";

export default function RadioButton(props) {
    return (
    <>
        <label class="inline-flex items-center ml-3">
        <input
            type="radio"
            class="form-radio h-5 w-5 text-red-600"
            ref={props.register}
            name={props.name}
            value={props.value}
            required={props.required}
        />
        <span class="ml-2 text-gray-700">{props.text}</span>
        </label>
    </>
    );
}
