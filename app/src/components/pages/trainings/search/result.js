import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
// import Button from "@material-ui/core/Button";
import { TRAINING_CONST, TABLE_HEADER } from "../../../constant/training";
import { API_ENDPOINT } from "../../../constant/api";
import TrainingsSearch from "./search"
import TableBody from "../../../templates/TableBody"
import TableHeader from "../../../templates/TableHead"

const TrainingsResult = (props) => {

    // 社員情報の格納先
    const [ trainings, setTrainings] = useState([]);

    // 子コンポーネントから呼び出した初期表示や検索時のレスポンス結果を格納する
    const changeTrainings = (data) => {
        setTrainings(data)
    }

    // 初期表示時に社員ALL取得
    useEffect(() => {
        axios.get(API_ENDPOINT.TRAININGS_ALL)
        .then((res) => setTrainings(res.data));
    }, []);

    // 検索結果テーブルヘッダーのループ処理
    const renderTrainingTableHeader = TABLE_HEADER.TRAININGS_INDEX.map(
        (header) => (
            <TableHeader text={header}/>
        )
    );

    // 検索結果テーブルボディのループ処理
    let renderTrainingTableBody
    if (trainings.length > 0){
        renderTrainingTableBody = trainings.map((training) => (
                <tr className="bg-white hover:bg-gray-100" key={training.trainingId}>
                    <td className="py-3 px-3 border-gray-200 text-blue-600 underline"><Link to={`/trainings/${training.trainingId}`}>{training.trainingId}</Link></td>
                    <TableBody text={training.trainingName} to={`/trainings/${training.trainingId}`}/>
                    <TableBody text={TRAINING_CONST.trainingClass[training.trainingClass]} to={`/trainings/${training.trainingId}`}/>
                    <TableBody text={TRAINING_CONST.skillClass[training.skillClass]} to={`/trainings/${training.trainingId}`}/>
                    <TableBody text={TRAINING_CONST.ITLevel[training.ITLevel]} to={`/trainings/${training.trainingId}`}/>
                    <TableBody text={training.recruitmentNum} to={`/trainings/${training.trainingId}`}/>
                    <TableBody text={training.participationNum} to={`/trainings/${training.trainingId}`}/>
                    <TableBody text={TRAINING_CONST.newFlg[training.newFlg]} to={`/trainings/${training.trainingId}`}/>
                    <TableBody text={TRAINING_CONST.selectionFlg[training.selectionFlg]} to={`/trainings/${training.trainingId}`}/>
                    <TableBody text={training.startDate} to={`/trainings/${training.trainingId}`}/>
                    <TableBody text={training.endDate} to={`/trainings/${training.trainingId}`}/>
                </tr>
        ));
    } else {
        // 検索結果0件時の処理
        renderTrainingTableBody = <tr>
            <td colspan="11" className="text-center border-gray-200 text-gray-600 py-4 bg-white">該当する研修はありません</td>
        </tr>
    }

    return (
        <>
            {/* <!-- 検索条件テーブル --> */}
            <TrainingsSearch  changeTrainings={changeTrainings} />
            <div className="items-center">
                <table className="w-full shadow-lg">
                    <caption>検索結果　　　</caption>
                    <thead><tr>{renderTrainingTableHeader}</tr></thead>
                    <tbody>{renderTrainingTableBody}</tbody>
                </table>
                {/* <Button size="large" variant="outlined" color="secondary" component={Link} onClick={() => history.goBack()}>戻る</Button> */}
            </div>
        </>
    )
}

export default TrainingsResult;