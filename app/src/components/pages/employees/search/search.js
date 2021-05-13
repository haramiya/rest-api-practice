import React from "react";
import axios from "axios";
import { useForm } from "react-hook-form";
import { EMPLOYEE_CONST } from "../../../constant/employee";
import { API_ENDPOINT } from "../../../constant/api";
import Button from "../../../templates/Button"
import TextBox from "../../../templates/TextBox"
import Calendar from "../../../templates/Calendar"
import Checkbox from "../../../templates/CheckBox"
import SearchHeader from "../../../templates/SearchHead"

const EmployeesSearch = (props) => {

    // ref属性がregisterがであるものを監視
    const { register, handleSubmit } = useForm();

    // 検索ボタン押下時の処理
    const onSubmit = (data) => {

        //入力がないデータをリクエストボディから排除
        for (const key in data) {
            if (data[key] == "") {
                delete data[key];
        }}

        // 入力値をJSON形式に変換
        const params = JSON.stringify(data);

        // API処理
        axios({
            method: "POST",
            url: API_ENDPOINT.EMPLOYEES_SEARCH,
            data: params,
            headers: { "Content-Type": "application/json; charset=utf-8" },
        }).then((res) => {
            console.log("click search button");
            console.log(res.data);
            // 親コンポーネント（result.js）のstateのemployeesを変更する
            props.changeEmployees(res.data);
        });
    };

        // 部署チェックボックスのループ処理
        const renderInputDept = EMPLOYEE_CONST.dept.map((dept) =>
        <Checkbox register={register} name="dept" value={dept} text={dept}/>
    );

    // 役職チェックボックスのループ処理
    const renderInputTitle = Object.entries(EMPLOYEE_CONST.title).map(([key, title]) =>
        <Checkbox register={register} name="title" value={key} text={title}/>
    );

    // 等級チェックボックスのループ処理
    const renderInputGrade = EMPLOYEE_CONST.grade.map((grade) =>
        <Checkbox register={register} name="grade" value={grade} text={grade}/>
    );

    return (
        <>
            {/* 検索条件 */}
            <form onSubmit={handleSubmit(onSubmit)}>
            <table className="border-gray-200 shadow-lg">
                <tbody>
                    <tr>
                        <SearchHeader text="社員番号"/>
                        <TextBox register={register} name="employeeId"/>
                    </tr>
                    <tr>
                        <SearchHeader text="社員名"/>
                        <TextBox register={register} name="employeeName"/>
                    </tr>
                    <tr>
                        <SearchHeader text="部署"/>
                        <td className="border-b border-gray-200 bg-white">{renderInputDept}</td>
                    </tr>
                    <tr>
                        <SearchHeader text="入社年度"/>
                        <td className="border-b border-gray-200 bg-white">
                            <Calendar register={register} name="joiningYearFrom" /> ~ 
                            <Calendar register={register} name="joiningYearTo" />
                        </td>
                    </tr>
                    <tr>
                        <SearchHeader text="役職"/>
                        <td className="border-b border-gray-200 bg-white">{renderInputTitle}</td>
                    </tr>
                    <tr>
                        <SearchHeader text="等級"/>
                        <td className="border-b border-gray-200 bg-white">{renderInputGrade}</td>
                    </tr>
                    <tr>
                        <SearchHeader text="採用区分"/>
                        <td className="border-b border-gray-200 bg-white">
                            <Checkbox register={register} name="recruitmentClass" value="1" text="新卒"/>
                            <Checkbox register={register} name="recruitmentClass" value="2" text="中途"/>
                        </td>
                    </tr>
                    <tr>
                        <SearchHeader text="休職有無"/>
                        <td className="border-b border-gray-200 bg-white">
                            <Checkbox register={register} name="leaveFlg" value="1" text="有" />
                            <Checkbox register={register} name="leaveFlg" value="0" text="無" />
                        </td>
                    </tr>
                    <tr>
                        <SearchHeader text="性別"/>
                        <td className="border-b border-gray-200 bg-white">
                            <Checkbox register={register} name="gender" value="1" text="男" />
                            <Checkbox register={register} name="gender" value="2" text="女" />
                        </td>
                    </tr>
                    <tr>
                        <SearchHeader text="生年月日"/>
                        <td className="border-b border-gray-200 bg-white">
                            <Calendar register={register} name="birthdateFrom" /> ~ 
                            <Calendar register={register} name="birthdateTo" />
                        </td>
                    </tr>
                </tbody>
            </table>
            <div className="py-5 ml-96"><Button/></div>
            </form>
        </>
    );
}

export default EmployeesSearch;