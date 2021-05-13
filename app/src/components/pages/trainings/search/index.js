import React from "react";
import TrainingsResult from "./result"

const TrainingsIndex = () => {

    return (
    <>
        <div className="overflow-x-hidden bg-gray-100">
            <div className="mx-auto px-24 py-8 items-center">
                <h2 className="text-gray-700 text-3xl font-medium font-bol border-gray-500 text-center mb-5">研修一覧</h2>
                <TrainingsResult/>
            </div>
        </div>
    </>
    );
};

export default TrainingsIndex;
