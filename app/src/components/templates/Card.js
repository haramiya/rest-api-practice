import React from "react";

export default function Card(props) {
    return (
    <>
        <tr>
            <th className="border-b border-gray-200 bg-gray-200 text-gray-600 w-36">{props.header}</th>
            <td className="border-b border-gray-200 text-gray-700 bg-white pl-3">{props.body}</td>
        </tr>
    </>
    );
}
