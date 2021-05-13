import React from "react";
import { Link } from "react-router-dom";

export default function TablePhoto(props) {
    return (
    <>
        <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
            <Link to={props.to}>
                <div className="flex items-center">
                    <div className="flex-shrink-0 h-10 w-10">
                        <img className="h-10 w-10 rounded-full" src={props.photo} alt=""/>
                    </div>
                </div>
            </Link>
        </td>
    </>
    );
}
