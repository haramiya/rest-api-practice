import React from "react";

export default function Calnedar(props) {
    return (
        <>
            <input
                type="date"
                className="ml-3 border-2 border-gray-200 rounded-md"
                ref={props.register}
                name={props.name}
            />
        </>
    );
}
