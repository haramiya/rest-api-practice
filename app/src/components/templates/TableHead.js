import React from "react";

export default function TableHeader(props) {
  return (
    <>
      <th className="py-3 px-3 border-gray-300 bg-gray-200 uppercase text-sm text-gray-600">
        {props.text}
      </th>
    </>
  );
}
