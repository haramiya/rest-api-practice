import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import photo from "../../../../assets/img/photo_employee.JPG";
import { EMPLOYEE_CONST } from "../../../constant/employee";
import { API_ENDPOINT } from "../../../constant/api"
import TableHeader from "../../../templates/TableHead"
import TableBody2 from "../../../templates/TableBody2"
import { TABLE_HEADER } from "../../../constant/employee"

const EmployeesInfo = () => {

  // 社員詳細情報結果の格納先
  const [employeeDetails, setEmployeeDetails] = useState({});
  // アドレス情報の格納先
  const [employeeAddress, setEmployeeAddress] = useState({});
  // 研修受講情報リストの格納先
  const [attendTrainings, setAttendTrainings] = useState([]);
  // 資格情報リストの格納先
  const [certificationInfo, setCertificationInfo] = useState([]);

  // URLの末尾から社員番号を取得する
  const { employeeId } = useParams();

  // 初期表示時に社員詳細取得
  useEffect(async () => {
    await axios
      .get((API_ENDPOINT.EMPLOYEES_INFO).replace(":employeeId",employeeId))
      .then((res) => {
        setEmployeeDetails(res.data.employees);
        setEmployeeAddress(res.data.employeesAddress);
        setAttendTrainings(res.data.attendTrainings);
        setCertificationInfo(res.data.certificationInfo);
      });
  }, []);

  // 取得済み資格テーブルヘッダーのループ処理
  const renderEmployeeTableHeader1 = TABLE_HEADER.EMPLOYEES_INFO1.map((header) => (
    <TableHeader text={header}/>
  ))

  // 取得済み資格テーブルボディのループ処理
  let renderEmployeeTableBody1
  if (certificationInfo.length > 0){
    renderEmployeeTableBody1 = certificationInfo.map((certification) => (
      <tr className="bg-white" key={certification.certificationId}>
        <TableBody2 text={certification.certificationId} />
        <TableBody2 text={certification.certificationName} />
        <TableBody2 text={certification.getDate} />
      </tr>
    ));
  } else {
        renderEmployeeTableBody1 = <tr><td colspan="3" className="text-center border-gray-200 text-gray-600 py-4 bg-white">資格を取得していません</td></tr>
  }


    // 参加研修テーブルヘッダーのループ処理
    const renderEmployeeTableHeader2 = TABLE_HEADER.EMPLOYEES_INFO2.map((header) => (
        <TableHeader text={header}/>
  ))

    // 参加研修テーブルボディのループ処理
    let renderEmployeeTableBody2
    if (attendTrainings.length > 0){
      renderEmployeeTableBody2 = attendTrainings.map((attendTraining) => (
        <tbody className="bg-white" key={attendTraining.startDate}>
          <TableBody2 text={attendTraining.trainingName}/>
          <TableBody2 text={attendTraining.startDate}/>
          <TableBody2 text={attendTraining.satisfactionScore}/>
        </tbody>
      ));
    } else {
      renderEmployeeTableBody2 = <tr><td colspan="3" className="text-center border-gray-200 text-gray-600 py-4 bg-white">研修を受講していません</td></tr>
    }


  return (
    <>
      <div className="overflow-x-hidden bg-gray-100">
        <div className="mb-5 mt-10"></div>

        {/* 社員写真 */}
        <div className="photo ml-48 mt-10">
          <img className="shadow-lg rounded-full" src={photo} />
          <h2 className="text-center text-2xl my-5">{employeeDetails.employeeName}</h2>
        </div>

        {/* 社員詳細 */}
        <div className="info_employee mr-36">
          <h2 className="text-gray-700 text-3xl font-medium font-bol border-gray-500 mb-5 text-center">社員詳細</h2>
          <table className="rounded-lg shadow-lg">
            <tr>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">社員番号</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">{employeeDetails.employeeId}</td>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">所属会社</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">{employeeAddress.company}</td>
            </tr>
            <tr>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">部署</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">{employeeDetails.dept}</td>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">役職</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">{EMPLOYEE_CONST.title[employeeDetails.title]}</td>
            </tr>
            <tr>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">性別</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">{EMPLOYEE_CONST.gender[employeeDetails.gender]}</td>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">入社年度</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">{employeeDetails.joiningYear}</td>
            </tr>
            <tr>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">等級</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">{employeeDetails.grade}</td>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">生年月日</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">{employeeDetails.birthdate}</td>
            </tr>
            <tr>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">採用区分</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">
                {EMPLOYEE_CONST.recruitmentClass[employeeDetails.recruitmentClass]}
              </td>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">休職有無</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">{EMPLOYEE_CONST.leaveFlg[employeeDetails.leaveFlg]}</td>
            </tr>
            <tr>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">メール</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">{employeeAddress.mailAddress}</td>
              <th className="border-b border-gray-200 bg-gray-200 text-gray-600">備考</th>
              <td className="border-b border-gray-200 bg-white text-gray-700">-</td>
            </tr>
          </table>

          <div className="py-5"></div>

          {/* 資格取得情報 */}
          <div className="info_capacity">
            <table className="rounded-lg shadow-lg">
              <thead>{renderEmployeeTableHeader1}</thead>
              {renderEmployeeTableBody1}
            </table>
          </div>

          <div className="py-5"></div>

          {/* 研修参加情報 */}
          <div className="info_trainings">
            <table className="rounded-lg shadow-lg">
              <thead>{renderEmployeeTableHeader2}</thead>
              {renderEmployeeTableBody2}
            </table>
          </div>

          <div className="py-5"></div>
          {/* <Button size="large" variant="outlined" color="secondary" component={Link} onClick={() => history.goBack()}>
          戻る
          </Button> */}
        </div>
      </div>
    </>
  );
};

export default EmployeesInfo;
