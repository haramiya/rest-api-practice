import React from "react";
import EmployeesResult from "./result"

const EmployeesIndex = () => {

    return (
        <>
            <div className="overflow-x-hidden bg-gray-100">
                <div className="mx-auto px-48 py-8">
                <h2 className="text-gray-700 text-3xl font-medium font-bol border-gray-500 text-center mb-5">社員一覧</h2>
                    <div className="bg-gray-100 flex flex-col xs:flex-row items-center xs:justify-between">
                        <EmployeesResult/>
                    </div>
                </div>
            </div>
        </>
    );
};

export default EmployeesIndex;
