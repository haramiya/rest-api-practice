import React, { useState, useEffect } from "react";
import axios from "axios";
import {  useParams } from "react-router-dom";
// import Button from "@material-ui/core/Button";
import { TRAINING_CONST, TABLE_HEADER } from "../../../constant/training";
import { API_ENDPOINT } from "../../../constant/api"
import TableHeader from "../../../templates/TableHead"
import TableBody2 from "../../../templates/TableBody2"
import TablePhoto from "../../../templates/TablePhoto"
import Card from "../../../templates/Card"
import photo from "../../../../assets/img/photo_employee.JPG"

const TrainingsInfo = () => {

    // 研修詳細情報の格納先
    const [trainingDetails, setTrainingDetails] = useState({});

    // 参加社員リストの格納先
    const [attendLists, setAttendLists] = useState([]);

    // URL末尾の研修IDを取得
    const { trainingId } = useParams();

    // 初期表示時に研修詳細取得
    useEffect(async () => {
        await axios
        .get((API_ENDPOINT.TRAININGS_INFO).replace(":trainingId",trainingId))
        .then((res) => {
            setAttendLists(res.data.TrainingInfo_TrainingInfo);
            setTrainingDetails(res.data.body_2);
        });
    }, []);

    // 参加社員リストテーブルヘッダーのループ処理
    const renderTrainingTableHeader = TABLE_HEADER.TRAININGS_INFO.map((header) => (
        <TableHeader text={header}/>
    ))

    // 参加社員リストテーブルボディのループ処理
    let renderTrainingTableBody
    if (attendLists.length > 0){
        renderTrainingTableBody = attendLists.map((attendList) => (
            <tr className="bg-white" key={attendList.employeeId}>
                <TablePhoto photo={photo}/>
                <TableBody2 text={attendList.employeeId}/>
                <TableBody2 text={attendList.employeeName}/>
                <TableBody2 text={attendList.dept}/>
                <TableBody2 text={TRAINING_CONST.title[attendList.title]}/>
                <TableBody2 text={attendList.grade}/>
                <TableBody2 text={TRAINING_CONST.recruitmentClass[attendList.recruitmentClass]}/>
                <TableBody2 text={attendList.joiningYear}/>
                <TableBody2 text={TRAINING_CONST.attendance_state[attendList.attendance_state]}/>
                <TableBody2 text={attendList.satisfaction_score}/>
            </tr>
        ));
    } else {
        // 検索結果が0件の場合の処理
        renderTrainingTableBody = <tr><td colspan="10" className="text-center border-gray-200 text-gray-600 py-4">参加社員はいません</td></tr>
    }

    return (
        <>
            <div className="overflow-x-hidden bg-gray-100 mx-28">
                <div className="result_training">
                <h2 className="text-gray-700 text-3xl font-medium font-bol border-gray-500 mt-8 text-center">研修詳細</h2>
                    <table className="box rounded-lg shadow-lg">
                        <Card header="研修名" body={trainingDetails.trainingName}/>
                        <Card header="研修分類" body={TRAINING_CONST.trainingClass[trainingDetails.trainingClass]}/>
                        <Card header="スキル分類" body={TRAINING_CONST.skillClass[trainingDetails.skillClass]}/>
                        <Card header="IT人材レベル" body={TRAINING_CONST.ITLevel[trainingDetails.ITLevel]}/>
                        <Card header="概要" body={trainingDetails.summary}/>
                        <Card header="研修分類" body={TRAINING_CONST.trainingClass[trainingDetails.trainingClass]}/>
                        <Card header="募集人数" body={trainingDetails.recruitmentNum}/>
                        <Card header="参加人数" body={trainingDetails.participationNum}/>
                        <Card header="実施回数" body={trainingDetails.numOfTimes}/>
                    </table>

                    {/* <!-- 検索結果テーブル２ --> */}
                    <table className="my-6 rounded-lg shadow-lg">
                        <Card header="研修開始日" body={trainingDetails.startDate}/>
                        <Card header="研修終了日" body={trainingDetails.endDate}/>
                        <Card header="1回あたりの時間" body={trainingDetails.timePerSession}/>
                        <Card header="既存/新規" body={TRAINING_CONST.newFlg[trainingDetails.newFlg]}/>
                        <Card header="選抜/募集" body={TRAINING_CONST.selectionFlg[trainingDetails.selectionFlg]}/>
                        <Card header="概要" body={trainingDetails.summary}/>
                        <Card header="参加条件" body={trainingDetails.conditions}/>
                        <Card header="講師名" body={trainingDetails.teacher}/>
                        <Card header="備考" body={trainingDetails.remarks}/>
                    </table>
                </div>
            </div>

            <div>
                <table className="shadow-lg bg-white mx-auto w-4/5">
                    <thead><tr>{renderTrainingTableHeader}</tr></thead>
                    <tbody>{renderTrainingTableBody}</tbody>
                </table>
                {/* <Button size="large" variant="outlined" color="secondary" component={Link} onClick={() => history.goBack()}>
                戻る
                </Button> */}
            </div>
        </>
    );
};

export default TrainingsInfo;
