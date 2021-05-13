import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
// import Button from "@material-ui/core/Button";
import { EMPLOYEE_CONST, TABLE_HEADER } from "../../../constant/employee";
import { API_ENDPOINT } from "../../../constant/api";
import EmployeesSearch from "./search"
import TableHeader from "../../../templates/TableHead"
import TableBody from "../../../templates/TableBody"
import TablePhoto from "../../../templates/TablePhoto"
import photo from "../../../../assets/img/photo_employee.JPG"

const EmployeesResult = (props) => {

    // レスポンス情報の格納先
    const [employees, setEmployees] = useState([]);

    // 子コンポーネントから呼び出した初期表示や検索時のレスポンス結果を格納する
    const changeEmployees = (data) => {
        setEmployees(data)
    }

    // 初期表示時に社員ALL取得
    useEffect(() => {
        axios
        .get(API_ENDPOINT.EMPLOYEES_ALL)
        .then((res) => setEmployees(res.data));
    }, []);

    // 検索結果テーブルヘッダーのループ処理
    const renderEmployeeTableHeader = TABLE_HEADER.EMPLOYEES_INDEX.map((header) =>
        <TableHeader text={header}/>
    );

    // 検索結果テーブルボディのループ処理
    let renderEmployeeTableBody
    if (employees.length > 0) {
        renderEmployeeTableBody = employees.map((employee) => (
            <tr key={employee.employeeId} className="bg-white hover:bg-gray-100">
                <TablePhoto photo={photo} to={`/employees/${employee.employeeId}`}/>
                <td className="py-3 px-3 border-gray-200 text-blue-600 underline"><Link to={`/employees/${employee.employeeId}`}>{employee.employeeId}</Link></td>
                <TableBody text={employee.employeeName} to={`/employees/${employee.employeeId}`}/>
                <TableBody text={employee.dept} to={`/employees/${employee.employeeId}`}/>
                <TableBody text={employee.joiningYear} to={`/employees/${employee.employeeId}`}/>
                <TableBody text={EMPLOYEE_CONST.title[employee.title]} to={`/employees/${employee.employeeId}`}/>
                <TableBody text={employee.grade} to={`/employees/${employee.employeeId}`}/>
                <TableBody text={EMPLOYEE_CONST.recruitmentClass[employee.recruitmentClass]} to={`/employees/${employee.employeeId}`}/>
                <TableBody text={EMPLOYEE_CONST.gender[employee.gender]} to={`/employees/${employee.employeeId}`}/>
                <TableBody text={employee.birthdate} to={`/employees/${employee.employeeId}`}/>
            </tr>
        ));
    } else {
        // 検索結果が0件だった場合の処理
        renderEmployeeTableBody = <tr><td colspan="11" className="text-center border-gray-200 text-gray-600 py-4 bg-white">該当する社員はいません</td></tr>
    }


    return (
        <>
            {/* search.jsとpropsを共有 */}
            <EmployeesSearch changeEmployees={changeEmployees} />

            {/* 検索結果 */}
            <div className="search_result">
                <table className="w-full shadow-lg">
                    <caption>検索結果</caption>
                    <thead><tr>{renderEmployeeTableHeader}</tr></thead>
                    <tbody>{renderEmployeeTableBody}</tbody>
                </table>
                <div className="py-3"></div>
                {/* <Button size="large" variant="outlined" color="secondary" component={Link} onClick={() => history.goBack()}>戻る</Button> */}
            </div>
        </>
    );
}

export default EmployeesResult;