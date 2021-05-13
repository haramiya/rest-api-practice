import React from "react";

export default function SearchButton() {
  return (
    <>
      <button
        type="submit"
        className="my-3 bg-red-500 hover:bg-red-600 text-white font-bold py-2.5 px-6 rounded shadow-lg focus:outline-none"
      >
        検索
      </button>
    </>
  );
}
