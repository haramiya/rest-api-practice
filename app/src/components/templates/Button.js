import React from "react";

export default function SearchButton(props) {
  return (
    <>
      <button
        type="submit"
        className="my-3 bg-red-500 hover:bg-red-600 text-white font-bold py-2.5 px-6 rounded shadow-lg focus:outline-none"
      >
        {props.text}
      </button>
    </>
  );

}

// Propsのデフォルト値
SearchButton.defaultProps = {
  text: "検索"
}