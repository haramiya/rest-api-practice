import React from "react";

export default function SearchHeader2(props) {
    return (
    <>
        <td className="border-b border-gray-200 bg-gray-200 text-gray-600 w-auto text-center">
            {props.text}
        </td>
    </>
    );
}
