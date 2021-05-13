import React from "react";
import { Link } from "react-router-dom";

export default function TableBody(props) {
    return (
    <>
        <td className="border-gray-300 text-gray-600 px-0 py-0">
            <Link className="block w-full px-3 py-3 align-middle" to={props.to}>
                {props.text}
            </Link>
        </td>
    </>
    );
}
